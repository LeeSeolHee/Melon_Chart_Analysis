import re
import requests
from bs4 import BeautifulSoup
import csv
 
headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
    }
 
# User-Agent가 없으면 사이트로 접근이 되지 않기 때문에 headers 입력
# 멜론차트 top-100
top100_url ="https://www.melon.com/chart/index.htm"
html = requests.get(top100_url, headers = headers)
soup = BeautifulSoup(html.text, "html.parser")
melonlist = []
rank = 1  # 순위

#playsong이 있는 a태그에 접근해서 songId 번호를 가져오기
for tag in soup.select('#tb_list a[href*=playSong]'):
    title = tag.text
    js = tag['href']
    matched = re.search(r",(\d+)",js)
    if matched:
        song_Id = matched.group(1)
        # 가져온 songId 번호로 앨범 상세정보 페이지에 접근
        song_url = 'https://www.melon.com/song/detail.htm?songId=' + song_Id 
        
        # 앨범명, 가수, 발매날짜, 장르는 들고온 url에서 추가 추출
        res = requests.get(song_url, headers=headers).text
        soup = BeautifulSoup(res, "html.parser")

        # 가수
        singer_html = str(soup.select('.artist span')[0])
        matched = re.search(r">(.*)<", singer_html)
        singer = matched.group(1)
        
        # 앨범명
        album_name_html = str(soup.select('.list dd')[0])
        matched = re.search(r">(.*)<", album_name_html)
        matched2 = re.search(r">(.*)<", matched.group(1))
        album_name = matched2.group(1).strip()

        # 발매날짜
        song_date_html = str(soup.select('.list dd')[1])
        matched = re.search(r">(.*)<", song_date_html)
        song_date = matched.group(1)

        # 장르
        song_genre_html = str(soup.select('.list dd')[2])
        matched = re.search(r">(.*)<", song_genre_html)
        song_genre = matched.group(1)
        
        print("가수:", singer)
        print("곡명:", title)
        print("앨범명:", album_name)
        print("발매날짜:", song_date)
        print("장르:", song_genre)
         # 장르 추출 부분에 문자열 수정
        if song_genre == 'R&amp;B/Soul':
            song_genre = 'R&B/Soul'
        
        # 리스트에 내용 추가
        temp = []
        temp.append(rank)
        temp.append(song_date)
        temp.append(title)
        temp.append(album_name)
        temp.append(singer)
        temp.append(song_genre)
        melonlist.append(temp) # 리스트에 한줄씩 내용 추가
        
        # 순위 50위까지 추출
        rank += 1
        if rank > 50:
            break

# csv 파일 생성    
with open('2022melon50.csv', 'w', encoding='CP949', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['순위','발매일','곡명','앨범명','가수','장르'])
    writer.writerows(melonlist)