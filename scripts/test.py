import requests
from bs4 import BeautifulSoup

def get_amazon_price():
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={key}"
    res = requests.get(url)
    data = res.json()

    return data

print(get_amazon_price())