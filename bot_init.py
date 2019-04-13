import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)



markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')

markup.add(itembtna, itembtnv)

