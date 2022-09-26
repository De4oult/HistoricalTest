from telebot import types

import telebot

import configuration as conf # в файле configuration.py содержится текстовый контент и api-ключ приложения

app = telebot.TeleBot(conf.api_key) # инициализация бота по ключу из файла configuration.py


@app.message_handler(commands=["start"]) # прослушивание входящих сообщений
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    testApp = types.WebAppInfo("https://zxcoin.ru")
    todo_item = types.KeyboardButton(text = "Хочу пройти", web_app=testApp)
    about_item = types.KeyboardButton(text = "О тесте")
    markup.add(todo_item)
    markup.add(about_item)

    app.send_message(message.chat.id, conf.messages["welcome"], reply_markup = markup) # отправка приветствия при первом использовании

@app.message_handler(func = lambda message: True)
def keyboard_messages(message):
    if message.text.lower() == 'о тесте':
        app.send_message(message.chat.id, conf.messages["about"])

if __name__ == '__main__': # запуск бота
    app.infinity_polling()