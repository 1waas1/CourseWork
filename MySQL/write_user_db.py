import pymysql.cursors
from configparser import ConfigParser

config = ConfigParser()
config.read('../config.ini')

config_name = 'database'

connection = pymysql.connect(host=config.get(config_name, 'host'),
                             user=config.get(config_name, 'user'),
                             password=config.get(config_name, 'password'),
                             db=config.get(config_name, 'db_name'),
                             charset=config.get(config_name, 'charset'),
                             cursorclass=pymysql.cursors.DictCursor)


class WriteDb(object):
    def __init__(self, tg_id_user, name, username):
        self.tg_id_user = tg_id_user
        self.name = name
        self.username = username
        WriteDb.check_tg_id(self)

    def check_tg_id(self):
        select_id = "Select id From user where tg_user_id = %s"
        cursor = connection.cursor()
        cursor.execute(select_id, self.tg_id_user)
        if len(cursor.fetchall()) > 0:
            WriteDb.return_id(self.tg_id_user)
        else:
            WriteDb.registration_db(self)

    def return_id(self, telegram_id):
        select_id = "Select id From user where tg_user_id = %s"
        cursor = connection.cursor()
        cursor.execute(select_id, telegram_id)
        user_id = cursor.fetchall()[0]["id"]
        return user_id

    def registration_db(self):
        add_user = "INSERT INTO user (tg_user_id, name, tg_name) VALUES (%s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(add_user, (self.tg_id_user, self.name, self.username))
        connection.commit()
        connection.close()
        #WriteDb.return_id(self.tg_id_user)

class WriteGoods(WriteDb):
    def write_name_goods(self, name_category, brand, model):
        name_goods_sql = "INSERT INTO name_goods (id_category, brand, model) VALUES (%s, %s, %s)"
        cursor = connection.cursor()
        id_category = WriteGoods.id_category(self, name_category)
        cursor.execute(name_goods_sql, (id_category, brand, model))
        connection.commit()
        connection.close()
        # дізнатися і повернути id товару який тільки що був записаний
    def write_date(self, id_user, id_name_goods):
        date_sql = "INSERT INTO date (id_user, id_name_goods, date) VALUES (%s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(date_sql, (id_user, id_name_goods, data))#запись даты
        connection.commit()
        connection.close()
    def write_category(self, name_category):
        category_sql = "INSERT INTO category (id_category) VALUES %s"
        cursor = connection.cursor()
        id_category = WriteGoods.id_category(self, name_category)
        cursor.execute(category_sql, id_category)
        connection.commit()
        connection.close()

    def write_goods(self, score, name, description, cost, link):
        category_sql = "INSERT INTO goods (id_name_goods, id_cost, id_score, name, description, link) " \
                       "VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = connection.cursor()
        id_category = WriteGoods.id_category(self, name_category)
        cursor.execute(category_sql, id_category)
        connection.commit()
        connection.close()


    def id_score(self, score):
        id_score_arr = {
            "Rozetka": 1,
            "Citrus": 2
        }
        return id_score_arr[score]
    def id_category(self, category):
        id_category_arr = {
            "Телефони": 1,
            "Планшети":2,
            "Телевізори":3,
            "Ноутбуки":4
        }
        return id_category_arr[category]





# class SearchGoods(WriteDb):
#     def __init__(self, tg_id_user ,category, name_goods):
#         self.category = category
#         self.name_goods = name_goods
#         super().__init__(self, tg_id_user)
#     def formulation_url_rozetka(self, name_goods, category):
#         self.name_goods = name_goods
#         #https://rozetka.com.ua/search/?class=0&text=xiaomi&section_id=80003 пример
#         url = "https://rozetka.com.ua/search/?class=0&text="
#         category_roz = [{"Телефони": "80003",
#                          "Планшети": "130309",
#                          "Телевізори": "80037",
#                          "Ноутбуки": "80004"
#                          }]
#         true_name_goods = self.name_goods.replace(" ", "+")
#         url += true_name_goods + "&section_id=" + category_roz[self.category]
#         return url
#     def formulation_url_citrus(self):
#         url = "https://www.citrus.ua/search?query="
#         category_cit = [{"Телефони": "20",
#                          "Планшети": "63",
#                          "Телевізори": "139",
#                          "Ноутбуки": "96"
#                          }]
#         true_name_goods = self.name_goods.replace(" ", "%20")
#         url += true_name_goods + "&categories=" + category_cit[self.category]
#         return url




