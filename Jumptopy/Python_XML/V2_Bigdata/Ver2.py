import urllib.request
from pandas import DataFrame
import xml.etree.ElementTree as ET
import os

def Make_Nene(index):
    nene="Nene"
    data="_data"
    os.system("mkdir "+nene+data+index)
    return None

def make_nene(Index):
    nene ="nene"
    csv =".csv"
    nene_table.to_csv(nene + Index + csv, encoding="cp949", mode='w', index=True)
    return None

result = []

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

try :
    with open("Nene1_index.txt", 'r') as file:
        index = file.readline()
        Make_Nene(index)
        index = int(index)
        index += 1
        index = str(index)
    with open("Nene1_index.txt", 'w') as file:
        file.write(index)
except FileNotFoundError :
    with open("Nene1_index.txt", 'w') as file:
        file.write('2')
        Make_Nene('1')

try :
    with open("nene_index.txt", 'r') as file:
        Index = file.readline()
        make_nene(Index)
        Index = int(Index)
        Index += 1
        Index = str(Index)
    with open("nene_index.txt", 'w') as file:
        file.write(Index)
except FileNotFoundError:
    with open("nene_index.txt", 'w') as file:
        file.write('2')
        make_nene('1')

print("End")