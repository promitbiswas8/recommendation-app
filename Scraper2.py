import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.seattlecoffeegear.com/coffee-makers'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("li", {"class": "item"})
containers2 = page_soup.findAll("div", {"class": "price-box"})


filename = "CoffeeProducts.csv"
f = open(filename, "w")

headers = "item, price_of_item, image \n"

f.write(headers)

for i in range(len(containers)):
    item = containers[i].h2.a.text
    print("item: " + item)
    price_of_item = containers2[i].span.span.text
    print("price_of_item: " + price_of_item)
    itemImage = "hello"
    print("image: " + itemImage + "\n")
    f.write(item.replace("," ,"|") + "," + price_of_item + "," + itemImage + "\n")


f.close()
