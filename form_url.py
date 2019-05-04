def formulation_url_rozetka(name_goods, category):
    # https://rozetka.com.ua/search/?class=0&text=xiaomi&section_id=80003 пример
    url = "https://rozetka.com.ua/search/?class=0&text="
    category_roz = {"Телефони": 80003,
                     "Планшети": 130309,
                     "Телевізори": 80037,
                     "Ноутбуки": 80004
                     }
    true_name_goods = name_goods.replace(" ", "+")
    url += str(true_name_goods) + "&section_id=" + str(category_roz[category]) + "&view=tile"
    return url

def formulation_url_citrus(name_goods, category):
    url = "https://www.citrus.ua/search?query="
    category_cit = {"Телефони": "20",
                     "Планшети": "63",
                     "Телевізори": "139",
                     "Ноутбуки": "96"
                     }
    true_name_goods = name_goods.replace(" ", "%20")
    url += true_name_goods + "&categories=" + category_cit[category]
    return url