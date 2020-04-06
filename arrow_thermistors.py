import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,64)]

filename = "arrow_thermistors.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_type; number_of_terminals; thermal_coefficient; thermal_time_constant; sensitivity_index_range; accuracy; operating_temperature; resistance_25C; percentage_of_resistance; package_case; packaging; dose_level; rad_hard; military; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page=' + page + '&prodline=Thermistors&selectedType=plNames&perPage=100'
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

	    asc20 = container.find_all("td",{"data-column":"feature-type"})
	    try:
	    	product_type = asc20[0].text.strip()
	    except IndexError:
	    	product_type = 'null'

	    asc21 = container.find_all("td",{"data-column":"feature-number-of-terminals"})
	    try:
	    	number_of_terminals = asc21[0].text.strip()
	    except IndexError:
	    	number_of_terminals = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-thermal-coefficient-range"})
	    try:
	    	thermal_coefficient = asc22[0].text.strip()
	    except IndexError:
	    	thermal_coefficient = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-thermal-time-constant-range-s"})
	    try:
	    	thermal_time_constant = asc23[0].text.strip()
	    except IndexError:
	    	thermal_time_constant = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-sensitivity-index-range-k"})
	    try:
	    	sensitivity_index_range = asc235[0].text.strip()
	    except IndexError:
	    	sensitivity_index_range = 'null'

	    asc24 = container.find_all("td",{"data-column":"feature-accuracy"})
	    try:
	    	accuracy = asc24[0].text.strip()
	    except IndexError:
	    	accuracy = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc25[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc26 = container.find_all("td",{"data-column":"feature-resistance-25c-ohm"})
	    try:
	    	resistance_25C = asc26[0].text.strip()
	    except IndexError:
	    	resistance_25C = 'null'

	    asc27 = container.find_all("td",{"data-column":"feature-percentage-of-resistance-tolerance-range-25c-"})
	    try:
	    	percentage_of_resistance = asc27[0].text.strip()
	    except IndexError:
	    	percentage_of_resistance = 'null'

	    asc310 = container.find_all("td",{"data-column":"feature-package-case"})
	    try:
	    	package_case = asc310[0].text.strip()
	    except IndexError:
	    	package_case = 'null'

	    asc31 = container.find_all("td",{"data-column":"feature-packaging"})
	    try:
	    	packaging = asc31[0].text.strip()
	    except IndexError:
	    	packaging = 'null'

	    asc32 = container.find_all("td",{"data-column":"feature-dose-level-krad"})
	    try:
	    	dose_level = asc32[0].text.strip()
	    except IndexError:
	    	dose_level = 'null'

	    asc33 = container.find_all("td",{"data-column":"feature-rad-hard"})
	    try:
	    	rad_hard = asc33[0].text.strip()
	    except IndexError:
	    	rad_hard = 'null'

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

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_type + ";" + number_of_terminals + ";" + thermal_coefficient + ";" + thermal_time_constant + ";" + sensitivity_index_range + ";" + accuracy + ";" + operating_temperature + ";" + resistance_25C + ";" + percentage_of_resistance + ";" + package_case + ";" + packaging + ";" + dose_level + ";" + rad_hard + ";" + military + ";" +  automotive + "\n")
    
    print(page)

f.close()