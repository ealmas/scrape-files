import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,11)]

filename = "arrow_connector_fiber_optics.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_category; typee; gender; mode; termination_method; body_orientation; cable_diameter; fiber_cable_type; insertion_loss; operating_temperature; packaging; military; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page=' + page + '&prodline=Connector%20Fiber%20Optics&selectedType=plNames&perPage=100'
    user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)'
    headers = {'User-Agent': user_agent}

    #opening up connection' grabbing the page
    #uClient = uReq.(my_url, headers=headers)
    uClient = requests.get(my_url, headers=headers)
    page_html = uClient.content
    uClient.close()

    sleep(randint(30,50))

    #html parsing
    page_soup = soup(page_html, "html.parser")
    table_body = page_soup.find("tbody")
    containers = table_body.find_all("tr")

    f.write(header)

    for container in containers:

	    mfr_prt = container.find_all("span",{"class":"SearchResults-productName"})
	    try:
	    	manufacturer_part = mfr_prt[0].text.strip()
	    except IndexError:
	    	manufacturer_part = 'null'

	    mfr = container.find_all("a",{"class":"SearchResults-productManufacturer"})
	    try:
	    	manufacturer = mfr[0].text.strip()
	    except IndexError:
	    	manufacturer = 'null'

	    dsc = container.find_all("span",{"class":"SearchResults-productName--description"})
	    try:
	    	description = dsc[0].text.strip()
	    except IndexError:
	    	description = 'null'

	    prc = container.find_all("div",{"class":"SearchResults-priceTiers"})
	    try:
	    	pricing = prc[0].text.replace('\n', ' ').strip()
	    except IndexError:
	    	pricing = 'null'

	    avb = container.find_all("span",{"class":"SearchResults-stock"})
	    try:
	    	availability = avb[0].text.split()[1]
	    except IndexError:
	    	availability = 'null'

	    asc20 = container.find_all("td",{"data-column":"type"})
	    try:
	    	product_type = asc20[0].text.strip()
	    except IndexError:
	    	product_type = 'null'

	    asc21 = container.find_all("td",{"data-column":"feature-type"})
	    try:
	    	typee = asc21[0].text.strip()
	    except IndexError:
	    	typee = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-gender"})
	    try:
	    	gender = asc22[0].text.strip()
	    except IndexError:
	    	gender = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-mode"})
	    try:
	    	mode = asc23[0].text.strip()
	    except IndexError:
	    	mode = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-termination-method"})
	    try:
	    	termination_method = asc235[0].text.strip()
	    except IndexError:
	    	termination_method = 'null'

	    asc24 = container.find_all("td",{"data-column":"feature-body-orientation"})
	    try:
	    	body_orientation = asc24[0].text.strip()
	    except IndexError:
	    	body_orientation = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-cable-diameter-mm"})
	    try:
	    	cable_diameter = asc25[0].text.strip()
	    except IndexError:
	    	cable_diameter = 'null'

	    asc26 = container.find_all("td",{"data-column":"feature-fiber-cable-type"})
	    try:
	    	fiber_cable_type = asc26[0].text.strip()
	    except IndexError:
	    	fiber_cable_type = 'null'

	    asc27 = container.find_all("td",{"data-column":"feature-insertion-loss-db"})
	    try:
	    	insertion_loss = asc27[0].text.strip()
	    except IndexError:
	    	insertion_loss = 'null'

	    asc34 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc34[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc36 = container.find_all("td",{"data-column":"feature-packaging"})
	    try:
	    	packaging = asc36[0].text.strip()
	    except IndexError:
	    	packaging = 'null'

	    asc41 = container.find_all("td",{"data-column":"feature-military"})
	    try:
	    	military = asc41[0].text.strip()
	    except IndexError:
	    	military = 'null'

	    asc42 = container.find_all("td",{"data-column":"feature-automotive"})
	    try:
	    	automotive = asc42[0].text.strip()
	    except IndexError:
	    	automotive = 'null'

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_type + ";" + typee + ";" + gender + ";" + mode + ";" + termination_method + ";" + body_orientation + ";" + cable_diameter + ";" + fiber_cable_type + ";" + insertion_loss + ";" + operating_temperature + ";" + packaging + ";" + military + ";" + automotive + "\n")
    
    print(page)

f.close()