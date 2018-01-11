#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"  # delimiter='구분자'
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 3

def make_dir(index):
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))
    return None

def make_nene(dir_index, file_index):
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + str(file_index) + csv
    nene_table.to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu =element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

for i in range(1174):
    if i % 100 == 0:
        print(i)


try: os.mkdir(dir_name)
except: pass
try:
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file:
        file_index = file.readline()               # text의 값을 읽고
        file_index = int(file_index)               # 그 값을 int로 전환(연산을 위해)
        dir_index = int(file_index / record_limit) # text의 값과 recode_limit의 값을 나눔
        if file_index % record_limit != 0:         # 나누는 값이 0이 아닐 때
            dir_index = dir_index+1                # 1 증가시켜줌
        if file_index % record_limit == 1:         # 나누는 값이 1일 때
            make_dir(dir_index)                    # 3개씩 들어가고 나머지는 다음폴더에 저장

        make_nene(dir_index, file_index)
        file_index += 1
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file:
        file.write(str(file_index))
except FileNotFoundError:
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file:
        file.write('2')
    make_dir(1)
    make_nene(1, 1)
print("End")