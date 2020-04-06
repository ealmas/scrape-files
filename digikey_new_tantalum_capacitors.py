import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,209)]

filename = "digikey_tantalum_capacitors.csv"
f = open(filename, "w")
header = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; packaging; series; status; capacitance; tolerance; voltage_rated; typee; esr; operating_temperature; life_time_temperature; mounting_type; package_case; size_dimension; height_seated; lead_spacing; manufacturer_size_code; ratings; features; failure_rate\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/capacitors/tantalum-capacitors/59?FV=ffe0003b&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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

	    cpctnc = container.find_all("td",{"class":"CLS 2049 ptable-param"})
	    try:
	    	capacitance = cpctnc[0].text.strip()
	    except IndexError:
	    	capacitance = 'null'

	    tlrnc = container.find_all("td",{"class":"CLS 3 ptable-param"})
	    try:
	    	tolerance = tlrnc[0].text.strip()
	    except IndexError:
	    	tolerance = 'null'

	    vltgrtd = container.find_all("td",{"class":"CLS 2079 ptable-param"})
	    try:
	    	voltage_rated = vltgrtd[0].text.strip()
	    except IndexError:
	    	voltage_rated = 'null'

	    typ = container.find_all("td",{"class":"CLS 183 ptable-param"})
	    try:
	    	typee = typ[0].text.strip()
	    except IndexError:
	    	typee = 'null'

	    esr = container.find_all("td",{"class":"CLS 724 ptable-param"})
	    try:
	    	esr_ = esr[0].text.strip()
	    except IndexError:
	    	esr_ = 'null'

	    o_t = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = o_t[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    l_t = container.find_all("td",{"class":"CLS 725 ptable-param"})
	    try:
	    	life_time_temperature = l_t[0].text.strip()
	    except IndexError:
	    	life_time_temperature = 'null'

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

	    ld = container.find_all("td",{"class":"CLS 508 ptable-param"})
	    try:
	    	lead_spacing = ld[0].text.strip()
	    except IndexError:
	    	lead_spacing = 'null'

	    sz = container.find_all("td",{"class":"CLS 987 ptable-param"})
	    try:
	    	manufacturer_size_code = sz[0].text.strip()
	    except IndexError:
	    	manufacturer_size_code = 'null'

	    rt = container.find_all("td",{"class":"CLS 0 ptable-param"})
	    try:
	    	ratings = rt[0].text.strip()
	    except IndexError:
	    	ratings = 'null'

	    ftrs = container.find_all("td",{"class":"CLS 5 ptable-param"})
	    try:
	    	features = ftrs[0].text.strip()
	    except IndexError:
	    	features = 'null'

	    f_rate = container.find_all("td",{"class":"CLS 1531 ptable-param"})
	    try:
	    	failure_rate = f_rate[0].text.strip()
	    except IndexError:
	    	failure_rate = 'null'


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

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + capacitance + ";" +  tolerance + ";" + voltage_rated + ";" + typee + ";" + esr_ + ";" + operating_temperature + ";" + life_time_temperature + ";" + mounting_type + ";" + package_case + ";" + size_dimension + ";" + height_seated + ";" + lead_spacing + ";" + manufacturer_size_code + ";" + ratings + ";" + features + ";" + failure_rate + "\n")
    
    print(page)

f.close()
