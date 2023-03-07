import requests
from bs4 import BeautifulSoup

def get_amazon_price():
    url = "https://finance.yahoo.com/quote/AMZN"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    return soup

print(get_amazon_price())