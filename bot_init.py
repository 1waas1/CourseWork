import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)



markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)

