import requests

apikey = ''
server = 'https://rest.coinapi.io'
endpoint = '/v1/assets'

ur = server + endpoint
headers = {
    'X-coinAPI-Key': apikey
}

respuesta = requests.get(server, headers=headers)

if respuesta.status_code == 200:
    json_respuesta = respuesta.json()

    for coin in json_respuesta:
        id = coin.get('asset_id')
        if (id in ['BTC', 'USD', 'EUR', 'ETH']):
            print(id, '-', coin.get('name'), coin.get('type_is_crypto'))
else:
    print('Algo no ha ido bien. Error', respuesta.status_code, respuesta.reason)
