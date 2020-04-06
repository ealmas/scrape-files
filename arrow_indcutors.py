import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(232,448)]

filename = "arrow_fixed_inductors2.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_category; technology; protection_style; core_meterial; inductance; tolerance; impedance; inductance_test_frequency; maximum_dc_current; maximum_dc_resistance; minimum_quality_factor; min_self_resonant_freq; case_size; operating_temperature; product_diameter; product_lenght; product_depth; prodcut_height; packaging; dose_level; rad_hard; military; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page='+ page + '&prodline=Inductor%20Surface%20Mount&selectedType=plNames&perPage=100'
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
	    	technology = asc21[0].text.strip()
	    except IndexError:
	    	technology = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-protection-style"})
	    try:
	    	protection_style = asc22[0].text.strip()
	    except IndexError:
	    	protection_style = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-core-material"})
	    try:
	    	core_meterial = asc23[0].text.strip()
	    except IndexError:
	    	core_meterial = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-inductance-h"})
	    try:
	    	inductance = asc235[0].text.strip()
	    except IndexError:
	    	inductance = 'null'

	    asc24 = container.find_all("td",{"data-column":"feature-tolerance"})
	    try:
	    	tolerance = asc24[0].text.strip()
	    except IndexError:
	    	tolerance = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-impedance-ohm"})
	    try:
	    	impedance = asc25[0].text.strip()
	    except IndexError:
	    	impedance = 'null'

	    asc26 = container.find_all("td",{"data-column":"feature-inductance-test-frequency-hz"})
	    try:
	    	inductance_test_frequency = asc26[0].text.strip()
	    except IndexError:
	    	inductance_test_frequency = 'null'

	    asc27 = container.find_all("td",{"data-column":"feature-maximum-dc-current-a"})
	    try:
	    	maximum_dc_current = asc27[0].text.strip()
	    except IndexError:
	    	maximum_dc_current = 'null'

	    asc271 = container.find_all("td",{"data-column":"feature-maximum-dc-resistance-ohm"})
	    try:
	    	maximum_dc_resistance = asc271[0].text.strip()
	    except IndexError:
	    	maximum_dc_resistance = 'null'

	    asc310 = container.find_all("td",{"data-column":"feature-minimum-quality-factor"})
	    try:
	    	minimum_quality_factor = asc310[0].text.strip()
	    except IndexError:
	    	minimum_quality_factor = 'null'

	    asc34 = container.find_all("td",{"data-column":"feature-minimum-self-resonant-frequency-hz"})
	    try:
	    	min_self_resonant_freq = asc34[0].text.strip()
	    except IndexError:
	    	min_self_resonant_freq = 'null'

	    asc35 = container.find_all("td",{"data-column":"feature-case-size"})
	    try:
	    	case_size = asc35[0].text.strip()
	    except IndexError:
	    	case_size = 'null'

	    asc36 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc36[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc40 = container.find_all("td",{"data-column":"feature-product-diameter-mm"})
	    try:
	    	product_diameter = asc40[0].text.strip()
	    except IndexError:
	    	product_diameter = 'null'

	    asc415 = container.find_all("td",{"data-column":"feature-product-length-mm"})
	    try:
	    	product_lenght = asc415[0].text.strip()
	    except IndexError:
	    	product_lenght = 'null'

	    asc41 = container.find_all("td",{"data-column":"feature-product-depth-mm"})
	    try:
	    	product_depth = asc41[0].text.strip()
	    except IndexError:
	    	product_depth = 'null'

	    asc42 = container.find_all("td",{"data-column":"feature-product-height-mm"})
	    try:
	    	prodcut_height = asc42[0].text.strip()
	    except IndexError:
	    	prodcut_height = 'null'

	    asc43 = container.find_all("td",{"data-column":"feature-packaging"})
	    try:
	    	packaging = asc43[0].text.strip()
	    except IndexError:
	    	packaging = 'null'

	    asc44 = container.find_all("td",{"data-column":"feature-dose-level-krad"})
	    try:
	    	dose_level = asc44[0].text.strip()
	    except IndexError:
	    	dose_level = 'null'

	    asc45 = container.find_all("td",{"data-column":"feature-rad-hard"})
	    try:
	    	rad_hard = asc45[0].text.strip()
	    except IndexError:
	    	rad_hard = 'null'

	    asc46 = container.find_all("td",{"data-column":"feature-military"})
	    try:
	    	military = asc46[0].text.strip()
	    except IndexError:
	    	military = 'null'

	    asc47 = container.find_all("td",{"data-column":"feature-automotive"})
	    try:
	    	automotive = asc47[0].text.strip()
	    except IndexError:
	    	automotive = 'null'

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_type + ";" + technology + ";" + protection_style + ";" + core_meterial + ";" + inductance + ";" + tolerance + ";" + impedance + ";" + inductance_test_frequency + ";" + maximum_dc_current + ";" + maximum_dc_resistance + ";" + minimum_quality_factor + ";" + min_self_resonant_freq + ";" + case_size + ";" + operating_temperature + ";" + product_diameter + ";" + product_lenght + ";" + product_depth + ";" + prodcut_height + ";" +  packaging + ";" + dose_level + ";" + rad_hard + ";" + military + ";" + automotive + "\n")
    
    print(page)

f.close()