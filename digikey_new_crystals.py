import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(3,113)]

filename = "digikey_crystlas(2).csv"
f = open(filename, "w")
headers = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; packaging; series; status; typee; frequence; freq_stability; freq_tolerance; load_capacitance; esr; operating_mode;operating_temperature; ratings; mounting_type; package_case; size_dimension; height_seated\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/crystals-oscillators-resonators/crystals/171?FV=ffe000ab&quantity=0&ColumnSort=0&pageSize=500&page=' + page

    #opening up connection' grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    sleep(randint(30,50))

    #html parsing
    page_soup = soup(page_html, "html.parser")
    table_body = page_soup.find_all("tbody")[0]
    containers = table_body.find_all("tr",{"itemtype":"http://schema.org/Product"})

    f.write(headers)

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

	    frq = container.find_all("td",{"class":"CLS 2150 ptable-param"})
	    try:
	    	freq = frq[0].text.strip()
	    except IndexError:
	    	freq = 'null'

	    frq_s = container.find_all("td",{"class":"CLS 253 ptable-param"})
	    try:
	    	freq_stability = frq_s[0].text.strip()
	    except IndexError:
	    	freq_stability = 'null'

	    frq_t = container.find_all("td",{"class":"CLS 537 ptable-param"})
	    try:
	    	freq_tolerance = frq_t[0].text.strip()
	    except IndexError:
	    	freq_tolerance = 'null'

	    load = container.find_all("td",{"class":"CLS 35 ptable-param"})
	    try:
	    	load_capacitance = load[0].text.strip()
	    except IndexError:
	    	load_capacitance = 'null'

	    esr = container.find_all("td",{"class":"CLS 2082 ptable-param"})
	    try:
	    	e_s_resistance = esr[0].text.strip()
	    except IndexError:
	    	e_s_resistance = 'null'

	    o_m = container.find_all("td",{"class":"CLS 538 ptable-param"})
	    try:
	    	operating_mode = o_m[0].text.strip()
	    except IndexError:
	    	operating_mode = 'null'

	    o_t = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = o_t[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    rtng = container.find_all("td",{"class":"CLS 707 ptable-param"})
	    try:
	    	rating = rtng[0].text.strip()
	    except IndexError:
	    	rating = 'null'

	    mntg = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = mntg[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    pck = container.find_all("td",{"class":"CLS 16 ptable-param"})
	    try:
	    	package_case = pck[0].text.strip()
	    except IndexError:
	    	package_case = 'null'

	    size = container.find_all("td",{"class":"CLS 46 ptable-param"})
	    try:
	    	size_dimension = size[0].text.strip()
	    except IndexError:
	    	size_dimension = 'null'

	    hght = container.find_all("td",{"class":"CLS 1500 ptable-param"})
	    try:
	    	height_seated = hght[0].text.strip()
	    except IndexError:
	    	height_seated = 'null'

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

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + typee + ";" +  freq + ";" + freq_stability + ";" + freq_tolerance + ";" + load_capacitance + ";" + e_s_resistance + ";" + operating_mode + ";" + operating_temperature + ";" + rating + ";" + mounting_type + ";" + package_case  + ";" + size_dimension + ";" + height_seated + "\n")
    
    print(page)

f.close()
