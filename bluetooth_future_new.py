import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(0,4)]

filename = "future_bluetooth.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; Lead_Time; Package\n"

for page in pages:

    my_url = 'https://www.futureelectronics.com/search/?q=BLUETOOTH:relevance&selectedTab=products&text=BLUETOOTH&pageSize=100&page=' + page
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}

    #opening up connection' grabbing the page
    #uClient = uReq.(my_url, headers=headers)
    uClient = requests.get(my_url,headers=headers)
    page_html = uClient.content
    uClient.close()

    sleep(randint(30,50))

    #html parsing
    page_soup = soup(page_html, "html.parser")
    table_body = page_soup.find("table")
    containers = table_body.find_all("tr",{"class":"list-row"})

    f.write(header)

    for container in containers:

	    mfr_prt = container.find_all("a",{"class":"product__list--code"})
	    try:
	    	manufacturer_part = mfr_prt[0].text.strip()
	    except IndexError:
	    	manufacturer_part = 'null'

	    mfr = container.find_all("div",{"class":"product__list--name"})
	    try:
	    	manufacturer = mfr[0].text.strip()
	    except IndexError:
	    	manufacturer = 'null'

	    dsc = container.find_all("div",{"class":"product__list--description"})
	    try:
	    	description = dsc[0].text.replace(';',' ').strip()
	    except IndexError:
	    	description = 'null'

	    prc = container.find_all("td",{"class":"product_price"})
	    try:
	    	pricing = prc[0].text.strip()
	    except IndexError:
	    	pricing = 'null'

	    avb = container.find_all("td",{"class":"product_stock"})
	    try:
	    	availability = avb[0].text.strip()
	    except IndexError:
	    	availability = 'null'

	    asc = container.find_all("td",{"class":"product_pkg"})
	    others = asc[0].text.strip()

	    asc = container.find_all("td",{"class":"product_pkg"})
	    others2 = asc[2].text.strip()
	    
	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + others + ";" + others2 + "\n")
    
    print(page)

f.close()
