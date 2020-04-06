import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from time import sleep
from random import randint

pages = [i for i in range(0, 1564)]


filename = "mouser_oscillators_abracon.csv"
f = open(filename, "w")

for page in pages:

    url = 'https://www.mouser.com/ABRACON/Passive-Components/Frequency-Control-Timing-Devices/Oscillators/_/N-7jdfi?No=' + str(page * 25) +'&P=1z0znsm'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url,headers=headers)
    html = response.content

    sleep(randint(20,40))

    soup = BeautifulSoup(response.content,'lxml')
    table = soup.find_all('tbody')
    df = pd.read_html(str(table))[0]

    print(page)
    df.to_csv(filename, encoding='utf-8', mode='a', index=False)

f.close()