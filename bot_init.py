import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)




keyboard = types.ReplyKeyboardMarkup(row_width=2)
url_button = types.KeyboardButton("Перейти в гугл")
keyboard.add(url_button)

bot.polling()