import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import io
from time import sleep
from random import randint

pages = [str(i) for i in range(1,13)]

filename = "digikey_power_transformers.csv"
f = open(filename, "w", encoding="utf-8")
header = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; series; status; type; voltage_primary; voltage_secondary; current_output; primary_windings; secondary_winding; center_tap; power_max; mounting_type; termination_style; size_dimension; height_seated; voltage_isolation; weight\n"
for page in pages:

    my_url = 'https://www.digikey.com/products/en/transformers/power-transformers/164?FV=ffe000a4&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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

	    typ = container.find_all("td",{"class":"CLS 183 ptable-param"})
	    try:
	    	typee= typ[0].text.strip()
	    except IndexError:
	    	typee = 'null'

	    vltg = container.find_all("td",{"class":"CLS 1393 ptable-param"})
	    try:
	    	voltage_primary = vltg[0].text.strip()
	    except IndexError:
	    	voltage_primary = 'null'

	    vltg2 = container.find_all("td",{"class":"CLS 1617 ptable-param"})
	    try:
	    	voltage_secondary = vltg2[0].text.strip()
	    except IndexError:
	    	voltage_secondary = 'null'

	    crrnt = container.find_all("td",{"class":"CLS 1120 ptable-param"})
	    try:
	    	current_output = crrnt[0].text.strip()
	    except IndexError:
	    	current_output = 'null'

	    prmry = container.find_all("td",{"class":"CLS 496 ptable-param"})
	    try:
	    	primary_windings = prmry[0].text.strip()
	    except IndexError:
	    	primary_windings = 'null'

	    scndry = container.find_all("td",{"class":"CLS 497 ptable-param"})
	    try:
	    	secondary_winding = scndry[0].text.strip()
	    except IndexError:
	    	secondary_winding = 'null'

	    cntr = container.find_all("td",{"class":"CLS 1618 ptable-param"})
	    try:
	    	center_tap = cntr[0].text.strip()
	    except IndexError:
	    	center_tap = 'null'

	    pwr = container.find_all("td",{"class":"CLS 588 ptable-param"})
	    try:
	    	power_max = pwr[0].text.strip()
	    except IndexError:
	    	power_max = 'null'

	    mntg = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = mntg[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    trmntn = container.find_all("td",{"class":"CLS 258 ptable-param"})
	    try:
	    	termination_style = trmntn[0].text.strip()
	    except IndexError:
	    	termination_style = 'null'

	    sz = container.find_all("td",{"class":"CLS 46 ptable-param"})
	    try:
	    	size_dimension = sz[0].text.strip()
	    except IndexError:
	    	size_dimension = 'null'

	    height = container.find_all("td",{"class":"CLS 1500 ptable-param"})
	    try:
	    	height_seated = height[0].text.strip()
	    except IndexError:
	    	height_seated = 'null'

	    vltg = container.find_all("td",{"class":"CLS 597 ptable-param"})
	    try:
	    	voltage_isolation = vltg[0].text.strip()
	    except IndexError:
	    	voltage_isolation = 'null'

	    wght = container.find_all("td",{"class":"CLS 211 ptable-param"})
	    try:
	    	weight = wght[0].text.strip()
	    except IndexError:
	    	weight = 'null'

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

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + series + ";" + status + ";" + typee + ";" +  voltage_primary + ";" + voltage_secondary + ";" + current_output + ";" + primary_windings + ";" + secondary_winding + ";" + center_tap + ";" + power_max +  ";" + mounting_type + ";" + termination_style + ";" +  size_dimension + ";" +  height_seated + ";" +  voltage_isolation + ";" + weight + "\n")

    print(page)

f.close()
