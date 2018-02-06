import json

with open('jtbcnews_facebook_2018-01-24_2018-01-25.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)

for data_info in data:
    count = 0
    print(data['data'][0]['shares']['count'])
    while True:
        if count < 24:
           count += 1
           print(data['data'][count]['shares']['count'])
           continue