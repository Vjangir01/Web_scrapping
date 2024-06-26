from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

path ="V:/Softwares/chromedriver-win64/chromedriver-win64/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")

box= driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("House of dragon")
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div/div/div[1]/div/div/span/a""").click()

driver.save_screenshot("C:/Users/jangi/OneDrive/Desktop/Web_scraping_P/dragon.png")
