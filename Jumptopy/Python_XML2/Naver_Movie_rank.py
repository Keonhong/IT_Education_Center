import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

result = []
max_rank = 1

for movie in range(max_rank):
    html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    soup = BeautifulSoup(html,'html.parser')

    div_tags = soup.findAll('div', attrs={'class':'tit3'})
    print(div_tags)
    # print("End")
    if(div_tags):
        for tag in div_tags:
            div_tag = list(tag.strings)
            if(div_tag[1].count('순위')==0):
                movie_title = div_tag[1]
                # movie_fluctuation = div_tag[1]
                result.append([movie_title])

movie_table = DataFrame(result, columns=('title'))
movie_table.to_csv("Naver_movie_rank.csv",encoding="cp949",mode='w',index=False)

# count = 1
# for m in tags:
#     title = m.find('a')
# print (count, '순위:', re.search('title=".+"', str(title)).group()[7:-1])
# count += 1