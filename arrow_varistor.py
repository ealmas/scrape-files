import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,88)]

filename = "arrow_varistors.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_category; technology; varistor_voltage; max_AC_voltage_rating; max_DC_voltage_rating; clamping_voltage; clamping_current; max_surge_current; max_current; capacitance_value; operating_temperature; size_code; packaging; dose_level; rad_hard; cecc_qualified; military; terminal_pitch; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page='+ page + '&prodline=Varistors&selectedType=plNames&perPage=100'
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

	    asc21 = container.find_all("td",{"data-column":"feature-technology"})
	    try:
	    	techonogy = asc21[0].text.strip()
	    except IndexError:
	    	techonogy = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-varistor-voltage-v"})
	    try:
	    	varistor_voltage = asc22[0].text.strip()
	    except IndexError:
	    	varistor_voltage = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-maximum-ac-voltage-rating-v"})
	    try:
	    	max_AC_voltage_rating = asc23[0].text.strip()
	    except IndexError:
	    	max_AC_voltage_rating = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-maximum-dc-voltage-rating-v"})
	    try:
	    	max_DC_voltage_rating = asc235[0].text.strip()
	    except IndexError:
	    	max_DC_voltage_rating = 'null'

	    asc24 = container.find_all("td",{"data-column":"feature-clamping-voltage-v"})
	    try:
	    	clamping_voltage = asc24[0].text.strip()
	    except IndexError:
	    	clamping_voltage = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-clamping-current-a"})
	    try:
	    	clamping_current = asc25[0].text.strip()
	    except IndexError:
	    	clamping_current = 'null'

	    asc26 = container.find_all("td",{"data-column":"feature-maximum-surge-current-a"})
	    try:
	    	max_surge_current = asc26[0].text.strip()
	    except IndexError:
	    	max_surge_current = 'null'

	    asc27 = container.find_all("td",{"data-column":"feature-maximum-dc-current-a"})
	    try:
	    	max_current = asc27[0].text.strip()
	    except IndexError:
	    	max_current = 'null'

	    asc310 = container.find_all("td",{"data-column":"feature-capacitance-value"})
	    try:
	    	capacitance_value = asc310[0].text.strip()
	    except IndexError:
	    	capacitance_value = 'null'

	    asc34 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc34[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc35 = container.find_all("td",{"data-column":"feature-size-code"})
	    try:
	    	size_code = asc35[0].text.strip()
	    except IndexError:
	    	size_code = 'null'

	    asc36 = container.find_all("td",{"data-column":"feature-packaging"})
	    try:
	    	packaging = asc36[0].text.strip()
	    except IndexError:
	    	packaging = 'null'

	    asc40 = container.find_all("td",{"data-column":"feature-dose-level-krad"})
	    try:
	    	dose_level = asc40[0].text.strip()
	    except IndexError:
	    	dose_level = 'null'

	    asc415 = container.find_all("td",{"data-column":"feature-rad-hard"})
	    try:
	    	rad_hard = asc415[0].text.strip()
	    except IndexError:
	    	rad_hard = 'null'

	    asc4150 = container.find_all("td",{"data-column":"feature-cecc-qualified"})
	    try:
	    	cecc_qualified = asc4150[0].text.strip()
	    except IndexError:
	    	cecc_qualified = 'null'

	    asc41 = container.find_all("td",{"data-column":"feature-military"})
	    try:
	    	military = asc41[0].text.strip()
	    except IndexError:
	    	military = 'null'

	    asc416 = container.find_all("td",{"data-column":"feature-terminal-pitch-mm"})
	    try:
	    	terminal_pitch = asc416[0].text.strip()
	    except IndexError:
	    	terminal_pitch = 'null'

	    asc42 = container.find_all("td",{"data-column":"feature-automotive"})
	    try:
	    	automotive = asc42[0].text.strip()
	    except IndexError:
	    	automotive = 'null'

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_type + ";" + techonogy + ";" + varistor_voltage + ";" + max_AC_voltage_rating + ";" + max_DC_voltage_rating + ";" + clamping_voltage + ";" + clamping_current + ";" + max_surge_current + ";" + max_current + ";" + capacitance_value + ";" + operating_temperature + ";" + size_code + ";" + packaging + ";" + dose_level + ";" + rad_hard + ";" + cecc_qualified + ";" + military + ";" + terminal_pitch + ";" + automotive + "\n")
    
    print(page)

f.close()