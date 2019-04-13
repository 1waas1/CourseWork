import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)




keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
url_button = types.KeyboardButton(text="Перейти в гугл")
keyboard.add(url_button)

bot.polling()