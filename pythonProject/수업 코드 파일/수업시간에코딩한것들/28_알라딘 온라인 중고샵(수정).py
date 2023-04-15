import urllib.request as req
from bs4 import BeautifulSoup

f = open("./알라딘중고샵.txt", "w")

page_num = 1
while True:
    code = req.urlopen("https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(page_num))
    soup = BeautifulSoup(code, "html.parser")
    book_list = soup.select("div.ss_book_box") # 우선 책 리스트들을 크롤링합니다.
    if len(book_list) == 0: # 책 리스트가 없다는 것은 끝 페이지까지 크롤링을 모두 완료했다는 뜻이므로,
        break # 무한 루프를 탈출합니다.
    for i in range(len(book_list)):
        # 책 제목 크롤링
        title = book_list[i].select_one("a.bo3 > b").string
        # 책 가격 크롤링 시, 웹페이지상에서 '새책 가격'이 누락되어있는 것들이 중간에 껴있는 것을 확인하였습니다. 따라서 이를 처리해줄 알고리즘을 짜야합니다.
        new_book_price = book_list[i].select_one("tr > th:nth-of-type(1) > .bo_used") # 우선 표에서 "새책" 이라는 문자열이 있는지를 확인합니다. 이 때, 제가 css선택자로 :nth-of-type(1) 이라는 것을 적었는데
                                                            # 이 ":nth-of-type()" 은 자손들 중에서 특정 자손 하나만을 가르킬 때 사용합니다.
                                                            # 예를 들어, tr > td:nth-of-type(1)  이라고 하면, "<tr>의 자손인 <td> 들 중에서 '첫번째' <td>" 를 의미하게 됩니다.
                                                            # 한번 그 크롬의 개발자 도구 창에서 'css 선택자 검토하는 방법'으로,
                                                            # 위 CSS 선택자를 넣어 어떤 요소들이 검색되는지 확인해보세요.
                                                            # :nth-of-type(1) 을 없애고 검색된 결과와
                                                            # :nth-of-type(1) 을 넣고 검색된 결과를 비교해보면 왜 제가 :nth-of-type(1)을 넣었는지 이해하실 수 있을 거에요.
                                                            # 지금과 같이 우리가 알고 있는 css 선택자만으로 우리가 원하는 것을 가져오기 힘들 때, :nth-of-type()은 유용하게 쓰입니다.
        if new_book_price.string != "새책": # 크롤링 결과가 "새책"이 아니라면? --> 이는 해당 책에는 새책 가격이 없다는 뜻이므로,
            price = "새책 가격 없음" # price 변수에 "새책 가격 없음"이라고 저장
        else:  # 크롤링 결과가 "새책"이라면? --> 이는 해당 책에는 새책 가격이 있다는 뜻이므로,
            price = book_list[i].select_one("tr > td:nth-of-type(1) > a.bo_used > b").string # 새책 가격 크롤링  # 기존에는 제가 css 선택자를 단순히 "a.bo_used > b" 라고 했지만, 이는 다른 동명이인까지 가져오게 됩니다. 따라서 CSS 선택자를 더 자세히 작성해주었습니다.
        print(title, price)
        f.write(title + "\t" + price + "\n")
    page_num += 1

f.close()