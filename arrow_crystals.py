import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,308)]

filename = "arrow_crystals.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_category; standard_frequency; frequency_tolerance; frequency_stability; load_capacitance; series_resistance; mode_of_oscillation; operating_temperature; packaging; pin_count; supplier_package; standard_package_name; military; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page='+ page + '&prodline=Crystals&selectedType=plNames&sortBy=calculatedQuantity&sortDirection=desc&perPage=100'
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
	    	description = dsc[0].text.replace(';', ' ').strip()
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
	    	product_category = asc20[0].text.strip()
	    except IndexError:
	    	product_category = 'null'

	    asc21 = container.find_all("td",{"data-column":"feature-standard-frequency-mhz"})
	    try:
	    	standard_frequency = asc21[0].text.strip()
	    except IndexError:
	    	standard_frequency = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-frequency-tolerance-ppm"})
	    try:
	    	frequency_tolerance = asc22[0].text.strip()
	    except IndexError:
	    	frequency_tolerance = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-frequency-stability-ppm"})
	    try:
	    	frequency_stability = asc23[0].text.strip()
	    except IndexError:
	    	frequency_stability = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-load-capacitance-pf"})
	    try:
	    	load_capacitance = asc235[0].text.strip()
	    except IndexError:
	    	load_capacitance = 'null'

	    asc24 = container.find_all("td",{"data-column":"feature-series-resistance-ohm"})
	    try:
	    	series_resistance = asc24[0].text.strip()
	    except IndexError:
	    	series_resistance = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-mode-of-oscillation"})
	    try:
	    	mode_of_oscillation = asc25[0].text.strip()
	    except IndexError:
	    	mode_of_oscillation = 'null'

	    asc26 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc26[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc27 = container.find_all("td",{"data-column":"feature-packaging"})
	    try:
	    	packaging = asc27[0].text.strip()
	    except IndexError:
	    	packaging = 'null'

	    asc310 = container.find_all("td",{"data-column":"feature-pin-count"})
	    try:
	    	pin_count = asc310[0].text.strip()
	    except IndexError:
	    	pin_count = 'null'

	    asc34 = container.find_all("td",{"data-column":"feature-supplier-package"})
	    try:
	    	supplier_package = asc34[0].text.strip()
	    except IndexError:
	    	supplier_package = 'null'

	    asc35 = container.find_all("td",{"data-column":"feature-standard-package-name"})
	    try:
	    	standard_package_name = asc35[0].text.strip()
	    except IndexError:
	    	standard_package_name = 'null'

	    asc36 = container.find_all("td",{"data-column":"feature-military"})
	    try:
	    	military = asc36[0].text.strip()
	    except IndexError:
	    	military = 'null'

	    asc40 = container.find_all("td",{"data-column":"feature-automotive"})
	    try:
	    	automotive = asc40[0].text.strip()
	    except IndexError:
	    	automotive = 'null'

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_category + ";" + standard_frequency + ";" + frequency_tolerance + ";" + frequency_stability + ";" + load_capacitance + ";" + series_resistance + ";" + mode_of_oscillation + ";" + operating_temperature + ";" + packaging + ";" + pin_count + ";" + supplier_package + ";" + standard_package_name + ";" + military + ";" + automotive + "\n")
    
    print(page)

f.close()