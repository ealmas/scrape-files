import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from time import sleep
from random import randint

pages = [str(i) for i in range(1,684)]

filename = "oscillators_digikey.csv"
f = open(filename, "w")

for page in pages:

    # Make a get request
    my_url = 'https://www.digikey.com/products/en/crystals-oscillators-resonators/oscillators/172?FV=ffe000ac&quantity=0&ColumnSort=0&pageSize=500&page=' + page
    res = requests.get(my_url)
        
    # Pause the loop
    sleep(randint(20,40))

    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]

    part_numbers = df["Manufacturer Part Number"].tolist()
    manufacturer = df["Manufacturer"].tolist()

    print(part_numbers)
    print(manufacturer)
    print(page)
    df.to_csv(filename, encoding='utf-8', mode='a', index=False)
f.close()
