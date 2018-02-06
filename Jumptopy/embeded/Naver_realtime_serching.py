# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get('https://www.naver.com/').text
# soup = BeautifulSoup(html, 'html.parser')
#
# title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
#
# for idx, title in enumerate(title_list, 1):
#     print("{}{} {}".format(idx, '위', title.text))

import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.melon.com/chart/index.htm').text
soup = BeautifulSoup(html, 'html.parser')

print(html)
tag_list = soup.select('wrap_tabmenu01')

for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text)


