import telebot
from telebot.types import Message

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def text(message):
    bot.reply_to(message, message.text.upper())
bot.polling()