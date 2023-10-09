import requests

url = 'http://randomuser.me/api/'

respuesta = requests.get(url)

if respuesta.status_code == 200:
    print(respuesta.json())
else:
    print('Algo ha ido mal')
    print('Código de error:', respuesta.status_code)
    print(respuesta.reason)
