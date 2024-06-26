import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Price = []
Description = []
Review = []

for i in range(2, 4):
    url = 'https://www.flipkart.com/search?q=mobiles+under+40000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_7_10_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_7_10_na_na_na&as-pos=7&as-type=RECENT&suggestionId=mobiles+under+40000&requestId=e21bd759-e41e-4746-be29-6097da78443e&as-searchtext=mobiles+under+40000&page=' + str(i)
    r = requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find("div", class_="DOjaWF YJG4Cf")
    names = box.find_all("div", class_="KzDlHZ")
    #print(names)
    for i in names:
        names = i.text
        Product_name.append(names)
    #print(Product_name)
    price = box.find_all('div', class_ = "Nx9bqj _4b5DiR")
    for i in price:
        name = i.text
        Price.append(name)
    #print(Price)
    desc = box.find_all("ul", class_="G4BRas")
    for i in desc:
        name = i.text
        Description.append(name)
    #print(Description)
    reviews = box.find_all("div", class_="XQDdHH")
    for i in reviews:
        name = i.text
        Review.append(name)
    #print(Review)

df = pd.DataFrame({"Product_name":Product_name,"Price":Price,"reviews":Review,"Description":Description,})
# print(df)
# print("Length of Product_name:", len(Product_name))
# print("Length of Price:", len(Price))
# print("Length of Description:", len(Description))
# print("Length of Review:", len(Review))





df.to_csv("Flipkart_mobile_under_40000.csv")

    # print(soup)
    #while True:
    # np = soup.find("a", class_="_9QVEpD").get("href")
    # cnp = "https://www.flipkart.com" + np
    # print(cnp)


# url = cnp
# r = requests.get(url)
# soup = BeautifulSoup(r.text,"lxml")
