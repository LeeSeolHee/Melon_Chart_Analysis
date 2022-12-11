
# Melon_Chart_Analysis
## 멜론 차트 분석 프로젝트

---
### 프로젝트 주제
> 제가 정한 프로젝트 주제는
‘연도별 장르 분석＇입니다. 
크롤링이 가능한 melon 사이트를 기반으로 시대별 차트와 현재 TOP100 차트 데이터를 가져옵니다. 2005년부터 2022년까지 대중들에게 선택받은 음악 트렌드를 살펴보며 그동안의 변화를 알아보았습니다.

### 주요 설명
---
1. **크롤링** : 멜론차트에서 시대별 차트와 TOP100 차트를 가져옵니다. 시대별 차트는 2005~2020까지 5년 단위로 가져오고, TOP100 차트는 현재 2022년 데이터를 가져옵니다. 모든 데이터는 1위부터 50위까지만 가져옵니다.<br>
2. **시각화** : matplotlib 라이브러리를 이용하여 그래프와 파이 차트를 그립니다. 그리고 텍스트 빈도 수 확인을 위한 워드 클라우드를 사용하여 보기 쉽게 표현했습니다. <br>


### 진행 상황
---
1. **데이터 수집**
    + BeautifulSoup, requests를 통하여 노래 목록을 받습니다.
    + chrome에서 개발자 도구(F12)를 사용해 HTML 요소를 확인하여 원한는 정보를 가져옵니다.
    + 노래 목록은 제목과 가수명이 있습니다. 더 나아가 장르, 발매일을 가져오기 위해 songid 값을 받아 url에 접속합니다.<br><br>
   [멜론 차트 연도별 데이터 크롤링 (2005~2020)](https://github.com/LeeSeolHee/Melon_Chart_Analysis/blob/master/crawling_by_year.py)<br>
   [멜론 차트 TOP100 데이터 크롤링 (2022)](https://github.com/LeeSeolHee/Melon_Chart_Analysis/blob/master/crawling_top_100.py)<br><br>
2. **데이터 전처리**
    + 크롤링 때 장르 부분에 추출 이상 발견
    ```
    if song_genre == 'R&amp;B/Soul':
            song_genre = 'R&B/Soul'
    ```
    + 장르 컬럼 값 조건 변경
    ```
    df.loc[df['장르'] == '발라드, 국내드라마', '장르'] = '발라드'
    df.loc[df['장르'] == '발라드, 인디음악', '장르'] = '발라드'
    df.loc[df['장르'] == '록/메탈, 국내드라마', '장르'] = '록/메탈'
    ```
    + 장르 컬럼 값 공백 제거
    ```
    df["가수"] = df["가수"].str.replace(" ", "")
    ```
    + 컬럼 값 -> 한 문장(str)으로 변환
    ```
    text = ' '.join(v for v in df['가수'])
    text = re.sub(pattern=pattern, repl='', string=text)
    ```
3. **시각화 처리**
    + 한글 폰트 설정 : from matplotlib import font_manager, rc
    + 사용한 시각화 방법 : bar, pie, word cloud<br><br>
    [연도별 장르 변화, 2005vs2022 장르 비교](https://github.com/LeeSeolHee/Melon_Chart_Analysis/blob/master/genre_comparison.py)<br>
    [연도별 인기 가수 변화](https://github.com/LeeSeolHee/Melon_Chart_Analysis/blob/master/Singer_frequency.py)<br>
   


