import telebot
import base64
import requests
import json
from wordpress import API

bot = telebot.TeleBot("***************************************************")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Бот запущен:)")

@bot.message_handler(commands=['newpost'])
def start(message):
    msg = bot.reply_to(message, "Введите пароль:")
    bot.register_next_step_handler(msg, start_2)

def start_2(message):
    bot.send_message(message.chat.id, "Введите сообщение", )
    if "**********" == message.text:
        @bot.message_handler(content_types=["text"])
        def send_message(message):

            bot.send_message(message.chat.id, "Отлично.")
            username = '*****'
            password = '**********'
            url = 'http://li79.ru/wp-json/wp/v2/posts/'

            credentials = username + ':' + password
            token = base64.b64encode(credentials.encode())
            headers = {'Authorization': 'Basic ' + token.decode('utf-8')}
            post = {
                'content': f'<marquee>{message.text}</marquee >',
            }

            r = requests.post(url + '2566', headers=headers, json=post)
            print(r)
    else:
        bot.reply_to(message, "Пароль неверный")
bot.polling()
