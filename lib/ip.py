import requests
def ipConsu(ip):
    jso = requests.get(f'http://ip-api.com/json/{ip}').json()
    return jso


