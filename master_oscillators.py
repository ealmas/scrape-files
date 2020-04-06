import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from random import randint
import pandas as pd

pages = [str(i) for i in range(1,390)]

filename = "master_abr_oscillators.csv"
f = open(filename, "w", encoding="utf-8")
header = "name : lead_time : price\n"

for page in pages:

    urlpage = 'https://www.masterelectronics.com/products/oscillators-crystals/oscillators/mems-oscillators/?Manf=abracon&pagenum=' + page
    driver = webdriver.Chrome(executable_path =r"C:\Users\elif.issi\Desktop\chrome\chromedriver.exe")
    driver.get(urlpage)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    sleep(randint(30,50))

    name = driver.find_elements_by_xpath("//a[@class='product-title']")
    lead_time = driver.find_elements_by_xpath("//div[@class='product-data-row']")
    price = driver.find_elements_by_xpath("//div[@class='col product-pricing']")

    num_page_items = len(name)

    f.write(header)

    for i in range(num_page_items):
    	f.write(name[i].text + ":" + lead_time[i].text + ":" + price[i].text.replace('\n','/') + "\n")

    print(page)
    
f.close()