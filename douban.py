import urllib.request
from bs4 import BeautifulSoup
import time
import random
absolute = "https://movie.douban.com/subject/26588308/comments"
i = 0


def get_data(html, i):
    i+=1
    print(i)
    soup=BeautifulSoup(html,'lxml')
    comment_list = soup.select('.comment > p')
    next_page = []
    next_page= soup.select('.next')[-1].get('href')
    return comment_list, next_page, i


headers = {
'Host':'movie.douban.com',
'Connection':' keep-alive',
'Upgrade-Insecure-Requests':' 1',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/63.0.3239.84 Safari/537.36',
'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://www.douban.com/',
'Accept-Language':' zh-CN,zh;q=0.9',
'Cookie':' ',} # Add cookie here.


comment_list = []
next_page = " "
while next_page != None :
    print(absolute + next_page)
    request = urllib.request.Request(url=absolute+next_page, headers=headers)
    html = urllib.request.urlopen(request).read().decode("UTF-8")
    comment_list, next_page, i = get_data(html,i)

    with open(u"comments.txt", 'a+', encoding='utf-8') as f:
        for l in comment_list:
            comment = l.get_text().strip().replace("\n", "")
            # print(comment)
            f.writelines(comment + u'\n')
    time.sleep(1 + float(random.randint(1, 50)) / 20)
