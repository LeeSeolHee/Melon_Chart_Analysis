import csv
import re
import requests
from bs4 import BeautifulSoup
from time import sleep
 
 
# 2005년대 노래 시대별차트
# https://www.melon.com/chart/age/list.htm?idx=1&chartType=YE&chartGenre=POP&chartDate=2005&moved=Y
headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
}

# 멜론 시대별차트
age_url = "https://www.melon.com/chart/age/list.htm"

# 5년 간격으로 검색하기 위한 연도 리스트
year = ["2005","2010","2015","2020"]

for j in range(4):    
    params = {
        'idx': '1',
        'chartType': 'YE',     # 10년 단위로 검색하는 부분과 연관
        'chartGenre': 'KPOP',  # 가요검색: KPOP
        'chartDate': year[j],   # 검색연도
        'moved': 'Y',
    }
    
    response = requests.get(age_url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_list = soup.select('.lst50') # 50위까지
    melonlist = []

    for i, meta in enumerate(song_list,1):
        ### 순위, 제목
        rank = i
        try:
            title = meta.select('a[href*=playSong]')[0].text
        except:
            title = meta.select('.wrap_song_info .ellipsis')[0].text
        title = title.strip()
        print(str(params['chartDate'])+'년')
        print(str(rank )+ '위. ', title)
    
    
        # 노래 데이터 url의 html 추출
        song_id_html = str(meta.select('a[onclick*=SongDetail]'))
        matched = re.search(r"\'(\d+)\'", song_id_html)
        song_id = matched.group(1)
        front_url = 'https://www.melon.com/song/detail.htm?songId='
        song_url = front_url + song_id
    
    
        ### 가수, 앨범명, 발매날짜, 장르
        response = requests.get(song_url, params=params, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        singer_html = soup.select('.wrap_info .artist a')
    
        ### 가수
        singer_s = []
        if len(singer_html) != 0:
            for html in singer_html:
                singer_s.append(html['title'])
        else:
            # url 없는 Various Artists용
            singer_html = str(soup.select('.wrap_info .artist')[0])
            singer_html = singer_html.replace('\t','').replace('\r','').split('\n')
            singer_html = ''.join(singer_html)
            matched = re.search(r">(.*)<", singer_html)
            singer_s.append(matched.group(1))
    
        # 가수가 여러명일 때 하나의 string으로 표현
        singer_s = ', '.join(singer_s)
    
    
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
        # 장르 추출 부분에 문자열 수정
        if song_genre == 'R&amp;B/Soul':
            song_genre = 'R&B/Soul'
    
        print("가수:", singer_s)
        print("곡명:", title)
        print("앨범명:", album_name)
        print("발매날짜:", song_date)
        print("장르:", song_genre)
        
        # 리스트에 내용 추가
        temp = []
        temp.append(rank)
        temp.append(song_date)
        temp.append(title)
        temp.append(album_name)
        temp.append(singer_s)
        temp.append(song_genre)
        melonlist.append(temp) # 리스트에 한줄씩 내용 추가
    
        sleep(1)
        
    # csv 파일 생성    
    with open(year[j]+'melon50.csv', 'w', encoding='cp949', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['순위','발매일','곡명','앨범명','가수','장르'])
        writer.writerows(melonlist)
    
    
        
    