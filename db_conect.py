import pymysql.cursors
class DbConector(object):
    def __init__(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='YAROSLAW1999',
                                     db='tg_bot',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)



