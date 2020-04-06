import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import io
from time import sleep
from random import randint

pages = [str(i) for i in range(1,17)]

filename = "digikey_RF_antennas.csv"
f = open(filename, "w", encoding="utf-8")
header = "d_partnumber; mfg_partnumber; manufacturer; description; qty_available; unit_price; min_qty; packaging; series; status; rf_family; frequnecy_group; frequency; frequency_range; antenna_type; number_of_brands; vswr; return_loss; gain; power_max; features; termination; ingress_protection; mounting_type; height_seated; applications\n"
for page in pages:

    my_url = 'https://www.digikey.com/products/en/rf-if-and-rfid/rf-antennas/875?FV=ffe0036b&quantity=0&ColumnSort=0&pageSize=500&page=' + page
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

	    rf_fmly = container.find_all("td",{"class":"CLS 1883 ptable-param"})
	    try:
	    	rf_family = rf_fmly[0].text.strip()
	    except IndexError:
	    	rf_family = 'null'

	    frqny_grp = container.find_all("td",{"class":"CLS 1850 ptable-param"})
	    try:
	    	frequnecy_group = frqny_grp[0].text.strip()
	    except IndexError:
	    	frequnecy_group = 'null'

	    frq = container.find_all("td",{"class":"CLS 1851 ptable-param"})
	    try:
	    	freq = frq[0].text.strip()
	    except IndexError:
	    	freq = 'null'

	    frqncy_rng = container.find_all("td",{"class":"CLS 344 ptable-param"})
	    try:
	    	frequency_range = frqncy_rng[0].text.strip()
	    except IndexError:
	    	frequency_range = 'null'

	    typee = container.find_all("td",{"class":"CLS 965 ptable-param"})
	    try:
	    	antenna_type = typee[0].text.strip()
	    except IndexError:
	    	antenna_type = 'null'

	    brands = container.find_all("td",{"class":"CLS 963 ptable-param"})
	    try:
	    	number_of_brands = brands[0].text.strip()
	    except IndexError:
	    	number_of_brands = 'null'

	    vsr = container.find_all("td",{"class":"CLS 964 ptable-param"})
	    try:
	    	vswr = vsr[0].text.strip()
	    except IndexError:
	    	vswr = 'null'

	    rtrn_lss = container.find_all("td",{"class":"CLS 1166 ptable-param"})
	    try:
	    	return_loss = rtrn_lss[0].text.strip()
	    except IndexError:
	    	return_loss = 'null'

	    gn = container.find_all("td",{"class":"CLS 445 ptable-param"})
	    try:
	    	gain = gn[0].text.strip()
	    except IndexError:
	    	gain = 'null'

	    pwr = container.find_all("td",{"class":"CLS 2109 ptable-param"})
	    try:
	    	power_max = pwr[0].text.strip()
	    except IndexError:
	    	power_max = 'null'

	    ftrs = container.find_all("td",{"class":"CLS 5 ptable-param"})
	    try:
	    	features = ftrs[0].text.strip()
	    except IndexError:
	    	features = 'null'

	    trmntn = container.find_all("td",{"class":"CLS 589 ptable-param"})
	    try:
	    	termination = trmntn[0].text.strip()
	    except IndexError:
	    	termination = 'null'

	    ingrss = container.find_all("td",{"class":"CLS 697 ptable-param"})
	    try:
	    	ingress_protection = ingrss[0].text.strip()
	    except IndexError:
	    	ingress_protection = 'null'

	    mntn = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = mntn[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    hght = container.find_all("td",{"class":"CLS 966 ptable-param"})
	    try:
	    	height_seated = hght[0].text.strip()
	    except IndexError:
	    	height_seated = 'null'

	    app = container.find_all("td",{"class":"CLS 405 ptable-param"})
	    try:
	    	applications = app[0].text.strip()
	    except IndexError:
	    	applications = 'null'

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

	    f.write(part_numbers_d + ";" + part_numbers + ";" + manufacturer + ";" + description + ";" + qty_available + ";" + price + ";" + min_qty + ";" + packaging + ";" + series + ";" + status + ";" + rf_family + ";" +  frequnecy_group + ";" + freq + ";" + frequency_range + ";" + antenna_type + ";" + number_of_brands + ";" + vswr + ";" + return_loss + ";" + gain + ";" + power_max + ";" + termination + ";" + ingress_protection + ";" + mounting_type + ";" + height_seated + ";" + applications + "\n")
    
    print(page)

f.close()
