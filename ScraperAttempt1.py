import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.patagonia.com/shop/mens-fleece?start=0&sz=24#tile-1'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class": "product-name"})

filename = "Showproducts.csv"
f = open(filename, "w")

headers = "item, price_of_item, image \n"

f.write(headers)

for i in range(len(containers)):
    item = containers[i].a.text
    print("item: " + item)
    containers2 = page_soup.findAll("div", {"class": "product-price mobile"})
    price_of_item = containers2[i].span.text
    print("price_of_item: " + price_of_item)
    itemImage = "hello"
    print("image: " + itemImage + "\n")
    f.write(item.replace("," ,"|") + "," + price_of_item + "," + itemImage + "\n")


f.close()
