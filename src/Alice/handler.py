"""
This module contains handlers for Yandex Alice
"""

import datetime
import json
import logging
import traceback

import requests

log = logging.getLogger(__name__)

teachers = requests.get("https://storage.yandexcloud.net/bot-scheduler/teachers.json").json()['teachers']


def get_schedule(teacher_id, date) -> dict:
    """Get schedule for teacher by id and date."""

    url = f"https://storage.yandexcloud.net/bot-scheduler/{teacher_id}.json"

    print(url)

    schedule = requests.get(url)

    if schedule.status_code != 200:
        print("status_code", schedule.status_code)
        print("text", schedule.text)
        return {}

    schedule = schedule.json()

    schedule = schedule.get(date.strftime("%d.%m.%Y"), {})

    return schedule


def get_windows(teachers_schedule) -> list[dict]:
    """Get windows from schedule."""

    print(teachers_schedule)

    start_time = datetime.time(8, 00)
    end_time = datetime.time(21, 30)

    # занятое время
    busy_times = []

    # проходимся по всем учителям
    for teacher, teacher_schedule in teachers_schedule.items():
        # проходимся по всем занятиям учителя
        for lesson in teacher_schedule:
            # добавляем в список занятое время
            busy_times.append(lesson["time"])

    busy_times = list(set(busy_times))

    # свободное время
    free_time = []


    tt = start_time

    busy_times.sort()

    print('busy_times', busy_times)

    for busy_time in busy_times:
        print('st', busy_time.split("-")[0])
        print('st2', *busy_time.split("-")[0].split(":"))
        st = datetime.time(*map(int, busy_time.split("-")[0].split(":")))
        et = datetime.time(*map(int, busy_time.split("-")[1].split(":")))

        if tt < st:
            free_time.append([tt, st])
        tt = et

    if tt < end_time:
        free_time.append([tt, end_time])

    # Проверяем что промежуток больше 10 минут
    _ = [] 
    for s, e in free_time:
        if (datetime.datetime.combine(datetime.date.today(), e) - datetime.datetime.combine(datetime.date.today(), s)).seconds > 600:
            _.append([s, e])

    free_time = _

    print(free_time)
    return free_time



def process_event(event: dict) -> dict:
    """Process event from Yandex Alice and return response."""

    log.info("Event: %s", event)

    request = event["request"]
    response = {
        "version": event["version"],
        "session": event["session"],
        "response": {
            "end_session": False,
        },
    }

    # сущности
    entities = request["nlu"].get("entities", [])
    # команда
    command = request["command"].lower()
    # токены
    tokens = request["nlu"]["tokens"]

    if command in ["привет", "здравствуй", "здравствуйте", ""]:
        ans = "\n".join([
            "Привет!",
            "Я могу показать расписание преподавателя или найти свободные окна для встречи нескольких преподавателей.",
            "Назовите дату и преподователя или нескольких преподавателей и я покажу свободные окна.",
        ])

        response["response"]["text"] = ans

        return response

    date = None
    names = []

    print('names', names)

    # если есть сущности
    for entity in entities:
        # если тип сущности - дата
        if entity["type"] == "YANDEX.DATETIME":
            # получаем дату
            if entity["value"].get("day_is_relative", False):
                date = datetime.datetime.now() + datetime.timedelta(days=entity["value"].get("day", 0))
            else:
                day = entity["value"].get("day", None)
                month = entity["value"].get("month", None)
                year = entity["value"].get("year", None)

                if day and month and year:
                    date = datetime.datetime(year=year, month=month, day=day)
                elif day and month:
                    # 2022-2023 учебный год
                    if month > 8:
                        year = 2022
                    else:
                        year = 2023
                    date = datetime.datetime(year=year, month=month, day=day)

        # если тип сущности - имя
        elif entity["type"] == "YANDEX.FIO":
            # получаем имя
            names.append(entity["value"].get("last_name", ''))

    print(date, names)

    if not date:
        date = datetime.datetime.now()

    teachers_schedule = {}

    print("names", names)

    names_not_found = []

    for name in names:
        for teacher in teachers:
            if teacher['title'].split()[0].lower().replace("ё", "е") == name.lower():
                print(teacher)
                teachers_schedule[teacher['name']] = get_schedule(teacher['id'], date)
            else:
                names_not_found.append(name)

    names_not_found = list(set(names_not_found))
            
    

    if "расписание" in tokens:
        if not teachers_schedule:
            if names_not_found:
                response["response"]["text"] = f"Не найдены преподаватели: {', '.join(names_not_found)}"
            else:
                response["response"]["text"] = "Укажите преподавателя"
        else:
            response["response"]["text"] = "Расписание:\n"
            response["response"]["tts"] = "Расписание: - - "
            for teacher, schedule in teachers_schedule.items():
                response["response"]["text"] += f"\n{teacher}\n\n"
                response["response"]["tts"] += f"- - {teacher} - -"
                if not schedule:
                    response["response"]["text"] += "Нет занятий"
                    response["response"]["tts"] += "Нет занятий"
                else:
                    for lesson in schedule:
                        aud = lesson['aud']
                        time = lesson['time']
                        response["response"]["text"] += "\n".join([
                            f"{lesson['number']} {time}",
                            f"{lesson['name']} {lesson['type']}",
                            f"Аудитория {aud}",
                            f"{', '.join(lesson['groups'])}",
                            "",
                            "",
                        ])

                        numerals = {
                            "1 пара": "Первая пара",
                            "2 пара": "Вторая пара",
                            "3 пара": "Третья пара",
                            "4 пара": "Четвертая пара",
                            "5 пара": "Пятая пара",
                            "6 пара": "Шестая пара",
                            "7 пара": "Седьмая пара",
                            "8 пара": "Восьмая пара",
                            "9 пара": "Девятая пара",
                        }

                        # Произношение
                        response["response"]["tts"] += " - - ".join([
                            f"{numerals[lesson['number']]} с {time.split('-')[0]} до {time.split('-')[1]}",
                            f"{lesson['type']}",
                            f"Корпус {aud.split('-')[0]} аудитория {aud.split('-')[1]}" if len(aud.split('-')) > 1 else f"{aud}",
                            "sil <[750]>",
                        ])
                    
                    response["response"]["tts"] += "sil <[1000]>"



    elif "помощь" in tokens:
        response["response"]["text"] = "\n".join([
            "Я могу показать расписание преподавателя или найти свободные окна для встречи нескольких преподавателей.",
            "Назовите дату и преподователя или нескольких преподавателей и я покажу свободные окна.",
            "Также вы можете узнать расписание преподавателя на конкретный день.",
        ])

    elif "пинг" in tokens:
        response["response"]["text"] = "Понг"
    
    elif "преподаватели" in tokens:
        response["response"]["text"] = "Преподователи:\n" + "\n".join([teacher['title'] for teacher in teachers])

    elif len(teachers_schedule) >= 1:
        windows = get_windows(teachers_schedule) # Окна в расписании

        if windows:
            ans = "Окна в расписании:\n\n"
            for s, e in windows:
                ans += f"с {s.strftime('%H:%M')} до {e.strftime('%H:%M')}\n"
            response["response"]["text"] = ans

        else:
            response["response"]["text"] = "Нет окон"

    else:
        if names_not_found:
            response["response"]["text"] = f"Не найдены преподаватели: {', '.join(names_not_found)}"
        else:
            response["response"]["text"] = "Не понятно"


    log.info("Response: %s", response)

    return response




def main(event, context):
    """Main function for Yandex.Cloud functions."""

    try:
        return process_event(event)
    except BaseException as err:
        print(err)
        print(traceback.format_exc())
    return {"statusCode": 200}

