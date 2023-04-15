# <외장모듈> 파이썬에 없는 모듈
# 모듈 출처 : 외부 모듈 구글링(다양한 모듈 종류, 설명, 예제 등을 볼 수 있다(ex. 게임 모듈 / 그래프 모듈 / 서버 모듈 등등))
# 모듈 설치1 : View >> Tool Windows >>Terminal >> Terminal창에 pip install 모듈명
# 모듈 설치2 : Python Packages >> packages창에 필요한 모듈명 검색 후 설치
# 모듈 설치3 : import 모듈명 부분 클릭 후 Alt+Enter+Enter
# 모듈 삭제 : View >> Tool Windows >>Terminal >> Terminal창에 pip uninstall 모듈명
# 모듈 불러오기 : import 모듈명
# 모듈 불러오면서 별멍 지정 : import 모듈명 as 별명
# 모듈에서 함수만 불러오기 : from 모듈 import 함수
# 모듈 사용 : 모듈명.함수() or 별명.함수()
#파이썬 파일명과 특정 모듈명이 중복되면 안된다

# <folium>
# 0. 모듈 불러오기 : import folium
# 1. 지도 열기 : folium.Map(location=[경도, 위도], zoom_start=축척 숫자)
# 2. 지도에 마커 표시 : folium.Marker(location=[경도, 위도], popup="클릭했을 때 팝업 창에 띄울 메시지", tooltip="마우스 커서 댔을 때 띄울 메시지", icon=folium.Icon(color=색깔)).add_to(folium.Map(location=[경도, 위도], zoom_start=축척 숫자)
# 3. 지도 저장 : folium.Map(location=[경도, 위도], zoom_start=축척 숫자).save("./map.html")
import folium

map = folium.Map(location=[39.01126861171913, 125.76282210487871], zoom_start=17)
map.save("map.html")