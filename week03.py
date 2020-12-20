import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
base_url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200713&hh=20&rtm=N&pg='
page_num = 1

for i in range(4) :
    new_url = base_url+str(page_num)
    data = requests.get(new_url, headers = headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    page_num = page_num + 1

    music_chart = soup.select('div.newest-list > div > table > tbody > tr')

    for music in music_chart :
        title = music.select_one('td.info> a').text.strip()
        rank = music.select_one('td.number').text[0:3].strip()
        artist = music.select_one('td.info > a.artist').text.strip()
        print(rank, title, artist)

        doc = {
            'rank': rank,
            'title': title,
            'artist': artist
        }
        db.music.insert_one(doc)
