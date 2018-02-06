import urllib.request
import datetime
import json

access_key = "zKXKKnSlFbzQlSo3VGM7RSWUTndjwM0szSJhbK%2F85hKnvtPxU6zBzaudnzPFNNHf5j1azPl%2B7p4IfYMW8%2Bi4lg%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL request Success" %datetime.datetime.now())
            return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None

def getEdrcntTourismStatsService(yyyymm,nat_Cd,ed_Cd):
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters ="?_type=json&serviceKey="+access_key
    parameters+="&YM="+yyyymm
    parameters+="&NAT_CD="+nat_Cd
    parameters+="&ED_CD="+ed_Cd

    url = end_point+parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    jsonResult = []

    natCd = "115" + str(1)
    edCd = 'E'

    nStartYear = 2011
    nEndYear = 2017

    for year in range(nStartYear,nEndYear):
        for month in range(1,13):
            yyyymm = "{0}{1:0>2}".format(str(year),str(month))
            jsonData = getEdrcntTourismStatsService(yyyymm,natCd,edCd)

            try:
                if(jsonData['response']['header']['resultMsg']=='OK'):
                    krName = jsonData['response']['body']['items']['item']["natKorNm"]
                    krName = krName.replace(' ','')
                    iTotalVisit = jsonData['response']['body']['items']['item']["num"]
                    print('%s_%s:%s'%(krName,yyyymm,iTotalVisit))
                    jsonResult.append({'nat_cd':natCd,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})
            except TypeError:pass
            cnVisit = []
            VisitYM = []
            index = []

            i = 0
            for item in jsonResult:
                index.append(i)
                cnVisit.append(item['visit_cnt'])
                VisitYM.append(item['yyyymm'])
                i = i + 1

    try:
        with open('%s(%s)_해외방문객정보_%d_%d.json'%(krName,natCd,nStartYear,nEndYear-1),'w',encoding='UTF8') as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
            print('%s(%s)_해외방문객정보_%d_%d.json SAVED'%(krName,natCd,nStartYear,nEndYear-1))
    except UnboundLocalError:pass
if __name__ == '__main__':
    main()