import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,335)]

filename = "digikey_fixed_inductors.csv"
f = open(filename, "w")
header = "mfg_partnumber; unit_price; manufacturer; description; qty_available; min_qty; packaging; series; status; typee; material_core; inductance; tolerance; current_rating; current_saturation; shielding; resistance; freq; self_resonant; ratings; temperature; frequency_test; features; mounting_type; package_case; supplier_package; size_dimension; height_seated\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/inductors-coils-chokes/fixed-inductors/71?FV=ffe00047&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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
	    description = dscr[0].text.replace(';','').strip()

	    qtySpan = container.find_all("td", {"class":"tr-qtyAvailable ptable-param"})
	    try:
	    	qty_available = qtySpan[0].find("span",{"class":"phone"}).text.strip()
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

	    mtrl = container.find_all("td",{"class":"CLS 1221 ptable-param"})
	    try:
	    	material_core = mtrl[0].text.strip()
	    except IndexError:
	    	material_core = 'null'

	    indctnc = container.find_all("td",{"class":"CLS 2087 ptable-param"})
	    try:
	    	inductance = indctnc[0].text.strip()
	    except IndexError:
	    	inductance = 'null'

	    tlrnc = container.find_all("td",{"class":"CLS 3 ptable-param"})
	    try:
	    	tolerance = tlrnc[0].text.strip()
	    except IndexError:
	    	tolerance = 'null'

	    rtng = container.find_all("td",{"class":"CLS 2088 ptable-param"})
	    try:
	    	current_rating = rtng[0].text.strip()
	    except IndexError:
	    	current_rating = 'null'

	    strtn = container.find_all("td",{"class":"CLS 1219 ptable-param"})
	    try:
	    	current_saturation = strtn[0].text.strip()
	    except IndexError:
	    	current_saturation = 'null'

	    shldng = container.find_all("td",{"class":"CLS 80 ptable-param"})
	    try:
	    	shielding = shldng[0].text.strip()
	    except IndexError:
	    	shielding = 'null'

	    rstnc = container.find_all("td",{"class":"CLS 314 ptable-param"})
	    try:
	    	resistance = rstnc[0].text.strip()
	    except IndexError:
	    	resistance = 'null'

	    frq = container.find_all("td",{"class":"CLS 705 ptable-param"})
	    try:
	    	freq = frq[0].text.strip()
	    except IndexError:
	    	freq = 'null'

	    slf = container.find_all("td",{"class":"CLS 706 ptable-param"})
	    try:
	    	self_resonant = slf[0].text.strip()
	    except IndexError:
	    	self_resonant = 'null'

	    rt = container.find_all("td",{"class":"CLS 707 ptable-param"})
	    try:
	    	ratings = rt[0].text.strip()
	    except IndexError:
	    	ratings = 'null'

	    tmpr = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	temperature = tmpr[0].text.strip()
	    except IndexError:
	    	temperature = 'null'

	    frq_tst = container.find_all("td",{"class":"CLS 1222 ptable-param"})
	    try:
	    	frequency_test = frq_tst[0].text.strip()
	    except IndexError:
	    	frequency_test = 'null'

	    ftrs = container.find_all("td",{"class":"CLS 0 ptable-param"})
	    try:
	    	features = ftrs[0].text.strip()
	    except IndexError:
	    	features = 'null'

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

	    spl_pck = container.find_all("td",{"class":"CLS 1291 ptable-param"})
	    try:
	    	supplier_package = spl_pck[0].text.strip()
	    except IndexError:
	    	supplier_package = 'null'

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

	    f.write(part_numbers + ";" + price + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + typee + ";" +  material_core + ";" + inductance + ";" + tolerance + ";" + current_rating + ";" + current_saturation + ";" + shielding + ";" + resistance + ";" + freq + ";" + self_resonant + ";" + ratings + ";" + temperature + ";" + frequency_test + ";" + features + ";" + mounting_type + ";" + package_case  + ";" + supplier_package + ";" + size_dimension + ";" + height_seated + "\n")
    
    print(page)

f.close()
