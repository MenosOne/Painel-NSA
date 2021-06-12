import os

os.system('cls' if os.name == 'nt' else 'clear')
print('''                                             
 _   _ ____    _      ____   _    ___ _   _ _____ _     
| \ | / ___|  / \    |  _ \ / \  |_ _| \ | | ____| |    
|  \| \___ \ / _ \   | |_) / _ \  | ||  \| |  _| | |    
| |\  |___) / ___ \  |  __/ ___ \ | || |\  | |___| |___ 
|_| \_|____/_/   \_\ |_| /_/   \_|___|_| \_|_____|_____|
''')

from lib import ip

if __name__ == '__main__':
    while True:
        print('''
[1] consulta de ip
[2] sair
[?] vai ter mais coisas ksks
        ''')
        x = str(input('>>> ')).strip()
        if x not in "12":
            print('escreveu errado')
        else:
            if x == "1":
                os.system('clear');os.system('cls')
                aip = str(input('Ip a ser consultado: '))
                jsn = ip.ipConsu(aip)
                print(f'''
Ip: {jsn['query']}
Estatus: {jsn['status']}
País: {jsn['country']}
Código do País: {jsn['countryCode']}
Estado: {jsn['region']}
Nome da Ragião: {jsn['regionName']}
Cidade: {jsn['city']}
zip...?: {jsn['zip']}
Latitude: {jsn['lat']}
Lontitude: {jsn['lon']}
TimeZone: {jsn['timezone']}
Isp: {jsn['isp']}
Organização: {jsn['org']}
As: {jsn['as']}
                ''')
            if x == "2":
                exit()

