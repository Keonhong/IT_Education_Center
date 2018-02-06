import urllib.request
import time
import json
import datetime
import os

# access_key = "zKXKKnSlFbzQlSo3VGM7RSWUTndjwM0szSJhbK%2F85hKnvtPxU6zBzaudnzPFNNHf5j1azPl%2B7p4IfYMW8%2Bi4lg%3D%3D"
#
# def get_request_url(url):
#     req = urllib.request.Request(url)
#     try:
#         response = urllib.request.urlopen(req)
#         if response.getcode() == 200:
#             print("[%s] URL request Success" %datetime.datetime.now())
#             return response.read().decode('UTF-8')
#     except Exception as e:
#         print(e)
#         print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
#         return None
#
# def getForecastTimeDataResponse(base_date,base_time,nx,ny):
#     end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
#     parameters = "?base_date=" + base_date
#     parameters += "&base_time=" + base_time
#     parameters += "&nx=" + nx
#     parameters += "&ny=" + ny
#     parameters += "&_type=json&serviceKey=" + access_key + "&pageNo=1"
#
#     url = end_point+parameters
#
#     retData = get_request_url(url)
#
#     if(retData == None):
#         return None
#     else:
#         return json.loads(retData)
#
# def main():
#     jsonResult = []
#     base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
#     base_time = time.strftime("%H%M", time.localtime(time.time()))
#     nx = "89"
#     ny = "91"
#     base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
#     base_time = time.strftime("%H%M", time.localtime(time.time()))
#     base_Time = int(base_time) - 200
#     jsonData = getForecastTimeDataResponse(base_date,str(base_Time),nx,ny)
#
#
#     if (jsonData['response']['header']['resultMsg'] == 'OK'):
#         for i in (jsonData['response']['body']['items']['item']):
#                 jsonResult.append({'baseDate':i['baseDate'],'baseTime':i['baseTime'],'category':i["category"],'fcstDate':i['fcstDate'],'fcstTime':i['fcstTime'],'fcstValue':i['fcstValue'],'nx':i['nx'],'ny':i['ny']})
#
#         print("%s_%s_Weather.json" %(base_date,base_Time))
#
#         with open("%s_%s_Weather.json" %(base_date,base_Time),'w',encoding='utf8')as outfile:
#             retJson = json.dumps(jsonResult, indent=4, sort_keys=True,ensure_ascii=False)
#             outfile.write(retJson)
g_humidifier = False
def Dry_forecast_simulation():
    global g_humidifier
    base_date = time.strftime("%Y%m%d", time.localtime(time.time()))
    base_time = time.strftime("%H%M", time.localtime(time.time()))
    base_Time = int(base_time)-200
    retJson = []

    with open("20180201_1524_Weather.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        retJson = json.loads(json_string)

    for retJson in retJson:
        if(retJson['category']) == 'REH':
            print("REH//fcstValue = " + str(retJson['fcstValue']))
            if retJson['fcstValue'] < 40:
                if g_humidifier == False:
                    print("\n***습도가 낮으므로 가습기를 가동하겠습니다.***")
                    g_humidifier = not g_humidifier
                elif g_humidifier == True:
                    print("***습도가 낮으므로 가습기가 작동중입니다.***")
if Dry_forecast_simulation() == '__main__()':
    Dry_forecast_simulation()