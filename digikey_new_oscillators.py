import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import io
from time import sleep
from random import randint

pages = [str(i) for i in range(1,680)]

filename = "digikey_oscillators.csv"
f = open(filename, "w", encoding="utf-8")
header = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; packaging; series; status; base_resonator; typee; frequency; function; output; voltage_suply; frequency_stability; absoulute_pull_range; operating_temperature; spread_spectrum; current_supply; ratings; mounting_type; package_case; size_dimension; height_seated\n"
for page in pages:

    my_url = 'https://www.digikey.com/products/en/crystals-oscillators-resonators/oscillators/172?FV=ffe000ac&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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

	    pckg = container.find_all("td",{"class":"tr-packaging ptable-param"})
	    packaging = pckg[0].text.replace('Alternate Packaging','').strip()

	    srs = container.find_all("td",{"class":"tr-series ptable-param"})
	    series = srs[0].text.strip()

	    stts = container.find_all("td",{"class":"CLS 1989 ptable-param"})
	    status = stts[0].text.strip()

	    bsrsntr = container.find_all("td",{"class":"CLS 2338 ptable-param"})
	    try:
	    	base_resonator = bsrsntr[0].text.strip()
	    except IndexError:
	    	base_resonator = 'null'

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

	    fnctn = container.find_all("td",{"class":"CLS 110 ptable-param"})
	    try:
	    	function = fnctn[0].text.strip()
	    except IndexError:
	    	function = 'null'

	    outpt = container.find_all("td",{"class":"CLS 71 ptable-param"})
	    try:
	    	output = outpt[0].text.strip()
	    except IndexError:
	    	output = 'null'

	    vltg_sply = container.find_all("td",{"class":"CLS 276 ptable-param"})
	    try:
	    	voltage_suply = vltg_sply[0].text.strip()
	    except IndexError:
	    	voltage_suply = 'null'

	    frq_stb = container.find_all("td",{"class":"CLS 253 ptable-param"})
	    try:
	    	frequency_stability = frq_stb[0].text.strip()
	    except IndexError:
	    	frequency_stability = 'null'

	    apr = container.find_all("td",{"class":"CLS 0 ptable-param"})
	    try:
	    	absoulute_pull_range = apr[0].text.strip()
	    except IndexError:
	    	absoulute_pull_range = 'null'

	    o_t = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = o_t[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    spctrm = container.find_all("td",{"class":"CLS 0 ptable-param"})
	    try:
	    	spread_spectrum = spctrm[0].text.strip()
	    except IndexError:
	    	spread_spectrum = 'null'

	    crrnt_sply = container.find_all("td",{"class":"CLS 1121 ptable-param"})
	    try:
	    	current_supply = crrnt_sply[0].text.strip()
	    except IndexError:
	    	current_supply = 'null'

	    ratng = container.find_all("td",{"class":"CLS 707 ptable-param"})
	    try:
	    	ratings = ratng[0].text.strip()
	    except IndexError:
	    	ratings = 'null'

	    mnt_typ = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = mnt_typ[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    pck_cs = container.find_all("td",{"class":"CLS 16 ptable-param"})
	    try:
	    	package_case = pck_cs[0].text.strip()
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

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + base_resonator + ";" +  typee + ";" + freq + ";" + function + ";" + output + ";" + voltage_suply + ";" + frequency_stability + ";" + absoulute_pull_range + ";" + operating_temperature + ";" + spread_spectrum + ";" + current_supply + ";" + ratings + ";" + mounting_type + ";" + package_case + ";" + size_dimension + ";" + height_seated + "\n")
    
    print(page)

f.close()
