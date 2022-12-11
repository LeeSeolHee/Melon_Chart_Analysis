from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import re

# # 2005~2022 csv 파일 읽어오기
year = ["2005","2010","2015","2020","2022"]

for i in range(len(year)):
    path = 'C:/Users/LeeSeolHee/Desktop/빅데이터 프로젝트/'+ year[i] + 'melon50.csv'
    df = pd.read_csv(path, encoding='cp949')

    pattern = r'\([^)]*\)'

    # replace 함수를 통한 공백 제거
    df["가수"] = df["가수"].str.replace(" ", "")

    # WordCloud 하기 위해 한 문장(str)으로 변환
    text = ' '.join(v for v in df['가수'])
    text = re.sub(pattern=pattern, repl='', string=text)  # 정규표현식(re) 사용하여 괄호 제거
    print(text)

    wordcloud = WordCloud(font_path='malgun', background_color='ivory', 
    width=800, height=600).generate(text)
    plt.figure(figsize=(8,8))
    plt.axis('off')
    plt.imshow(wordcloud, interpolation='bilinear') 
    plt.title(year[i])
    plt.show()