"""
This module contains handlers for bot commands and messages.
"""

import json
import logging
import os
import traceback

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Logger initialization and logging level setting
log = logging.getLogger(__name__)
log.setLevel(os.environ.get("LOGGING_LEVEL", "INFO").upper())

bot = Bot(os.environ.get("TOKEN"))
dp = Dispatcher()


# Handlers
@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту."""

    answer_md = "\n".join(
        [
            "Добро пожаловать в *Планировщик*!\n",
            "Я бот, который поможет вам находить свободные временные интервалы для организации встреч с преподавателями или группами студентов университета.\n",
            'Вы можете воспользоватся кнопкой "Открыть расписание", чтобы открыть веб-приложение с расписанием.',
            "Если у вас есть вопросы или нужна помощь, просто введите /help, и я предоставлю список доступных команд.\n",
            "Приятного использования!",
        ]
    )

    # Кнопка запуска web app
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть расписание", web_app = types.WebAppInfo(url="https://d5di6ilkmeiiui1ktjan.apigw.yandexcloud.net/app")
                )
            ],
        ]
    )


    await message.reply(answer_md, parse_mode="Markdown", reply_markup=keyboard)

@dp.message(Command(commands=["help"]))
async def send_help(message: types.Message):
    """Отправляет сообщение с описанием команд."""

    answer_md = "\n".join(
        [
            "*Список команд:*\n",
            "/start - запуск бота",
            "/help - список команд",
            "/schedule - расписание",
        ]
    )

    await message.reply(answer_md, parse_mode="Markdown")


@dp.message(Command(commands=["schedule"]))
async def send_schedule(message: types.Message):
    """Отправляет сообщение с расписанием."""

    answer_md = "\n".join(
        [
            "*Расписание:*\n",
        ]
    )

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть расписание", web_app = types.WebAppInfo(url="https://d5di6ilkmeiiui1ktjan.apigw.yandexcloud.net/app")
                )
            ],
        ]
    )

    await message.reply(answer_md, parse_mode="Markdown", reply_markup=keyboard)

@dp.message(Command(commands=["schedule_dev"]))
async def send_schedule_dev(message: types.Message):
    """Отправляет сообщение с расписанием."""

    answer_md = "\n".join(
        [
            "*Расписание:*\n",
        ]
    )

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть расписание (л)",  web_app = types.WebAppInfo(url="https://0.0.0.0:3000")
                )
            ],
        ]
    )

    await message.reply(answer_md, parse_mode="Markdown", reply_markup=keyboard)



async def process_event(event, bot: Bot, dp: Dispatcher):
    """
    Converting an Yandex.Cloud functions event to an update and
    handling tha update.
    """

    update = json.loads(event["body"])

    print("Update:")
    print(update)

    await dp.feed_raw_update(bot, update)


async def main(event, context):
    """Main function for Yandex.Cloud functions."""

    try:
        await process_event(event, bot, dp)

    except BaseException as err:
        print(err)
        print(traceback.format_exc())
    return {"statusCode": 200}

