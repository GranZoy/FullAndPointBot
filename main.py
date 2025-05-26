from telebot import TeleBot, types
import time

BOT_TOKEN = ""
GROUP_ID = ""

user_data = {}

bot = TeleBot(BOT_TOKEN)


def GetKeyBoard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Отправить задачу"))
    return keyboard


@bot.message_handler(commands=['start'])
def StartCommand(message):
    bot.send_message(message.chat.id, "Привет!", reply_markup=GetKeyBoard())


@bot.message_handler(func=lambda message: message.text == "Отправить задачу")
def AskAuthors(message):
    user_data[message.chat.id] = {}
    bot.send_message(message.chat.id, "Введите имена авторов:", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'authors' not in user_data[message.chat.id])
def AskTaskDescription(message):
    user_data[message.chat.id]['authors'] = message.text
    bot.send_message(message.chat.id, "Введите условие задачи:")


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'task' not in user_data[message.chat.id])
def ConfirmTask(message):
    user_data[message.chat.id]['task'] = message.text
    authors = user_data[message.chat.id]['authors']
    task = user_data[message.chat.id]['task']

    text = f"Пожалуйста, подтвердите отправку:\n\nАвторы: {authors}\nУсловие: {task}"

    confirm_keyboard = types.InlineKeyboardMarkup()
    confirm_keyboard.add(types.InlineKeyboardButton("✅ Подтвердить", callback_data="confirm_task"))
    confirm_keyboard.add(types.InlineKeyboardButton("❌ Отменить", callback_data="cancel_task"))

    bot.send_message(message.chat.id, text, reply_markup=confirm_keyboard, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == "confirm_task")
def SendTask(call):
    chat_id = call.message.chat.id
    authors = user_data[chat_id]['authors']
    task = user_data[chat_id]['task']

    text = f"Авторы: {authors}\nУсловие: {task}"
    bot.send_message(GROUP_ID, text, parse_mode="Markdown")

    bot.edit_message_reply_markup(chat_id, call.message.message_id)
    bot.send_message(chat_id, "✅ Задача успешно отправлена!", reply_markup=GetKeyBoard())
    del user_data[chat_id]


@bot.callback_query_handler(func=lambda call: call.data == "cancel_task")
def CancelTask(call):
    chat_id = call.message.chat.id
    bot.edit_message_reply_markup(chat_id, call.message.message_id)
    bot.send_message(chat_id, "❌ Отправка задачи отменена.", reply_markup=GetKeyBoard())
    del user_data[chat_id]


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        time.sleep(5)
