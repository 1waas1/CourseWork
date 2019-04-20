import telebot
import Token
from telebot import types

bot = telebot.TeleBot(Token.TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
a = types.KeyboardButton('Мои Товары')
v = types.KeyboardButton('Поиск товара')
markup.add(a, v)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
but1 = types.KeyboardButton('Телефоны')
but2 = types.KeyboardButton('Планшеты')
but3 = types.KeyboardButton('Телевизоры')
but4 = types.KeyboardButton('Ноутбуки')

markup1.add(but1, but2, but3, but4)


@bot.message_handler(commands= ["start"])
def start_bot(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    bot.send_message(chat_id, "Hi\nWelcom %s" % user_name, reply_markup = markup)

@bot.message_handler(regexp="Мои Товары")
def user_product(message):
    bot.reply_to(message, "fds")

@bot.message_handler(regexp="Поиск товара")
def user_product(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Категория", reply_markup = markup1)

@bot.message_handler(func=lambda message: True)
def text(message):
    bot.reply_to(message, message.text, reply_markup = markup)


bot.polling()
