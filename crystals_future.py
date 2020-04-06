import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from time import sleep
from random import randint

pages = [str(i) for i in range(0,69)]

filename = "crystals_future.csv"
f = open(filename, "w")

for page in pages:

    url = 'https://www.futureelectronics.com/c/electromechanical/timing-devices--crystals/products?q=%3Arelevance&text=&pageSize=100&page=' + page
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url,headers=headers)
    html = response.content

    sleep(randint(30,50))

    soup = BeautifulSoup(response.content,'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))[0]

    print(page)
    df.to_csv(filename, encoding='utf-8', mode='a', index=False)

f.close()