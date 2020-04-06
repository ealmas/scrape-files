import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,7)]

filename = "digikey_real_time_clocks.csv"
f = open(filename, "w", encoding="utf-8" )

header = "mfg_partnumber; unit_price; manufacturer; description; qty_available; min_qty; packaging; series; status; typee; features; memory_size; time_format; date_format; interface; voltage_supply; voltage_supply_battery; current_timekeeping; operating_temperature; mounting_type; package_case; supplier_device_package\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/integrated-circuits-ics/clock-timing-real-time-clocks/690?FV=-8%7C690&quantity=0&ColumnSort=0&k=real+time+clock&pageSize=500&page=' + page
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

	    typ = container.find_all("td",{"class":"CLS 183 ptable-param"})
	    try:
	    	typee = typ[0].text.strip()
	    except IndexError:
	    	typee = 'null'

	    typ2 = container.find_all("td",{"class":"CLS 5 ptable-param"})
	    try:
	    	features = typ2[0].text.strip()
	    except IndexError:
	    	features = 'null'

	    mtrl = container.find_all("td",{"class":"CLS 142 ptable-param"})
	    try:
	    	memory_size = mtrl[0].text.strip()
	    except IndexError:
	    	memory_size = 'null'

	    indctnc = container.find_all("td",{"class":"CLS 341 ptable-param"})
	    try:
	    	time_format = indctnc[0].text.strip()
	    except IndexError:
	    	time_format = 'null'

	    rtng = container.find_all("td",{"class":"CLS 342 ptable-param"})
	    try:
	    	date_format = rtng[0].text.strip()
	    except IndexError:
	    	date_format = 'null'

	    strtn = container.find_all("td",{"class":"CLS 154 ptable-param"})
	    try:
	    	interface = strtn[0].text.strip()
	    except IndexError:
	    	interface = 'null'

	    shldng = container.find_all("td",{"class":"CLS 276 ptable-param"})
	    try:
	    	voltage_supply = shldng[0].text.strip()
	    except IndexError:
	    	voltage_supply = 'null'

	    rt = container.find_all("td",{"class":"CLS 1446 ptable-param"})
	    try:
	    	voltage_supply_battery = rt[0].text.strip()
	    except IndexError:
	    	voltage_supply_battery = 'null'

	    rstnc = container.find_all("td",{"class":"CLS 1754 ptable-param"})
	    try:
	    	current_timekeeping = rstnc[0].text.strip()
	    except IndexError:
	    	current_timekeeping = 'null'

	    tmpr = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = tmpr[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    frq = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = frq[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    size = container.find_all("td",{"class":"CLS 16 ptable-param"})
	    try:
	    	package_case = size[0].text.strip()
	    except IndexError:
	    	package_case = 'null'

	    mntg = container.find_all("td",{"class":"CLS 1291 ptable-param"})
	    try:
	    	supplier_device_package = mntg[0].text.strip()
	    except IndexError:
	    	supplier_device_package = 'null'

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

	    f.write(part_numbers + ";" + price + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + typee + ";" +  features +  ";" + memory_size + ";" + time_format + ";" + date_format + ";" + interface + ";" + voltage_supply + ";" + voltage_supply_battery + ";" + current_timekeeping + ";" + operating_temperature + ";" + mounting_type + ";" + package_case + ";" + supplier_device_package + "\n")
    
    print(page)

f.close()
