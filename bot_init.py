import telebot
from telebot import types

TOKEN = "838626620:AAEfM7W3LcrxruBicAYyGb8mWFUs0I4NwuQ"
bot = telebot.TeleBot(TOKEN)



markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
a = types.KeyboardButton('Мои Товары')
v = types.KeyboardButton('Поиск товара')
markup.add(a, v)

@bot.message_handler(commands= ["start"])
def start_bot(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    bot.send_message(chat_id, "Hi\nWelcom %s" % user_name, reply_markup = markup)

@bot.message_handler(regexp="Мои Товары")
def user_product(message):
    bot.reply_to(message, "fds")

@bot.message_handler(func=lambda message: True)
def text(message):
    bot.reply_to(message, message.text, reply_markup = markup)

bot.polling()
