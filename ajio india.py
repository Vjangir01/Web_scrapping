from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
url = "https://www.ajio.com/men-sports-shoes/c/830207008"
s = Service("V:/Softwares/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get(url)
time.sleep(2)
height = driver.execute_script("return document.body.scrollHeight")
# print(height)
while True:

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    new_height =driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height = new_height
