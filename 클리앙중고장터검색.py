# coding:utf-8
from bs4 import BeautifulSoup
#웹서버와 통신(requests) 
import urllib.request
#정규표현식(검색)
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\clien.txt", "wt", encoding="utf-8")
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        #2500줄 문자열 변수 저장
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="예약중 애플 에어팟 프로 Apple Airpods Pro 1세대 with 맥세이프 애캐플 23.11.27">
        # 	예약중 애플 에어팟 프로 Apple Airpods Pro 1세대 with 맥세이프 애캐플 23.11.27
        # </span>

        for item in list:
                try:
                        title = item.text.strip()
                        #print(title)
                        if (re.search('맥북', title)):
                                print(title)
                                f.write(title + "\n")
                except:
                        pass
        
f.close() 
