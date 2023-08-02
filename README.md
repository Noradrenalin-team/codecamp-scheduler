# **Проект "Планировщик"**

Добро пожаловать в репозиторий проекта "Планировщик"! Этот проект разработан в рамках хакатона и представляет собой сервис, позволяющий на основе расписания занятий университета находить временные интервалы для организации встреч преподавателей и студентов.

## Команда Noradrenalin-team​

- [Колядин Дмитрий](https://github.com/DeveloperDmitryKolyadin) - Team Lead, Backend
- [Шевлюк Василий](https://github.com/MrBallonvas) - Frontend

## Попробовать

- [Telegram бот](https://t.me/osu_scheduler_bot)
- [Web приложение](https://d5di6ilkmeiiui1ktjan.apigw.yandexcloud.net/)
- Чтобы получить доступ к навыку Алисы, напишите нам в [личку в телеграме](https://t.me/developerdk)
- [Исходный код](https://github.com/Noradrenalin-team/codecamp-scheduler)

## **Структура проекта**

```bash
├── .gitignore
├── README.md
│
├── docs/                  # Документация проекта
│   ├── infrastructure.md  # Инфраструктура
│   ├── repository_map.md  # Карта репозитория
│   └── technical_specification.md # Техническое задание
│   ├── bot/               # Документация по боту
│   │   ├── index.md       # Описание бота
│   │   └── to_begin.md    # С чего начать
│   └── frontend/          # Документация по фронтенду
│       ├── index.md       # Описание фронтенда
│       └── to_begin.md    # С чего начать
│
└── src/                   # Исходный код
    ├── Alice/             # Яндекс Алиса
    │   └── handler.py     # Обработчик сообщений
    ├── bot/               # Бот для Telegram
    │   ├── invoker.py     # Запуск бота
    │   └── bot/           # Обработчик сообщений
    │       └── handler.py
    └── tg_web_app/        # Web приложение

```

## **Документация**

1. **[Инфраструктура](docs/infrastructure.md)** - информация об инфраструктуре проекта и его компонентах.
2. **[Карта репозитория](docs/repository_map.md)** - описание структуры репозитория и размещение компонентов.
3. **[Техническое задание](docs/technical_specification.md)** - обзор технического задания на разработку проекта.

### **Компоненты проекта:**

- **[Документация по боту](docs/bot/index.md)** - описание бота и его функциональности.
- **[Документация по навыку для Яндекс Алисы](docs/Alice/index.md)** - описание бота и его функциональности.
- **[Документация по фронтенду](docs/frontend/index.md)** - описание веб-приложения и его интерфейса.

## **Краткое описание проекта**

"Планировщик" - это сервис, разработанный для университета, который помогает преподавателям и студентам находить свободные временные интервалы для организации встреч. Сервис анализирует расписание занятий и предлагает оптимальные временные слоты для встречи.

**Примечание**: В данном README.md представлены основные разделы, содержащие ссылки на страницы документации. Более подробные инструкции и описания могут быть представлены на соответствующих страницах документации.