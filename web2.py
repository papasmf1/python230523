# web2.py 
from bs4 import BeautifulSoup
import requests



url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#검색 조건 
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    print( f"{title} , {price}")

# 선택 블럭: ctrl + / 
# <div class="card-desc">
#       <h2 class="card-title">전원주택용 창고 팝니다</h2>
#       <div class="card-price ">
#         70,000원
#       </div>
#       <div class="card-region-name">
#         전북 전주시 덕진구 혁신동
#       </div>
