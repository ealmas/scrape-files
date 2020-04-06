import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,11)]

filename = "digikey_EMI_filter.csv"
f = open(filename, "w")
header = "mfg_partnumber; unit_price; manufacturer; description; qty_available; min_qty; packaging; series; status; typee; filter_order; tecnology; number_of_Channels; cutoff_frequency; attenuation_value; resistance_Channel; current; values; ESD_protection; operating_temperature; applications; voltage_rated; mounting_type; package_case; size_dimension; height\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/filters/emi-rfi-filters-lc-rc-networks/835?FV=ffe00343&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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

	    mtrl = container.find_all("td",{"class":"CLS 375 ptable-param"})
	    try:
	    	filter_order = mtrl[0].text.strip()
	    except IndexError:
	    	filter_order = 'null'

	    indctnc = container.find_all("td",{"class":"CLS 570 ptable-param"})
	    try:
	    	tecnology = indctnc[0].text.strip()
	    except IndexError:
	    	tecnology = 'null'

	    tlrnc = container.find_all("td",{"class":"CLS 2093 ptable-param"})
	    try:
	    	number_of_Channels = tlrnc[0].text.strip()
	    except IndexError:
	    	number_of_Channels = 'null'

	    rtng = container.find_all("td",{"class":"CLS 600 ptable-param"})
	    try:
	    	cutoff_frequency = rtng[0].text.strip()
	    except IndexError:
	    	cutoff_frequency = 'null'

	    strtn = container.find_all("td",{"class":"CLS 331 ptable-param"})
	    try:
	    	attenuation_value = strtn[0].text.strip()
	    except IndexError:
	    	attenuation_value = 'null'

	    shldng = container.find_all("td",{"class":"CLS 1540 ptable-param"})
	    try:
	    	resistance_Channel = shldng[0].text.strip()
	    except IndexError:
	    	resistance_Channel = 'null'

	    rstnc = container.find_all("td",{"class":"CLS 2155 ptable-param"})
	    try:
	    	current = rstnc[0].text.strip()
	    except IndexError:
	    	current = 'null'

	    frq = container.find_all("td",{"class":"CLS 300 ptable-param"})
	    try:
	    	values = frq[0].text.strip()
	    except IndexError:
	    	values = 'null'

	    slf = container.find_all("td",{"class":"CLS 1541 ptable-param"})
	    try:
	    	ESD_protection = slf[0].text.strip()
	    except IndexError:
	    	ESD_protection = 'null'

	    rt = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = rt[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    tmpr = container.find_all("td",{"class":"CLS 405 ptable-param"})
	    try:
	    	applications = tmpr[0].text.strip()
	    except IndexError:
	    	applications = 'null'

	    mntg = container.find_all("td",{"class":"CLS 14 ptable-param"})
	    try:
	    	voltage_rated = mntg[0].text.strip()
	    except IndexError:
	    	voltage_rated = 'null'

	    pck = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = pck[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    spl_pck = container.find_all("td",{"class":"CLS 16 ptable-param"})
	    try:
	    	package_case = spl_pck[0].text.strip()
	    except IndexError:
	    	package_case = 'null'

	    size = container.find_all("td",{"class":"CLS 46 ptable-param"})
	    try:
	    	size_dimension = size[0].text.strip()
	    except IndexError:
	    	size_dimension = 'null'

	    hgt = container.find_all("td",{"class":"CLS 329 ptable-param"})
	    try:
	    	height = hgt[0].text.strip()
	    except IndexError:
	    	height = 'null'

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

	    f.write(part_numbers + ";" + price + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + typee + ";" +  filter_order + ";" + tecnology + ";" + number_of_Channels + ";" + cutoff_frequency + ";" + attenuation_value + ";" + resistance_Channel + ";" + current + ";" + values + ";" + ESD_protection + ";" + operating_temperature + ";" + applications + ";" + voltage_rated + ";" + mounting_type  + ";" + package_case + ";" + size_dimension + ";" + height + "\n")
    
    print(page)

f.close()
