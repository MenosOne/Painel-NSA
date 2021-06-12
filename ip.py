import requests
def ipConsu(ip):
    jso = requests.get(f'http://ip-api.com/json/{ip}').json()
    return jso

ip = str(input("ip: "))
json = ipConsu(ip)
print(f'''
Ip: {json['query']}
Estatus: {json['status']}
País: {json['country']}
Cpdigo do País: {json['countryCode']}
Estado: {json['region']}
Nome da Ragião: {json['regionName']}
Cidade: {json['city']}
zip...?: {json['zip']}
Latitude: {json['lat']}
Lontitude: {json['lon']}
TimeZone: {json['timezone']}
Isp: {json['isp']}
Organização: {json['org']}
As: {json['as']}
''')


