import os

import requests
import telebot
from confing import *
from flask import Flask,request

bot = telebot.TeleBot(BOT_TELEGRAM)
server = Flask(__name__)

@bot.message_handler(commands=["start"])
def start(m):
    username = m.from_user.username
    bot.reply_to(m, f'Hello, {username}')

@server.route(f'/{BOT_TELEGRAM}',methods={'POST'})
def redirect_message():
    json_str = request.get_data().decode('utf-8')
    update=telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!',200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))
