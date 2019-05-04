import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    res = urllib.request.urlopen(url)
    return res.read()

def parse(html):
    soup = BeautifulSoup(html, "lxml")
    div_goods = soup.find("div", class_="g-i-tile-l").find("div", class_="g-i-tile-i-title")
    link = div_goods.a.get("href")
    parse_delivery(get_html(link + "delivery/"))
    return parse_goods(get_html(link), link)

def parse_goods(html, link):
    page = BeautifulSoup(html, "lxml")
    title = page.find("h1", class_="ng-star-inserted").text
    information = page.find("div", class_="short-description ng-star-inserted").text
    cost = page.find("span", class_="detail-price-uah").text.strip().replace("\u2009", " ")
    return "Rozetka", title, information, cost, link


def parse_delivery(html):
    soup = BeautifulSoup(html, "lxml")
    div_information = soup.find("h2")

def main_roz(url):
    #parse(get_html("https://rozetka.com.ua/search/?class=0&text=meizu&section_id=80003"))
    return parse(get_html(url))




# if __name__ == '__main__':
#     url = "https://rozetka.com.ua/search/?class=0&text=samsung+galaxy+tab&section_id=130309"
#     main(url)