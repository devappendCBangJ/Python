# <프로그램 자동 실행 순서 - 작업 스케쥴러>
# 0. 윈도우 검색 - 작업 스케쥴러 실행
# 1. 작업 만들기
# 1) 기본 작업 만들기 클릭
# 2) 이름 / 설명 / 작업 실행 시간 / 작업 실행 주기 / 동작 수행 타입 설정
# 3) 프로그램 / 스크립트 box : Python Interpretor 경로 지정
    # - PyCharm 왼쪽 화면 >> pythonProject 파일 >> venv 파일 >> Scripts 파일 >> python.exe 오른쪽 마우스 >> CopyPath >> 프로그램 / 스크립트에 복붙
# 4) 인수 추가 box : 실행 시킬 Python File 경로 지정
    # - PyCharm 왼쪽 화면 >> pythonProject 파일 >> 실행 시킬 파일 오른쪽 마우스 >> CopyPath >> 프로그램 / 스크립트에 복붙
    # - 파일 명에 띄워쓰기가 있는 경우 : "경로 전체" 이렇게 큰 따옴표 표시
# 5) 시작 위치 box : 실행 시킬 Project Folder 경로 지정
    # - Python File 경로에서 Python 파일명만 빼고 앞부분 복붙
# 2. 수정
# - 생성된 작업 더블클릭 후 설정
# 3. 삭제
# - 생성된 작업 오른쪽 마우스 클릭 후 삭제