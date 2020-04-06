import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,28)]

filename = "digikey_modular_connectors.csv"
f = open(filename, "w", encoding="utf-8" )

header = "mfg_partnumber: unit_price: manufacturer: description: qty_available: min_qty: packaging: series: status: connector_typee: number_of_positions: number_of_ports: number_of_rows: mounting_type: orientation: termination: shielding: ratings: features: led_color: ingress_protection: tab_direction: contact_material: contact_finish\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/connectors-interconnects/modular-connectors-jacks/366?FV=ffe0016e&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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

	    p_id = container.find_all("td",{"class":"tr-mfgPartNumber"})
	    part_numbers = p_id[0].text.strip()

	    prc = container.find_all("td",{"class":"tr-unitPrice ptable-param"})
	    price = prc[0].text.strip()

	    mnf = container.find_all("td",{"class":"tr-vendor"})
	    manufacturer = mnf[0].text.strip()

	    dscr = container.find_all("td",{"class":"tr-description"})
	    description = dscr[0].text.strip()

	    qtySpan = container.find_all("td", {"class":"tr-qtyAvailable ptable-param"})
	    try:
	    	qty_available = qtySpan[0].find("span",{"class":"desktop"}).text.strip()
	    except AttributeError:
	    	qty_available = 'null'

	    m_qty = container.find_all("td",{"class":"tr-minQty ptable-param"})
	    try:
	        min_qty = m_qty[0].find("span",{"class":"desktop"}).text.replace('Non-Stock','').strip()
	    except AttributeError:
	        min_qty =  'null'

	    pckg = container.find_all("td",{"class":"tr-packaging ptable-param"})
	    packaging = pckg[0].text.replace('Alternate Packaging','').strip()

	    srs = container.find_all("td",{"class":"tr-series ptable-param"})
	    series = srs[0].text.strip()

	    stts = container.find_all("td",{"class":"CLS 1989 ptable-param"})
	    status = stts[0].text.strip()

	    typ = container.find_all("td",{"class":"CLS 28 ptable-param"})
	    try:
	    	connector_typee = typ[0].text.strip()
	    except IndexError:
	    	connector_typee = 'null'

	    typ2 = container.find_all("td",{"class":"CLS 272 ptable-param"})
	    try:
	    	number_of_positions = typ2[0].text.strip()
	    except IndexError:
	    	number_of_positions = 'null'

	    mtrl = container.find_all("td",{"class":"CLS 2171 ptable-param"})
	    try:
	    	number_of_ports = mtrl[0].text.strip()
	    except IndexError:
	    	number_of_ports = 'null'

	    indctnc = container.find_all("td",{"class":"CLS 2172 ptable-param"})
	    try:
	    	number_of_rows = indctnc[0].text.strip()
	    except IndexError:
	    	number_of_rows = 'null'

	    rtng = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = rtng[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    strtn = container.find_all("td",{"class":"CLS 208 ptable-param"})
	    try:
	    	orientation = strtn[0].text.strip()
	    except IndexError:
	    	orientation = 'null'

	    shldng = container.find_all("td",{"class":"CLS 589 ptable-param"})
	    try:
	    	termination = shldng[0].text.strip()
	    except IndexError:
	    	termination = 'null'

	    rt = container.find_all("td",{"class":"CLS 80 ptable-param"})
	    try:
	    	shielding = rt[0].text.strip()
	    except IndexError:
	    	shielding = 'null'

	    rstnc = container.find_all("td",{"class":"CLS 707 ptable-param"})
	    try:
	    	ratings = rstnc[0].text.strip()
	    except IndexError:
	    	ratings = 'null'

	    tmpr = container.find_all("td",{"class":"CLS 5 ptable-param"})
	    try:
	    	features = tmpr[0].text.strip()
	    except IndexError:
	    	features = 'null'

	    frq = container.find_all("td",{"class":"CLS 596 ptable-param"})
	    try:
	    	led_color = frq[0].text.strip()
	    except IndexError:
	    	led_color = 'null'

	    size = container.find_all("td",{"class":"CLS 697 ptable-paramingress_protection"})
	    try:
	    	ingress_protection = size[0].text.strip()
	    except IndexError:
	    	ingress_protection = 'null'

	    mntg = container.find_all("td",{"class":"CLS 760 ptable-param"})
	    try:
	    	tab_direction = mntg[0].text.strip()
	    except IndexError:
	    	tab_direction = 'null'

	    pck = container.find_all("td",{"class":"CLS 1084 ptable-param"})
	    try:
	    	contact_material = pck[0].text.strip()
	    except IndexError:
	    	contact_material = 'null'

	    spl_pck = container.find_all("td",{"class":"CLS 30 ptable-param"})
	    try:
	    	contact_finish = spl_pck[0].text.strip()
	    except IndexError:
	    	contact_finish = 'null'

	    

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

	    f.write(part_numbers + ":" + price + ":" + manufacturer + ":" + description + ":" + qty_available + ":" + min_qty + ":" + packaging + ":" + series + ":" + status + ":" + connector_typee + ":" +  number_of_positions +  ":" + number_of_ports + ":" + number_of_rows + ":" + mounting_type + ":" + orientation + ":" + termination + ":" + shielding + ":" + ratings + ":" + features + ":" + led_color + ":" + ingress_protection + ":" + tab_direction + ":" + contact_material  + ":" + contact_finish + "\n")
    
    print(page)

f.close()
