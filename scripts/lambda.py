import json
from github import Github
import boto3
from datetime import datetime
import requests

GET_ALPHA_URL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={aplha_key}'

ssm = boto3.client('ssm', region_name='us-east-1')
alphavantage = ssm.get_parameter(Name="/simple-stock-tracer/alphavantage", WithDecryption=True)['Parameter']['Value']
github_token = ssm.get_parameter(Name="/simple-stock-tracer/access_token", WithDecryption=True)['Parameter']['Value']

def lambda_handler(event, context):
    all_stocks = ist_custom = ssm.get_parameter(Name="/simple-stock-tracer/stocks")['Parameter']['Value']
    all_stock_indexes = all_stocks.split(',')

    stock_prices = dict()
    for stock in all_stock_indexes:
        stock_price = getStockPrice(stock)
        stock_prices[stock] = stock_price

    create_stock_file_in_github(stock_prices)


def getStockPrice(stock):
    url = GET_ALPHA_URL.format(symbol=stock, aplha_key=alphavantage)
    response = requests.get(url)
    return response.json()['Global Quote']['05. price']

def create_stock_file_in_github(stock_prices):
    filename = '{}.txt'.format(datetime.now())
    file_content = ""
    for symbol in stock_prices:
        file_content += symbol + "=" + stock_prices[symbol] + "\n"
    
    # github upload
    github = Github(github_token)
    repo = github.get_user().get_repo('simple-stock-tracer')
    location = 'data/{}'.format(filename)
    repo.create_file(location, filename, file_content, branch="main")