import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    res = urllib.request.urlopen(url)
    return res.read()

def parse(html):
    page = BeautifulSoup(html, "lxml")
    first_goods = page.find("ul", id="hs-below-list-items")
    #link = first_goods.find("li", class_="list-item-first").find("h3", class_="icon-hotproduct").a.get("href")

    list = [{
        "link": page
    }]
    print(list)



def main(url):
    #parse(get_html("https://rozetka.com.ua/search/?class=0&text=meizu&section_id=80003"))
    parse(get_html(url))



if __name__ == '__main__':
    url = "https://ru.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190430121420&SearchText=samsung+galaxy"
    main(url)