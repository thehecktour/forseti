import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
resultado = data["bpi"]["USD"]["rate"]