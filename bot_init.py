import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.KeyboardButton(text="Перейти в гугл")
    keyboard.add(url_button)

bot.polling()