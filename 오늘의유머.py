# coding:utf-8
from bs4 import BeautifulSoup
#웹서버와 통신(requests) 
import urllib.request
#정규표현식(검색)
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\Today.txt", "wt", encoding="utf-8")
for n in range(1, 11):
        #오늘의 유머
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        #2500줄 문자열 변수 저장
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        #<td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;">기침 후 목에서 쇳덩이가 나온 남성</a><span class="list_memo_count_span"> [22]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>

        for item in list:
                try:
                        title = item.find("a").text.strip()  
                        #print(title)
                        if (re.search('한국', title)):
                                print(title)
                                f.write(title + "\n")
                except:
                        pass
        
f.close() 
