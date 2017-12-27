sumSec=0    # 초의 총합을 저장할 변수
for hour in range(24) :     # 시간
    for minute in range(60) :   #분
        if '3' in str(hour) or '3' in str(minute) : # 시간이나 분에 3이 들어가면
            sumSec += 60            # 60초씩 더함
print(sumSec)

s = 0
for h in range(24):
    if "3" in str(h): s += (60*60)
    else:
        for m in range(60):
            if "3" in str(m): s += 60
print(s)