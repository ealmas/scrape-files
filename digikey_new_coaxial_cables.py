import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import io
from time import sleep
from random import randint

pages = [str(i) for i in range(1,15)]

filename = "digikey_coaxial_cables.csv"
f = open(filename, "w", encoding="utf-8")
header = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; series; status; gender; style; 1st_connector; 2st_connector; length; cable_type; impedance; frequency_max; color; features; operating_temperature\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/cable-assemblies/coaxial-cables-rf/456?FV=ffe001c8&quantity=0&ColumnSort=0&pageSize=500&page=' + page
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}

    #opening up connection' grabbing the page
    uClient = requests.get(my_url,headers=headers)
    page_html = uClient.content
    uClient.close()

    sleep(randint(30,50))

    #html parsing
    page_soup = soup(page_html, "html.parser")
    table_body = page_soup.find("tbody")
    containers = table_body.find_all("tr")

    f.write(header)

    for container in containers:
	    p_id_d = container.find_all("td",{"class":"tr-dkPartNumber nowrap-culture"})
	    part_numbers_d = p_id_d[0].text.strip()

	    p_id = container.find_all("td",{"class":"tr-mfgPartNumber"})
	    part_numbers = p_id[0].text.strip()

	    mnf = container.find_all("td",{"class":"tr-vendor"})
	    manufacturer = mnf[0].text.strip()

	    dscr = container.find_all("td",{"class":"tr-description"})
	    description = dscr[0].text.strip()

	    qtySpan = container.find_all("td", {"class":"tr-qtyAvailable ptable-param"})
	    try:
	    	qty_available = qtySpan[0].find("span",{"class":"desktop"}).text.strip()
	    except AttributeError:
	    	qty_available = 'null'

	    prc = container.find_all("td",{"class":"tr-unitPrice ptable-param"})
	    price = prc[0].text.strip()

	    m_qty = container.find_all("td",{"class":"tr-minQty ptable-param"})
	    try:
	        min_qty = m_qty[0].find("span",{"class":"desktop"}).text.replace('Non-Stock','').strip()
	    except AttributeError:
	        min_qty =  'null'

	    srs = container.find_all("td",{"class":"tr-series ptable-param"})
	    series = srs[0].text.strip()

	    stts = container.find_all("td",{"class":"CLS 1989 ptable-param"})
	    status = stts[0].text.strip()

	    gndr = container.find_all("td",{"class":"CLS 29 ptable-param"})
	    try:
	    	gender= gndr[0].text.strip()
	    except IndexError:
	    	gender = 'null'

	    sty = container.find_all("td",{"class":"CLS 91 ptable-param"})
	    try:
	    	style = sty[0].text.strip()
	    except IndexError:
	    	style = 'null'

	    cnnctr1 = container.find_all("td",{"class":"CLS 726 ptable-param"})
	    try:
	    	connector_1st = cnnctr1[0].text.strip()
	    except IndexError:
	    	connector_1st = 'null'

	    cnnctr2 = container.find_all("td",{"class":"CLS 727 ptable-param"})
	    try:
	    	connector_2st = cnnctr2[0].text.strip()
	    except IndexError:
	    	connector_2st = 'null'

	    lngth = container.find_all("td",{"class":"CLS 77 ptable-param"})
	    try:
	    	length = lngth[0].text.strip()
	    except IndexError:
	    	length = 'null'

	    typee = container.find_all("td",{"class":"CLS 321 ptable-param"})
	    try:
	    	cable_type = typee[0].text.strip()
	    except IndexError:
	    	cable_type = 'null'

	    impdnc = container.find_all("td",{"class":"CLS 2080 ptable-param"})
	    try:
	    	impedance = impdnc[0].text.strip()
	    except IndexError:
	    	impedance = 'null'

	    frqncy = container.find_all("td",{"class":"CLS 2157 ptable-param"})
	    try:
	    	frequency_max = frqncy[0].text.strip()
	    except IndexError:
	    	frequency_max = 'null'

	    clr = container.find_all("td",{"class":"CLS 37 ptable-param"})
	    try:
	    	color = clr[0].text.strip()
	    except IndexError:
	    	color = 'null'

	    ftrs = container.find_all("td",{"class":"CLS 5 ptable-param"})
	    try:
	    	features = ftrs[0].text.strip()
	    except IndexError:
	    	features = 'null'

	    tmprtr = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = tmprtr[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    #print("part_numbers; " + part_numbers)
	    #print("price; " + price)
	    #print("manufacturer; " + manufacturer)
	    #print("description; " + description)
	    #print("qty_available; " + qty_available)
	    #print("min_qty; " + min_qty)
	    #print("packaging; " + packaging)
	    #print("series; " + series)
	    #print("status; " + status)
	    #print("typee; " + typee)
	    #print("material_core; " + material_core)
	    #print("inductance; " + inductance)
	    #print("tolerance; " + tolerance)
	    #print("current_rating; " + current_rating)
	    #print("current_saturation; " + current_saturation)
	    #print("shielding; " + shielding)
	    #print("resistance; " + resistance)
	    #print("freq; " + freq)
	    #print("self_resonant; " + self_resonant)
	    #print("ratings; " + ratings)
	    #print("temperature; " + temperature)
	    #print("frequency_test; " + frequency_test)
	    #print("features; " + features)
	    #print("mounting_type; " + mounting_type)
	    #print("package_case; " + package_case)
	    #print("supplier_package; " + supplier_package)
	    #print("size_dimension; " + size_dimension)
	    #print("height_seated; " + height_seated)

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + series + ";" + status + ";" + gender + ";" +  style + ";" + connector_1st + ";" + connector_2st + ";" + length + ";" + cable_type + ";" + impedance + ";" + frequency_max +  ";" + color + ";" + features + ";" + operating_temperature + "\n")

    print(page)

f.close()
