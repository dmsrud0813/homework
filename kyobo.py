import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://digital.kyobobook.co.kr/digital/publicview/publicViewNew.ink?tabType=SAM&tabSrnb=18',
                    headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

# listContent > div:nth-child(2) > ul:nth-child(1)
soup = BeautifulSoup(data.text, 'html.parser')
books = soup.select('#listContent > div > ul > li')
# print(books)

# listContent > div:nth-child(2) > ul:nth-child(4) > li:nth-child(5) > div.pic_area
# listContent > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > div.cont_area > div.title > strong
for book in books:
    title_tag = book.select_one('li> div > div.title').text
    publisher_tag = book.select_one('li> div > div.info1 > span.n2').text

    title = re.sub('&nbsp; | &nbsp;| \n | \t | \r|\n','', title_tag)
    publisher = re.sub('&nbsp; | &nbsp;| \n | \t | \r|\n','', publisher_tag)
    print(title + '~'+publisher)