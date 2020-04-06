import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(0,80)]

filename = "future_crystals.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; package; Load_Capacitance; operating_frequency; Frequency_Tolerance; Operating_Temp_Range; ESR; Insulation_Resistance; Drive_Level; Q_Value; Aging; Storage_Temperature_Range; Moisture_Sensitivity_Level; Dimension; No_Of_Pins;Mounting Feature\n"

for page in pages:

    my_url = 'https://www.futureelectronics.com/c/electromechanical/timing-devices--crystals/products?q=%3Arelevance&text=&pageSize=100&page=' + page
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
	    others = asc[2].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc21 = asc2[1].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc22 = asc2[2].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc23 = asc2[3].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc24 = asc2[4].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc25 = asc2[5].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc26 = asc2[6].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc27 = asc2[7].text.strip()
	    
	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc28 = asc2[8].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc29 = asc2[9].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc210 = asc2[10].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc211 = asc2[11].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc212 = asc2[12].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc213 = asc2[13].text.strip()

	    asc2 = container.find_all("td",{"class":"product_attr"})
	    asc214 = asc2[14].text.strip()

	    #asc2 = container.find_all("td",{"class":"product_attr"})
	    #asc215 = asc2[15].text.strip()

	    #asc2 = container.find_all("td",{"class":"product_attr"})
	    #asc216 = asc2[16].text.strip()
	    
	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + others + ";" + asc21 + ";" + asc22 + ";" + asc23 + ";" + asc24 + ";" + asc25 + ";" + asc26 + ";" + asc27 + ";" + asc28 + ";" + asc29 + ";" + asc210 + ";" + asc211 + ";" + asc212 + ";" + asc213 + ";" + asc214 + "\n")
    
    print(page)

f.close()
