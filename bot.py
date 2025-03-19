import telebot
import os

TOKEN = os.getenv('27445897')
bot = telebot.TeleBot(7820036140:AAFSq7KPDPCWD2Yqjo2MJC_9gruV4zfNLLw)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Bot kamu sudah aktif 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
 
