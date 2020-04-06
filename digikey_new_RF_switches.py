import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import io
from time import sleep
from random import randint

pages = [str(i) for i in range(1,16)]

filename = "digikey_RF_switches.csv"
f = open(filename, "w", encoding="utf-8")
header = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; packaging; series; status; rf_type; Topology; Circuit; frequency_range; Isolation; Insertion_Loss; Test_Frequency; P1dB; IIP3; features; Impedance; Voltage_Supply; Operating_Temperature; Package_Case; Supplier_Device_Package\n"
for page in pages:

    my_url = 'https://www.digikey.com/products/en/rf-if-and-rfid/rf-switches/865?FV=ffe00361&quantity=0&ColumnSort=0&pageSize=500&page=1' + page
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

	    rf_fmly = container.find_all("td",{"class":"CLS 236 ptable-param"})
	    try:
	    	rf_type = rf_fmly[0].text.strip()
	    except IndexError:
	    	rf_type = 'null'

	    frqny_grp = container.find_all("td",{"class":"CLS 1098 ptable-param"})
	    try:
	    	topology = frqny_grp[0].text.strip()
	    except IndexError:
	    	topology = 'null'

	    frq = container.find_all("td",{"class":"CLS 130 ptable-param"})
	    try:
	    	circuit = frq[0].text.strip()
	    except IndexError:
	    	circuit = 'null'

	    frqncy_rng = container.find_all("td",{"class":"CLS 344 ptable-param"})
	    try:
	    	frequency_range = frqncy_rng[0].text.strip()
	    except IndexError:
	    	frequency_range = 'null'

	    typee = container.find_all("td",{"class":"CLS 1165 ptable-param"})
	    try:
	    	isolation = typee[0].text.strip()
	    except IndexError:
	    	isolation = 'null'

	    brands = container.find_all("td",{"class":"CLS 327 ptable-param"})
	    try:
	    	insertion_loss = brands[0].text.strip()
	    except IndexError:
	    	insertion_loss = 'null'

	    vsr = container.find_all("td",{"class":"CLS 1110 ptable-param"})
	    try:
	    	test_frequency = vsr[0].text.strip()
	    except IndexError:
	    	test_frequency = 'null'

	    rtrn_lss = container.find_all("td",{"class":"CLS 1109 ptable-param"})
	    try:
	    	P1dB = rtrn_lss[0].text.strip()
	    except IndexError:
	    	P1dB = 'null'

	    gn = container.find_all("td",{"class":"CLS 1670 ptable-param"})
	    try:
	    	ipp3 = gn[0].text.strip()
	    except IndexError:
	    	ipp3 = 'null'

	    ftrs = container.find_all("td",{"class":"CLS 5 ptable-param"})
	    try:
	    	features = ftrs[0].text.strip()
	    except IndexError:
	    	features = 'null'

	    trmntn = container.find_all("td",{"class":"CLS 60 ptable-param"})
	    try:
	    	impedance = trmntn[0].text.strip()
	    except IndexError:
	    	impedance = 'null'

	    ingrss = container.find_all("td",{"class":"CLS 276 ptable-param"})
	    try:
	    	voltage_supply = ingrss[0].text.strip()
	    except IndexError:
	    	voltage_supply = 'null'

	    mntn = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = mntn[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    hght = container.find_all("td",{"class":"CLS 16 ptable-param"})
	    try:
	    	package_case = hght[0].text.strip()
	    except IndexError:
	    	package_case = 'null'

	    app = container.find_all("td",{"class":"CLS 1291 ptable-param"})
	    try:
	    	supplier_device_package = app[0].text.strip()
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

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + rf_type + ";" +  topology + ";" + circuit + ";" + frequency_range + ";" + isolation + ";" + insertion_loss + ";" + test_frequency + ";" + P1dB + ";" + ipp3 + ";" + features + ";" + impedance + ";" + voltage_supply + ";" + operating_temperature + ";" + package_case + ";" + supplier_device_package + "\n")
    
    print(page)

f.close()
