# FullAndPointBot
 Телеграм-бот, поддерживающий переписку с авторами задач для олимпиады. Процесс состоит из нескольких шагов:
 
- Ввод авторов задачи
- Ввод условия задачи
- Подтверждение перед отправкой

## Команды
- `/start` - начать работу с ботом
- "Отправить задачу" - начать процесс отправки задачи

## Как использовать
1. Начните диалог с ботом командой `/start`
2. Нажмите кнопку "Отправить задачу"
3. Следуйте инструкциям бота

## Технические детали
- Бот написан на Python с использованием библиотеки `pyTelegramBotAPI`
- Поддерживает подтверждение/отмену перед отправкой
- Автоматически восстанавливает соединение при обрыве

Для работы бота необходимо задать `BOT_TOKEN` и `GROUP_ID` в коде.
