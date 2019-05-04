import telebot
import Token
from telebot import types
import MySQL.write_user_db as DB
import form_url
import scrap.scrap_rozetka
import scrap.scrap_citrus

bot = telebot.TeleBot(Token.TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
a = types.KeyboardButton('Мої Товари')
v = types.KeyboardButton('Пошук')
markup.add(a, v)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
but1 = types.KeyboardButton('Телефони')
but2 = types.KeyboardButton('Планшети')
but3 = types.KeyboardButton('Телевізори')
but4 = types.KeyboardButton('Ноутбуки')

markup1.add(but1, but2, but3, but4)


@bot.message_handler(commands= ["start"])
def start_bot(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name + " " + message.from_user.last_name
    user_name = message.from_user.username

    bot.send_message(chat_id, "Hi\nWelcom %s" % name, reply_markup = markup)
    DB.WriteDb(user_id, name, user_name)


@bot.message_handler(regexp="Мої Товари")
def user_product(message):
    bot.reply_to(message, "fds")

@bot.message_handler(regexp="Пошук")
def user_product(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Каталог товарів", reply_markup = markup1)

@bot.message_handler(regexp="Телефони")
def phone(message):
    phone_search()
    bot.send_message(message.from_user.id, message)
def phone_search():
    rezult_roz = scrap.scrap_rozetka.main_roz(form_url.formulation_url_rozetka("meizu x8", "Телефони"))
    rezult_cit = scrap.scrap_citrus.main_cit(form_url.formulation_url_citrus("meizu x8", "Телефони"))
    return_phone(rezult_roz, rezult_cit)
def return_phone(roz, cit):
    score_info(roz[0], roz[1], roz[2], roz[3], roz[4])
    score_info(cit[0], cit[1], cit[2], cit[3], cit[4])


def score_info(score, name, information, cost, link):
    print("finish")
    info_goods = "Магазин: %s\nНазва: %s\nІнформація: %s\nЦіна: %s\nПосилання: %s" \
                 %(score, name, information, cost, link)
    print(info_goods)
# def send_info(message,text):
#     print("5")
#     bot.send_message(message. ,text)


@bot.message_handler(func=lambda message: True)
def text(message):
    bot.reply_to(message, message.text, reply_markup = markup)
    user_id = message.from_user.id
    print(message)
    # user_id = message.json.id


bot.polling()
