print("start")
import urllib.request
from pandas import DataFrame
import os

result=[]

if not os.path.isdir('V4_BigData'):
    os.mkdir('V4_BigData')

import xml.etree.ElementTree  as ET  # xml모듈을 가져오면서 xml.etree.ElementTree를 ET라는 새 이름으로 지정

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
# response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)#as ET가 없었다면 xml.etree.ElementTree.fromstring(..)으로
#했었어야 했음. 그마저도 변수 xml때문에 문제가 생김
file_num = 1
folder_num = 1
Div_Column=100
for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

Column_Count=len(root.findall('item'))

cnt=0
j=1
while 1:
    try:
        os.chdir("D:\Python_workspace\jump_to_python\Crawling\\01_10\V4_BigData")
        # os.chdir("D:\\1\pycharm\python_jaryo\Crawling\\01_10\\V4_BigData")
        if not os.path.isdir('Nene_Data%d' % folder_num):
            os.mkdir('Nene_Data%d' % folder_num)
            break
    except:#파일을 못찾으면~? 못 찾아서 찡찡~ 나 에러예요~ 응 아니야
        folder_name = 'D:\Python_workspace\jump_to_python\Crawling\\01_10\V4_BigData\\Nene_Data' + str(folder_num)+'\\'
        # folder_name = 'D:\\1\pycharm\python_jaryo\Crawling\\01_10\\V4_BigData\\Nene_Data' + str(folder_num) + '\\'
        break
    else:#파일이 있네?
        folder_num += 1
        continue

for i in range(Column_Count):
    folder_name = 'D:\Python_workspace\jump_to_python\Crawling\\01_10\V4_BigData\\Nene_Data' + str(folder_num) + '\\'
    # folder_name = 'D:\\1\pycharm\python_jaryo\Crawling\\01_10\\V4_BigData\\Nene_Data' + str(folder_num) + '\\'
    file_name = 'Nene' + str(file_num) + '.csv'
    if cnt == Div_Column:
        nene_table = DataFrame(result[Div_Column*(j-1):Div_Column*j], columns=('store', 'sido', 'gungu', 'store_address'))
        nene_table.to_csv(folder_name + file_name, encoding="cp949", mode='w', index=True)
        j += 1
        file_num+=1
        cnt=0
    elif i == Column_Count-1:#100개가 되지 않는 꼬다리(마지막)
        print(Div_Column*(j-1))
        nene_table = DataFrame(result[Div_Column * (j - 1): ],columns=('store', 'sido', 'gungu', 'store_address'))
        nene_table.to_csv(folder_name + file_name, encoding="cp949", mode='w', index=True)
    cnt+=1

print("End")