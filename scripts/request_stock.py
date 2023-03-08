import requests

content = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=XI74FW0PXR9KCD49')

response_body = content.json()
print(response_body)
print(response_body['Global Quote']['05. price'])
