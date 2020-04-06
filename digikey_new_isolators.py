import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,11)]

filename = "digikey_modular_isolators.csv"
f = open(filename, "w", encoding="utf-8" )

header = "mfg_partnumber: unit_price: manufacturer: description: qty_available: min_qty: packaging: series: status: Technology: Type: IsolatedPower: NumberofChannels: InputsSide: ChannelType: VoltageIsolation: CommonMode: DataRate: PropagationDelay: PulseWidth: RiseFall: VoltageSupply: OperatingTemperature: MountingType: PackageCase: SupplierDevicePackage\n"

for page in pages:

    my_url = 'https://www.digikey.com/products/en/isolators/digital-isolators/901?FV=ffe00385&quantity=0&ColumnSort=0&k=isolator&pageSize=500&page=' + page
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

	    typ = container.find_all("td",{"CLS 570 ptable-param"})
	    try:
	    	technology = typ[0].text.strip()
	    except IndexError:
	    	technology = 'null'

	    typ2 = container.find_all("td",{"class":"CLS 183 ptable-param"})
	    try:
	    	typee_ = typ2[0].text.strip()
	    except IndexError:
	    	typee_ = 'null'

	    mtrl = container.find_all("td",{"class":"CLS 1761 ptable-param"})
	    try:
	    	isolated_power = mtrl[0].text.strip()
	    except IndexError:
	    	isolated_power = 'null'

	    indctnc = container.find_all("td",{"class":"CLS 2093 ptable-param"})
	    try:
	    	number_of_channels = indctnc[0].text.strip()
	    except IndexError:
	    	number_of_channels = 'null'

	    rtng = container.find_all("td",{"class":"CLS 1290 ptable-param"})
	    try:
	    	inputs_side = rtng[0].text.strip()
	    except IndexError:
	    	inputs_side = 'null'

	    strtn = container.find_all("td",{"class":"CLS 1762 ptable-param"})
	    try:
	    	channel_type = strtn[0].text.strip()
	    except IndexError:
	    	channel_type = 'null'

	    shldng = container.find_all("td",{"class":"CLS 597 ptable-param"})
	    try:
	    	voltage_isolation = shldng[0].text.strip()
	    except IndexError:
	    	voltage_isolation = 'null'

	    rt = container.find_all("td",{"class":"CLS 1748 ptable-param"})
	    try:
	    	common_mode = rt[0].text.strip()
	    except IndexError:
	    	common_mode = 'null'

	    rstnc = container.find_all("td",{"class":"CLS 448 ptable-param"})
	    try:
	    	data_rate = rstnc[0].text.strip()
	    except IndexError:
	    	data_rate = 'null'

	    tmpr = container.find_all("td",{"class":"CLS 1749 ptable-param"})
	    try:
	    	propagation_delay = tmpr[0].text.strip()
	    except IndexError:
	    	propagation_delay = 'null'

	    frq = container.find_all("td",{"class":"CLS 1763 ptable-param"})
	    try:
	    	pulse_width = frq[0].text.strip()
	    except IndexError:
	    	pulse_width = 'null'

	    size = container.find_all("td",{"class":"CLS 1745 ptable-param"})
	    try:
	    	rise_fall = size[0].text.strip()
	    except IndexError:
	    	rise_fall = 'null'

	    mntg = container.find_all("td",{"class":"CLS 276 ptable-param"})
	    try:
	    	voltage_supply = mntg[0].text.strip()
	    except IndexError:
	    	voltage_supply = 'null'

	    pck = container.find_all("td",{"class":"CLS 252 ptable-param"})
	    try:
	    	operating_temperature = pck[0].text.strip()
	    except IndexError:
	    	operating_temperature = 'null'

	    spl_pck = container.find_all("td",{"class":"CLS 69 ptable-param"})
	    try:
	    	mounting_type = spl_pck[0].text.strip()
	    except IndexError:
	    	mounting_type = 'null'

	    spl_pck2 = container.find_all("td",{"class":"CLS 16 ptable-param"})
	    try:
	    	package_case = spl_pck2[0].text.strip()
	    except IndexError:
	    	package_case = 'null'

	    spl_pck3 = container.find_all("td",{"class":"CLS 1291 ptable-param"})
	    try:
	    	supplier_device = spl_pck3[0].text.strip()
	    except IndexError:
	    	supplier_device = 'null'


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

	    f.write(part_numbers + ":" + price + ":" + manufacturer + ":" + description + ":" + qty_available + ":" + min_qty + ":" + packaging + ":" + series + ":" + status + ":" + technology + ":" +  typee_ +  ":" + isolated_power + ":" + number_of_channels + ":" + inputs_side + ":" + channel_type + ":" + voltage_isolation + ":" + common_mode + ":" + data_rate + ":" + propagation_delay + ":" + pulse_width + ":" + rise_fall + ":" + voltage_supply + ":" + operating_temperature  + ":" + mounting_type + ":" + package_case + ":" + supplier_device + "\n")
    
    print(page)

f.close()
