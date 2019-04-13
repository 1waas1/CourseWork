import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)



markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
a = types.KeyboardButton('a')
v = types.KeyboardButton('v')
markup.add(a, v)

@bot.message_handler(func=lambda message: True)
def text(message):
    bot.reply_to(message, message.text, reply_markup = markup)
bot.polling()
