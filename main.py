#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import confing
bot = telebot.TeleBot(confing.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, давай поговорим")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'привет' in str(message.text).lower():
        bot.reply_to(message, "Привет, я пишу тебе из облака")
    else:
        bot.reply_to(message, f"Создатель меня еще не научил отвечать на '{message.text}'")

bot.polling()
