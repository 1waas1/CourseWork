import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    res = urllib.request.urlopen(url)
    return res.read()

def parse_link(html):
    soup = BeautifulSoup(html, "lxml")
    goods_block = soup.find("div", class_="product-card").find("a", class_="card-product-link")
    goods_link = "https://www.citrus.ua" + goods_block.get("href")
    goods_name = goods_block.get("title")
    return parse_goods(get_html(goods_link), goods_link)

def parse_goods(html, link):
    soup = BeautifulSoup(html, "lxml")
    price = soup.find("div", id="buy-block").find("div", class_="buy-block__base")\
        .find("div", class_="normal__prices").find_all("div", class_="price")
    name = soup.find("h1", class_="product__title").text
    goods_rating = soup.find("header", class_="product__header").find("div", class_="product__rating")
    warranty = soup.find("div", class_="showcase__body").find("div", class_="warranty").text.split(",")
    info = soup.find("div", class_="showcase__characteristics").find_all("div", class_="item__description")
    arr_info = ""
    for item in info:
        arr_info += item.text
    #count_rating(goods_rating)
    return "Citrus", name, arr_info, price[1].text, link


def count_rating(block_ratin):
    rating = block_ratin.find("div", class_="el-rate")
    item_rate = rating.find_all("span", class_="el-rate__item")
    count_user = block_ratin.find("div", class_="rate__amount").text.strip()
    # print(count_user)
    # for i in range(0, 5, 1):
    #     atribut_style = item_rate[i].i.get("style")
    #     print(atribut_style)
    #доробити лічильник рейтингу


def main_cit(url):
    #parse(get_html("https://rozetka.com.ua/search/?class=0&text=meizu&section_id=80003"))
    return parse_link(get_html(url))



# if __name__ == '__main__':
#     url = "https://www.citrus.ua/search?query=Meizu&categories=20"
#     main(url)