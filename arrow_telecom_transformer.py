import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,26)]

filename = "arrow_telecom_transformer.csv"
f = open(filename, "w", encoding="utf-8")
#with open(filename, "w", encoding="utf-8") as f:
#header = "manufacturer; description; qty_available; others\n"
header = "manufacturer_part; manufacturer; description; pricing; qty_available; product_category; transformer_type; turns_ratio; max_DCR_primary_side; max_DCR_secondary_side; high_petential; min_return_loss; max_insertion_loss; lead_style; number_of_terminals; operating_temperature; package_type; packaging; dose_level; rad_hard; military; automotive\n"

for page in pages:

    my_url = 'https://www.arrow.com/en/products/search?page='+ page + '&prodline=Telecom%20Transformers&selectedType=plNames&perPage=100'
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

	    asc21 = container.find_all("td",{"data-column":"feature-transformer-type"})
	    try:
	    	transformer_type = asc21[0].text.strip()
	    except IndexError:
	    	transformer_type = 'null'

	    asc22 = container.find_all("td",{"data-column":"feature-turns-ratio"})
	    try:
	    	turns_ratio = asc22[0].text.strip()
	    except IndexError:
	    	turns_ratio = 'null'

	    asc23 = container.find_all("td",{"data-column":"feature-maximum-dcr-primary-side-ohm"})
	    try:
	    	max_DCR_primary_side = asc23[0].text.strip()
	    except IndexError:
	    	max_DCR_primary_side = 'null'

	    asc235 = container.find_all("td",{"data-column":"feature-maximum-dcr-secondary-side-ohm"})
	    try:
	    	max_DCR_secondary_side = asc235[0].text.strip()
	    except IndexError:
	    	max_DCR_secondary_side = 'null'

	    asc24 = container.find_all("td",{"data-column":"feature-high-potential"})
	    try:
	    	high_petential = asc24[0].text.strip()
	    except IndexError:
	    	high_petential = 'null'

	    asc25 = container.find_all("td",{"data-column":"feature-minimum-return-loss-db"})
	    try:
	    	min_return_loss = asc25[0].text.strip()
	    except IndexError:
	    	min_return_loss = 'null'

	    asc26 = container.find_all("td",{"data-column":"feature-maximum-insertion-loss-db"})
	    try:
	    	max_insertion_loss = asc26[0].text.strip()
	    except IndexError:
	    	max_insertion_loss = 'null'

	    asc27 = container.find_all("td",{"data-column":"feature-lead-style"})
	    try:
	    	lead_style = asc27[0].text.strip()
	    except IndexError:
	    	lead_style = 'null'

	    asc310 = container.find_all("td",{"data-column":"feature-number-of-terminals"})
	    try:
	    	number_of_terminals = asc310[0].text.strip()
	    except IndexError:
	    	number_of_terminals = 'null'

	    asc34 = container.find_all("td",{"data-column":"feature-operating-temperature-c"})
	    try:
	    	operating_temperature = asc34[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    asc35 = container.find_all("td",{"data-column":"feature-package-type"})
	    try:
	    	package_type = asc35[0].text.strip()
	    except IndexError:
	    	package_type = 'null'

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

	    f.write(manufacturer_part + ";" + manufacturer + ";" + description + ";" + pricing + ";" + availability + ";" + product_type + ";" + transformer_type + ";" + turns_ratio + ";" + max_DCR_primary_side + ";" + max_DCR_secondary_side + ";" + high_petential + ";" + min_return_loss + ";" + max_insertion_loss + ";" + lead_style + ";" + number_of_terminals + ";" + operating_temperature + ";" + package_type + ";" + packaging + ";" + dose_level + ";" + rad_hard + ";" + military + ";" + automotive + "\n")
    
    print(page)

f.close()