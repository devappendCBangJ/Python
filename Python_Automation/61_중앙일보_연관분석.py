import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par

from konlpy.tag import Okt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

okt = Okt()
dataset = []

# 31. 중앙일보_뉴스크롤링
keyword = "코딩"
encoded = par.quote(keyword)
page_num = 1
while True:
    code = req.urlopen("https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(page_num, encoded))
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: #끝 페이지까지 크롤링을 완료해서 title의 원소개수가 0개가 된다면
        break
    for i in title:
        print("제목 :", i.text)
        # 요소 안에 또다른 요소가 들어있을 경우에는 none으로 출력되므로 .string이 아닌 .text사용
        #i.text와 title[i].text는 같음
        print("링크 :", i.attrs["href"])
        dataset.append(okt.nouns(i.text))
    page_num += 1 #페이지가 넘어가면 url주소가 아예 바뀌니까
    # while안에 정의한 url 주소와 같은 곳에 두기 위해 for문 밖으로 빼둠
    if page_num == 3:
        break

# print(dataset) # 확인용 코드

# 불용어 제거
dataset_without_stopwords = []
for data in dataset:
    data_without_stopwords = []
    for noun in data:
        if len(noun) != 1:
            data_without_stopwords.append(noun)
    dataset_without_stopwords.append(data_without_stopwords)

# 전처리
te = TransactionEncoder()
te_transform = te.fit(dataset_without_stopwords).transform(dataset_without_stopwords)
df = pd.DataFrame(te_transform, columns=te.columns_)

# print(df) # 확인용 코드

# 연관 확률 분석
df_apr = apriori(df, use_colnames=True, min_support=0.06)  # support는 연관성을 나타냄. 기본적으로 0.5 이상일 경우 값을 출력하지 않으므로 그 아래 연관성도 보고싶다면 원하는 최저 연관 확률을 지정해줘야함
print(df_apr)