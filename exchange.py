import requests

apikey = 'D7DF9194-3BC1-46B3-B0B3-BB90F1FAF25E'
server = 'https://rest.coinapi.io'
endpoint = '/v1/exchangerate'
headers = {
    'X-CoinAPI-Key': apikey
}

seguir = 's'
while seguir == 's':
    origen = input('¿Qué moneda quieres cambiar? ')
    destino = input('¿Qué moneda deseas obtener? ')

    # url = server + endpoint + '/' + origen + '/' + destino
    url = f'{server}{endpoint}/{origen}/{destino}'

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        exchange = respuesta.json()
        rate = exchange['rate']
        print(f'Un {origen} vale lo mismo que {rate} {destino}')
    else:
        print('Error', respuesta.status_code, ':', respuesta.reason)

    seguir = ''
    while seguir.lower() not in ('s', 'n'):
        seguir = input('¿Quieres consultar de nuevo? (s/n) ')
