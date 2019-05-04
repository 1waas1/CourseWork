import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='YAROSLAW1999',
                             db='tg_bot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class WriteDb(object):
    def __init__(self, tg_id_user, name, username):
        self.tg_id_user = tg_id_user
        self.name = name
        self.username = username
        WriteDb.check_tg_id(self)

    def check_tg_id(self):
        sql = "Select id From user where tg_user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, self.tg_id_user)
        if len(cursor.fetchall()) > 0:
            cursor.execute(sql, self.tg_id_user)
            user_id = cursor.fetchall()[0]["id"]
            WriteDb.id_user(user_id)
        else: WriteDb.registration_db(self)

    def id_user(self, user_id):
        return user_id

    def registration_db(self):
        sql = "INSERT INTO user (tg_user_id, name, tg_name) VALUES (%s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, (self.tg_id_user, self.name, self.username))
        connection.commit()
        connection.close()

class MyGoods(object):
    def __init__(self):
        pass
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




