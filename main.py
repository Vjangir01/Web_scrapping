import requests

from bs4 import BeautifulSoup

urls = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
r = requests.get(urls)
#print(r)

soup = BeautifulSoup(r.text,"lxml")
#print(soup)

# boxes = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))
# Ctrl+/ for multi line code command
# name  = soup.find_all("a",class_ = "title")
# for i in name:
#     print(i.text)

price = soup.find_all("h4",class_ = "price float-end card-title pull-right")
for i in price:
    print(i.text)
#print(price)
