import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(10,17)]

filename = "arrow_EMI_filter2.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_category; number_of_lines; number_of_terminals; cut_off_frequency; max_attenuation; capacitance; inductance; resistance; max_current_rating; max_voltage_rating; operating_temperature; termination_style; packaging; military; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page=' + page + '&prodline=EMI%20Filters&selectedType=plNames&perPage=100'
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
	    	product_category = asc20[0].text.strip()
	    except IndexError:
	    	product_category = 'null'

	    asc21 = container.find_all("td",{"data-column":"feature-number-of-lines"})
	    try:
	    	number_of_lines = asc21[0].text.strip()
	    except IndexError:
	    	number_of_lines = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-number-of-terminals"})
	    try:
	    	number_of_terminals = asc22[0].text.strip()
	    except IndexError:
	    	number_of_terminals = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-cut-off-frequency-mhz"})
	    try:
	    	cut_off_frequency = asc23[0].text.strip()
	    except IndexError:
	    	cut_off_frequency = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-maximum-attenuation-db"})
	    try:
	    	max_attenuation = asc235[0].text.strip()
	    except IndexError:
	    	max_attenuation = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-capacitance-pf"})
	    try:
	    	capacitance = asc25[0].text.strip()
	    except IndexError:
	    	capacitance = 'null'

	    asc37 = container.find_all("td",{"data-column":"feature-inductance-nh"})
	    try:
	    	inductance = asc37[0].text.strip()
	    except IndexError:
	    	inductance = 'null'

	    asc38 = container.find_all("td",{"data-column":"feature-resistance-ohm"})
	    try:
	    	resistance = asc38[0].text.strip()
	    except IndexError:
	    	resistance = 'null'

	    asc39 = container.find_all("td",{"data-column":"feature-maximum-current-rating-a"})
	    try:
	    	max_current_rating = asc39[0].text.strip()
	    except IndexError:
	    	max_current_rating = 'null'

	    asc40 = container.find_all("td",{"data-column":"feature-maximum-voltage-rating"})
	    try:
	    	max_voltage_rating = asc40[0].text.strip()
	    except IndexError:
	    	max_voltage_rating = 'null'

	    asc41 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc41[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc44 = container.find_all("td",{"data-column":"feature-termination-style"})
	    try:
	    	termination_style = asc44[0].text.strip()
	    except IndexError:
	    	termination_style = 'null'

	    asc49 = container.find_all("td",{"data-column":"feature-packaging"})
	    try:
	    	packaging = asc49[0].text.strip()
	    except IndexError:
	    	packaging = 'null'

	    asc35 = container.find_all("td",{"data-column":"feature-military"})
	    try:
	    	military = asc35[0].text.strip()
	    except IndexError:
	    	military = 'null'

	    asc36 = container.find_all("td",{"data-column":"feature-automotive"})
	    try:
	    	automotive = asc36[0].text.strip()
	    except IndexError:
	    	automotive = 'null'

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_category + ";" + number_of_lines + ";" + number_of_terminals + ";" + cut_off_frequency + ";" + max_attenuation + ";" + capacitance + ";" + inductance + ";" + resistance + ";" + max_current_rating + ";" + max_voltage_rating + ";" + operating_temperature + ";" + termination_style + ";" + packaging + ";" + military + ";" +  automotive  + "\n")
    
    print(page)

f.close()