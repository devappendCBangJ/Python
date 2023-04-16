#View > Tool Windows > Terminal에서 Terminal창 >> pip install requests 입력

# <API> Application Programming Interface - 프로그램 코딩과 개발자를 이어줌
# - 특징 : BeautifulSoup or Selenium 사용하지 않고 편리하게 크롤링 가능
# - 꿀 사이트 : 구글 >> API store >> 여러 API 검색 가능

# <UI> User Interface - 유저와 개발자를 이어줌

# <API 사용 순서>
# 0. json, requests 모듈 불러오기 : import json, import requests
# 0. 필요한 API 구글링
# 1. API 가입 & 사용 신청
# 2. 예제 복붙 / 알맞게 수정
# 3. json.loads(requests.get("웹 페이지 주소").text)

# <데이터 변환>
# 1) .csv 형식 : 나누기 by 콤마
# - comma separated values
# 2) .json 형식 : 딕셔너리 자료형으로 변환
# - 딕셔너리처럼 보이지만, 컴퓨터는 딕셔너리형과 아예 다른 것으로 판단

# <html 코드 받기 비교>
# requests.get()함수 : code.text
# urllib.request.urlopen()함수 : .없이 그냥 code

# 파이썬에서 url 주소 기입 : 반드시 http:// or https:// 로 시작

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# Google >> OpenWeathermap 검색 >> https://openweathermap.org/ >> Pricing 메뉴 클릭 >> 무료 API Key download >> 회원가입
# >> API keys 탭 >> Create key 란에 test 입력 후 Generate >> 생성된 api key 복사
# >> API 탭 >> Current Weather Data API doc 클릭 >> API 명령어 복사 후 사용

import requests
import json

# api url에서 받은 코드 가공
api_key = "★sid_name★"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul", api_key)
code = requests.get(url)
result = json.loads(code.text)
print(result)

# api에서 필요한 정보 출력
print("도시 : ", result["name"])
print("현재날씨 : ", result["weather"][0]["main"]) #딕셔너리 안에 list형 그 안에 딕셔너리형 존재
print("최저기온 : ", result["main"]["temp_min"])
print("최고기온 : ", result["main"]["temp_max"])
