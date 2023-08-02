# **Карта репозитория**

```bash
│   .gitignore
│   README.md
│
├───.vscode # Настройки VSCode
│       extensions.json
│       keybindings.json
│       launch.json
│       settings.json
│       tasks.json
│
├───docs # Документация
│   │   infrastructure.md # Инфраструктура
│   │   repository_map.md # Карта репозитория
│   │   technical_specification.md # Техническое задание
│   │
│   ├───bot
│   │       index.md # Описание бота
│   │       to_begin.md # С чего начать
│   │
│   └───frontend
│           index.md # Описание фронтенда
│           to_begin.md # С чего начать
│
└───src # Исходный код
    ├───Alice # Яндекс Алиса
    │       handler.py # Обработчик сообщений
    │
    ├───bot # Бот для Telegram
    │   │   invoker.py # Запуск бота
    │   │
    │   ├───bot
    │   │   │   handler.py # Обработчик сообщений
    │   │   └───__init__.py
    │   │
    │   └───bot_tools # Инструменты для бота
    │
    └───tg_web_app # Web приложение
```