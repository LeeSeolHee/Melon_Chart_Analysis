import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# # 2005~2022 csv 파일 읽어오기
year = ["2005","2010","2015","2020","2022"]

for i in range(len(year)):
    path = 'C:/Users/LeeSeolHee/Desktop/빅데이터 프로젝트/'+ year[i] + 'melon50.csv'
    df = pd.read_csv(path, encoding='cp949')

  
    # DataFrame 컬럼 값 조건 변경
    df.loc[df['장르'] == '발라드, 국내드라마', '장르'] = '발라드'
    df.loc[df['장르'] == '발라드, 인디음악', '장르'] = '발라드'
    df.loc[df['장르'] == '록/메탈, 국내드라마', '장르'] = '록/메탈'
    print(df['장르'].value_counts(normalize=True))
    
    # 연도별 인기 있던 장르 비율
    ratio = df['장르'].value_counts(normalize=True)
    labels = ratio.index
    colors = ['#d9ae94', '#f1dca7', '#ffcb69', '#e8ac65', '#d08c60', '#b58463', '#997b66' ,'#ad9585']

    plt.pie(ratio, labels=labels, autopct='%.1f%%' , colors=colors)
    plt.title(year[i])
    plt.show()

# 2005년 VS 2022년의 장르 변화
path1 = 'C:/Users/LeeSeolHee/Desktop/빅데이터 프로젝트/2005melon50.csv'
df1 = pd.read_csv(path1, encoding='cp949')
path2 = 'C:/Users/LeeSeolHee/Desktop/빅데이터 프로젝트/2022melon50.csv'
df2 = pd.read_csv(path2, encoding='cp949')

# 장르의 중복값 이름 출력
print(df1['장르'].unique())
print(df2['장르'].unique())

# DataFrame 컬럼 값 조건 변경
df1.loc[df1['장르'] == '발라드, 국내드라마', '장르'] = '발라드'
df1.loc[df1['장르'] == '록/메탈, 국내드라마', '장르'] = '록/메탈'
df2.loc[df2['장르'] == '발라드, 국내드라마', '장르'] = '발라드'
df2.loc[df2['장르'] == '발라드, 인디음악', '장르'] = '발라드'
df2.loc[df2['장르'] == '인디음악, 포크/블루스', '장르'] = '록/메탈'
df2.loc[df2['장르'] == 'POP', '장르'] = 'R&B/Soul'

# # 연도별 인기 있던 장르 비율
print(df1['장르'].value_counts().sort_index(ascending=False))
print(df2['장르'].value_counts().sort_index(ascending=False))

genre = ['발라드', '록/메탈', '랩/힙합', '댄스', 'R&B/Soul']

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
plt.title("2005 VS 2022 장르 변화")
plt.bar(range(1, 14, 3), df1['장르'].value_counts().sort_index(ascending=False), label='2005', color='orange')
plt.bar(range(2, 15, 3), df2['장르'].value_counts().sort_index(ascending=False), label='2022', color='skyblue')
plt.xticks(range(1, 14, 3), genre)
plt.legend() #범례 나타내기
plt.show()
