# 1. AWS 회원가입 : 구글 AWS EC2 검색 >> 무료 계정 만들기(해외결제카드 등록. 영문주소 기입 등) >> 로그인
# 2. AWS 키 페어 발급 : 좌측 상단 서비스 >> 컴퓨팅 >> EC2 >> 인스턴스 시작 >> Amazone Mahcine Image 중에서 Microsoft Windows Server 2019 Base 검토 및 시작
    # >> 새 키 페어 이름지정, 저장, 다운로드 >> 예상 요금 알림 받기 신청(이거 안하면 1년 무료 기간 이후 돈 계속 빠져나감)
    # >> 결제 알림 생성 버튼 >> 모든 체크 박스 체크, 이메일 주소 입력 후 저장
# 3. AWS 서버 설정 : 인스턴스 보기 >> 가운데 인스턴스 부분에서 오른쪽으로 스크롤 넘긴 후, 보안 그룹 이름 확인 >> 왼쪽 네트워크 및 보안 탭 부분에서 보안 그룹 이름 확인
    # >> 보안 그룹 ID 클릭 >> 인바운드 규칙 편집 클릭 >> 규칙 추가 클릭 >> 유형 : 사용자 지정 TCP, 포트 범위 : 5000, 소스 : 0.0.0.0/0 지정
    # >> 규칙 추가 한 번 더 클릭 >> 유형 : 모든 TCP, 소스 : 위치 무관 지정
# 4. AWS 서버 설정 : 왼쪽 인스턴스 탭 부분에서 인스턴스 ID 우클릭 >> 연결 클릭 >> RDP 클라이언트 클릭 >> Public DNS 값 복사, 사용자 이름 값 복사
    # >> 암호 가져오기 클릭 >> 키페어 Browse를 통해 불러오기 >> 암호 해독 클릭 >> 암호 값 복사
# 5. 원격 설정 : Microsoft Store 클릭 >> Microsoft remote desktop 설치 >> 실행 후 Add PC 클릭 >> PC name : Public DNS 값 붙여넣기,
    # User account : Add User Account >> Username : 사용자 이름 값 붙여넣기, Password : 암호 값 붙여넣기 >> Add 클릭
# 6. 원격 접속 후 초기 설정 :
    # 파일 설치 : Microsoft remote desktop에서 추가된 서버 클릭해서 접속 >> 인터넷 연결 Yes 클릭 >> python3.7 다운 후 설치
    # >> jdk Windows x64 다운 후 설치 >> This PC(내컴퓨터) 우클릭 Properties 클릭 >> Advanced system settings 클릭 >> Environment Variables 클릭
    # >> New 클릭 >> Variable name : JAVA_HOME 지정 >> Browse Directory 클릭 >> This PC 클릭 >> Local Disk(C:) 클릭 >> Program Files 클릭
    # >> Java 클릭 >> jdk 1.8.0_271 클릭 >> OK 클릭 >> 싹다 OK 클릭
    # 모듈 설치 : cmd >> pip install jpype1 konlpy tensorflow pyecharts==0.5.10 pyecharts_snapshot bs4 flask 입력
    # 파이썬 파일 가져오기 : 기존 컴퓨터에서 FlaskServer Pycharm 파일 전부 복사(venv만 제외) >> 서버에서 바탕화면 오른쪽 마우스 클릭 >> New 클릭 >> Folder 클릭
    # >> FlaskServer Pycharm 파일 전부 붙여넣기(venv만 제외)
    # 코드 수정 : main.py 열기 >> with open('wordIndex.json') 부분을 with open(r'C:\Users\Administrator\Desktop\server\main.py\wordIndex.json')으로 변경
    # >> loaded_model = load_model(best_model.h5) 부분을 loaded_model = load_model(r'C:\Users\Administrator\Desktop\server\main.py\best_model.h5')으로 변경
    # >> Flask는 외부와의 통신을 위해 5000번 port를 이용하므로 app.run(host="0.0.0.0", port=80)을 app.run(host="0.0.0.0", port=5000)으로 변경
    # >> Ctrl + S 후 닫기
    # 외부 통신 개방 : 윈도우 작업표시줄 검색 창 >> firewall 검색 후 클릭 >> Advanced settings 클릭 >> 왼쪽 Inbound Rules 클릭 >> 오른쪽 New Rule 클릭
    # >> Port 클릭 >> Next 클릭 >> Specific local ports : 5000 입력 >> Next 클릭 >> Allow the connection 클릭 >> Next 클릭
    # >> Name : flask_server 입력 >> Finish 클릭
# 7. 서버 실행 : cmd >> cd Desktop 입력 >> cd server 입력 >> python main.py 입력
    # >> 오류 발생 시 구글 c++ redistributable 입력 >> Download Visual Studio 2015용 C++ 재배포 가능 다운로드(vc_redist.x64.exe)
    # >> cmd >> python main.py 입력
    # >> 그래도 오류 발생 시 cmd >> pip uninstall tensorflow 입력 >> pip install tensorflow==1.15.0 입력
    # >> cmd >> python main.py 입력
    # >> 그래도 오류 발생 시 main.py 열기 >> loaded_model = load_model(r'C:\Users\Administrator\Desktop\server\main.py\best_model.h5')을
    # loaded_model = load_model(r'C:\Users\Administrator\Desktop\server\main.py\best_model.h5', compile=False)으로 변경 >> Ctrl + S 후 닫기
    # >> cmd >> python main.py 입력
# 8. 서버 접속 : 4에서 복사한 Public DNS값 이용 >> 아무데서나 인터넷 http://Public DNS값:5000 접속
# 9. 서버 24시간 유지 : server 폴더에서 txt 파일 생성 >> txt 파일 내에
    # Set objShell = WScript.CreateObject("WScript.Shell")
    # objShell.Run "cmd /c python C:\Users\Administrator\Desktop\server\main.py", 0 입력 후 저장
    # >> 확장자 .txt에서 .vbs로 변경 >> .vbs 파일 실행 >> 눈에 보이지는 않지만 서버 가동 중!!
    # >> 서버 접속 : 4에서 복사한 Public DNS값 이용 >> 아무데서나 인터넷 http://Public DNS값:5000 접속