import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
from konlpy.tag import Okt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

def show_me_the_graph(df):
    import networkx as nx
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm

    g = nx.Graph()
    g.add_edges_from(df)
    pr = nx.pagerank(g)
    nsize = np.array([v for v in pr.values()])
    nsize = 10000 * (nsize - min(nsize)) / (max(nsize) - min(nsize))
    pos = nx.kamada_kawai_layout(g)
    font_name = fm.FontProperties(fname="./NanumMyeongjoBold.ttf").get_name()
    plt.figure(figsize=(16, 12))
    plt.axis("off")
    nx.draw_networkx(g, font_family=font_name, font_size=16,
                     pos=pos, node_color=list(pr.values()), edge_color='.5', node_size=nsize,
                     alpha=0.7, cmap=plt.cm.autumn)
    plt.show()

okt = Okt()
keyword = "코딩"
encoded = par.quote(keyword)
page_num = 1
dataset = []
while True:
    url = "https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(page_num, encoded)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: # 끝 페이지까지 크롤링을 완료했다면?
        break
    for i in title:
        print("제목 :", i.text)
        print("링크 :", i.attrs["href"])

        dataset.append(okt.nouns(i.text))
    page_num += 1
    if page_num == 3:
        break

# print(dataset)
dataset_2 = []
for data in dataset:
    data_without_stopwords = []
    for noun in data:
        if len(noun) != 1:
            data_without_stopwords.append(noun)
    dataset_2.append(data_without_stopwords)
print(dataset_2)

te = TransactionEncoder()
te_transform = te.fit(dataset_2).transform(dataset_2)
df = pd.DataFrame(te_transform, columns=te.columns_)
# print(df)
df_apr = apriori(df, use_colnames=True, min_support=0.04)
# print(df_apr)
df_apr["length"] = df_apr["itemsets"].str.len()
df_result = df_apr[df_apr["length"] == 2]["itemsets"]

show_me_the_graph(df_result)






