import requests

apikey = 'D7DF9194-3BC1-46B3-B0B3-BB90F1FAF25E'
server = 'https://rest.coinapi.io'
endpoint = '/v1/assets'

url = server + endpoint
headers = {
    'X-CoinAPI-Key': apikey
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    json_respuesta = respuesta.json()

    for coin in json_respuesta:
        id = coin.get('asset_id')
        if (id in ['BTC', 'USD', 'EUR', 'ETH']):
            print(id, '-', coin.get('name'), coin.get('type_is_crypto'))
else:
    print('Algo no ha ido bien. Error', respuesta.status_code, respuesta.reason)
