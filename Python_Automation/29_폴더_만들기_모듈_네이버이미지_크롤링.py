#View > Tool Windows > Terminal에서 Terminal창 >> pip install os 입력

#<폴더 만들기 모듈>
# 0. 모듈 불러오기 : import os
# 1. 폴더 존재여부 확인 : os.path.exists("파일 경로/폴더 이름")
# 1. 파일의 절대경로 반환 : os.path.abspath("파일 경로/파일 이름")
    # ./ : 현재 프로젝트 폴더 경로
# 2. 폴더 생성 : os.mkdir("파일 경로/폴더 이름")

#<한글을 url주소에 맞는 문자열 형태로 변환 모듈>
# 0. 모듈 불러오기 : import urllib.parse as par
# 1. 한글을 url 주소에 맞는 형태로 변환 : urllib.parse.quote("한글")
    # - url 주소는 한글 인식 불가

# 2. url 이미지 다운 >> 경로에 저장 : urllib.request.urlretrieve(url, "파일 경로/폴더 이름")


#.attrs[""] : 딕셔너리 자료형에서 ""에 해당하는 속성값 추출
#.string : 인덱스에서 내용만 추출
# image.index(i) : image 리스트에서 원소를 하나씩 빼오는데, 이를 index 형태로 나타내면?

# if not ~~ : 만약 ~~가 아니라면

import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os

#이미지 저장할 폴더 만들기
if not os.path.exists("./알라딘이미지"):
    os.mkdir("./알라딘이미지")

keyword = input("키워드 입력 >> ")

#키워드 폴더 만들기
if not os.path.exists("./알라딘이미지/{}".format(keyword)):
    os.mkdir("./알라딘이미지/{}".format(keyword))
    
encoded = par.quote(keyword)
url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord={}&x=0&y=0".format(encoded)
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")
image = soup.select("img.i_cover") #거의 모든 웹페이지에서, 이미지를 표현하는 요소의 태그명은 img

for i in image:
    img_url = i.attrs["src"] #.attrs : 딕셔너리 자료형에서 속성값 추출
                             #.string : 인덱스에서 내용만 추출
    try:
        req.urlretrieve(img_url, "./알라딘이미지/{}/{}.jpg".format(keyword, image.index(i) + 1))
    except: # 위 문장에서 에러가 났다는 것은, 이미지가 존재하지 않는다는 뜻
        print("이미지 존재하지 않음")
    print("{} 이미지 크롤링 완료 {}".format("파이썬", image.index(i) + 1))

# cnt = 1             #이렇게 해도 위와 같음
# for i in image:
#     img_url = i.attrs["src"] #.attrs : 딕셔너리 자료형
#                              #.string : 인덱스에서 내용만
#     req.urlretrieve(img_url, "./네이버이미지/{}/{}.png".format(keyword, cnt)) 
#     #req.urlretrieve(url, 파일경로) : 해당 url 이미지를 다운로드해 경로에 저장하는 함수
#     cnt += 1