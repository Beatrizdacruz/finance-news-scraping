import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def scrapDataFinanceNews():
    site = requests.get("https://financenews.com.br").content
    soup = BeautifulSoup(site, 'html.parser')
    manchetes = soup.select("div.manchete.manchete3.light > h3 > a")
    data = []
    current_date = datetime.now()
    for result in manchetes:
        data.append({'notice':result.text, 'link': result.get('href'), 'date': current_date.strftime("%d/%m/%Y")})
    
    df = pd.DataFrame(data=data)
    print(data)
    df.to_csv('financeMainNews.csv')

    return data
   