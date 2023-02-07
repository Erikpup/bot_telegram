import telebot
from confing import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет! Я эхо-бот, пересылающий слова от пользователя. Просто напиши мне что-нибудь!')


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
