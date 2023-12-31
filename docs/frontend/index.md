# **Фронтенд "Планировщик"**

В данном разделе представлено описание фронтенда проекта "Планировщик". Фронтенд разработан с использованием фреймворка React и предоставляет пользовательский интерфейс для взаимодействия с расписанием преподавателей.

## **Описание файла `index.md`**

Фронтенд "Планировщик" представляет собой веб-приложение, которое позволяет пользователям быстро и удобно находить свободные временные интервалы для встреч с преподавателями университета.

### **Основные функции фронтенда:**

1. Поиск свободных временных окон:
    - Пользователь может указать дату и преподавателя(ей), для которых нужно найти свободные временные интервалы.
    - Фронтенд обращается к боту и навыку Яндекс Алисы для получения информации о расписании преподавателей и свободных временных окон.
2. Просмотр расписания преподавателя:
    - Пользователь может указать дату и имя преподавателя, чтобы просмотреть его расписание на заданный день.
3. Помощь и информация:
    - Фронтенд предоставляет подсказки по доступным командам и возможностям бота и навыка Яндекс Алисы.
    - Пользователь может получить список доступных преподавателей.

### **Развертывание и использование**

Фронтенд разрабатывается с использованием React и собирается в билд, который загружается в Object Storage. После этого фронтенд доступен для пользователей через веб-браузер.

## **Дальнейшее развитие**

В дальнейшем разработка фронтенда может быть дополнена следующими возможностями:

- Расширение функциональности для более удобного поиска и просмотра расписания.
- Добавление авторизации и персонализированных настроек для пользователей.
- Улучшение дизайна и интерфейса для более приятного взаимодействия с пользователем.

Примечание: Фронтенд разрабатывается параллельно с ботом и навыком Яндекс Алисы, и его функциональность должна быть согласована с обработчиками запросов в обоих сервисах.


## **Планируемая интеграция с Telegram Web App**

1. **Просмотр тем занятий**: Пользователи смогут запросить информацию о темах, которые будут рассматриваться на занятиях, чтобы более точно планировать встречи и подготовку.
2. **Подробное расписание**: При поиске свободных временных окон пользователи смогут получить более подробное расписание занятий, включая описание предмета, название аудитории и другие дополнительные детали.
3. **Уведомления о расписании**: Возможность настройки уведомлений для определенных преподавателей или групп студентов о предстоящих занятиях и встречах.
4. **Интеграция с календарем**: Пользователи смогут добавлять встречи и занятия в свой календарь напрямую из Telegram Web App, чтобы легко отслеживать своё расписание.
5. **Команды через интерфейс бота**: Добавление удобного интерфейса для выполнения различных команд, доступных в боте, с помощью кнопок и элементов интерфейса.
6. **Поддержка групповых встреч**: Расширение возможностей поиска свободных временных интервалов для групповых встреч или консультаций с несколькими преподавателями одновременно.

## **Преимущества глубокой интеграции**

- **Удобство и быстрота**: Благодаря интеграции с Telegram Web App пользователи смогут получать информацию и планировать встречи прямо из приложения, которое они уже используют ежедневно.
- **Более полная информация**: Пользователи смогут получать дополнительные данные о занятиях, что поможет им более точно ориентироваться в расписании.
- **Легкость в использовании**: Для использования функциональности бота не нужно переключаться между разными приложениями - всё доступно в одном месте.
- **Больше возможностей**: Глубокая интеграция позволит расширить функциональность проекта и предоставить пользователям новые интересные возможности.

## **План разработки**

1. **Анализ потребностей пользователей**: Проведение опросов и исследования, чтобы определить наиболее востребованные функции среди пользователей.
2. **Дизайн интерфейса**: Разработка удобного и интуитивно понятного интерфейса для Telegram Web App с учетом добавляемых функций.
3. **Интеграция с ботом и навыком Яндекс Алисы**: Разработка API и логики взаимодействия между фронтендом и бэкендом проекта.
4. **Тестирование и оптимизация**: Проведение тестирования, выявление и устранение ошибок, оптимизация производительности.
5. **Запуск и отслеживание**: Развертывание проекта с обновленной функциональностью и мониторинг его работы.
6. **Обратная связь и улучшения**: Сбор обратной связи от пользователей, учет их мнения и предложений для дальнейшего улучшения проекта.

Благодаря глубокой интеграции с Telegram Web App, "Планировщик" станет ещё более удобным и многофункциональным инструментом для планирования встреч и управления расписанием. Успехов в разработке и расширении функциональности проекта!