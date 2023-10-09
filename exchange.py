import requests

apikey = 'D7DF9194-3BC1-46B3-B0B3-BB90F1FAF25E'
server = 'https://rest.coinapi.io'
endpoint = '/v1/exchangerate'
headers = {
    'X-CoinAPI-Key': apikey
}


"""
1. Pedir moneda de origen: BTC
2. Pedir moneda destino: EUR
3. IR a la API y preguntar el valor de cambio

    {
    "time": "2017-08-09T14:31:18.3150000Z",
    "asset_id_base": "BTC",
    "asset_id_quote": "USD",
    "rate": 3260.3514321215056208129867667
    }
3.1 si hay error, mostrar mensaje

4. Recoger el dato
5. Mostrar un mensaje: 'Un BTC vale lo mismo que 30000 EUR'
6. Pregunta: ¿Quieres consultar de nuevo? (s/n)
"""

seguir = 's'
while seguir == 's':
    origen = input('¿Qué moneda quieres cambiar? ')
    destino = input('¿Qué moneda deseas obtener? ')

    url = server + endpoint + '/' + origen + '/' + destino
    # url = f'{server}{endpoint}/{origen}/{destino}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # respuesta OK
        exchange = response.json()
        rate = exchange['rate']
        print(f'Un {origen} vale lo mismo que {rate} {destino}')
    else:
        print('Error', response.status_code, ':', response.reason)

    seguir = ''
    while seguir.lower() not in ('s', 'n'):
        seguir = input('¿Quieres consultar de nuevo? (s/n) ')
