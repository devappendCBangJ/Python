# View >> Tool Windows >> Terminal에서 Terminal 창 >> pip install pyqt5 입력

# <qt designer 초기세팅>
    # 구글 qt designer download >> Windows용 다운로드
    # >> qt designer 실행 >> 좌측 상단 File 클릭 >> New 클릭 >> dialog without buttons 클릭
    # >> create 클릭 >> 용도에 맞게 꾸민후 저장

# <qt designer 사용순서>
# 0. pyqt5 관련 모듈 : from PyQt5.QtWidgets import *
# 0. GUI 파일 불러오기 모듈 : from PyQt5 import uic
# 0. GUI 이미지 불러오기 모듈 : from PyQt5.QtGui import QPixmap
# 0. GUI 스레드 모듈 : from PyQt5.QtCore import QObject, QThread, pyqtSignal
# 0. 파이썬 인터프리터 제공 함수 or 변수 직접 제어 모듈 : import sys
# 1. GUI 개발 기본 틀
    # class MainDialog(QDialog):
    #     def __init__(self):
    #         QDialog.__init__(self, None)
    #         uic.loadUi("파일위치/파일명.ui", self)
    #
    #         self.worker = SeleniumWorker()
    #         self.thread = QThread()
    #         self.worker.moveToThread(self.thread)
    #         self.thread.start()
    #
    #         self.pushButton.clicked.connect(self.buttonClicked)
    #
    #     def buttonClicked(self):
    #         result = self.lineEdit.text()
    #         self.label.setText(result)
    # class Thread2(QObject):
    #     def __init__(self):
    #         QObject.__init__(self, None)
# 1-0. GUI 불러오기 : uic.loadUi("파일위치/파일명.ui", self)
    # - 위치 : 반드시 MainDialog class의 __init__ 함수 안에 GUI 불러오기 선언
# 1-0. 스레드 생성 :
    # self.worker = Thread2()
    # self.thread = QThread()
    # self.worker.moveToThread(self.thread)
    # self.thread.start()
# 1-1. 버튼 비활성화 : self.qt object명.setEnabled(False)
# 1-1. 버튼 활성화 : self.qt object명.setEnabled(True)
# 1-1. 텍스트 입력 : self.qt object명.setText("텍스트")
# 1-1. 텍스트 추출 : self.qt object명.text()
# 1-1. 숫자 입력 : self.qt object명.setValue(0~100 사이 숫자)
# 1-2. 시그널 선언 : signal명 = pyqtSignal(특정 자료형)
    # - 자료형 예시 : int, bool, double, str...
    # - 위치 : 반드시 signal 방출하는 class 안쪽 바로 아래에 시그널 선언
# 1-2. 시그널 방출 : self.signal명.emit(특정 자료형에 맞는 값)
    # - 자료형에 맞는 값 예시 : 50, True, 0.005, 한글
# 1-2. 시그널 연결 : self.signal명.connect(self.특정 함수명)
    # - 위치 : MainDialog class의 __init__ 함수 안에 시그널 연결 선언
    # - class안에 연결시킬 특정 함수명 생성해야함
    # - connect 안의 함수는 () 사용 하지 않는 것이 규칙
# 1-3. 이미지 입력 :
    # data = req.urlopen(img_url).read()
    # pixmap = QPixmap()
    # pixmap.loadFromData(data)
    # pixmap = pixmap.scaled(width 지정, height 지정)
    # self.img_label.setPixmap(pixmap)
# 2. GUI 스타일 지정 : QApplication.setStyle("fusion")
# 3. GUI 띄우기
    # app = QApplication(sys.argv)
    # main_dialog = MainDialog()
    # main_dialog.show()
    # sys.exit(app.exec_())

# class 내부에서 만들어진 변수는 반드시 self. 붙이기

# PyQt5의 기초 틀
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

ui_file = "./GUI/test.ui"
class MainDialog(QDialog):
    # Class 불러올 때 바로 시작
    def __init__(self):
        # Class 불러올 때 바로 시작
        QDialog.__init__(self, None)
        # GUI 파일 불러오기
        uic.loadUi(ui_file, self)
        
        # pushButton이 눌릴 때, lineEdit 텍스트를 label에 표시
        self.pushButton.clicked.connect(self.buttonClicked)

    # lineEdit 텍스트를 label에 표시
    def buttonClicked(self):
        # lineEdit 텍스트 추출
        result = self.lineEdit.text()
        # lineEdit 텍스트 label에 표시
        self.label.setText(result)

# GUI 스타일 지정
QApplication.setStyle("fusion")
app = QApplication(sys.argv)
# GUI 띄우기
main_dialog = MainDialog()
main_dialog.show()
# GUI 닫기
sys.exit(app.exec_())

# GUI 개발 예시
# 1. GUI 파일 불러오기, 텍스트 추출 후 표시
# class class명(QDialog):
#     def __init__(self): # class 처음 실행 함수
#         QDialog.__init__(self, None)
#         uic.loadUi("ui 파일 위치/파일명", self) : GUI 파일 불러오기
#
#         self.qt object명1.clicked.connect(self.함수명) : object명1 클릭 시 텍스트 추출본 붙여넣기
#
#     def 함수명(self):
#         result = self.qt object명2.text() : object명2 텍스트 추출
#         self.qt object명3.setText(result) : object명3에 텍스트 추출본 붙여넣기

# 1. GUI 파일 불러오기, 크롤링
# class class명(QDialog):
#     def __init__(self): # class 처음 실행 함수
#         QDialog.__init__(self, None)
#         uic.loadUi("ui 파일 위치/파일명", self) : GUI 파일 불러오기
#
#         self.qt object명1.clicked.connect(self.함수명) : object명1 클릭 시 텍스트 추출본 붙여넣기
#
#     def 함수명(self):
#         for i in range(len(title)):
#             code = req.urlopen("url 주소")
#             soup = BeautifulSoup(code, "html.parser")
#
#             텍스트 요소 = soup.select("원하는 요소")
#             이미지 요소 = soup.select("원하는 요소")
#
#             img_url = 이미지 요소[i].attrs["속성명"]
#             data = req.urlopen(img_url).read()

#             pixmap = QPixmap()
#             pixmap.loadFromData(data) : 이미지 추출
#             pixmap = pixmap.scaled(너비, 높이) : 이미지 축척 조정
#
#             getattr(self, "qt object명{}".format(i+1)).setPixmap(pixmap) : 이미지 추출본 붙여넣기

# 1. GUI 파일 불러오기, 스레드, 크롤링
# # Worker2
# class SeleniumWorker(QObject):
#     login_progress_signal = pyqtSignal(int) : 시그널 생성(int형)
#
#     def __init__(self):
#         self.user_id = "" : 시그널 받을 준비
#         self.user_pw = ""
#
#         self.browser = webdriver.Chrome("./chromedriver.exe")
#         QObject.__init__(self, None)
#
#     def instagram_login(self):
#         self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher") : 브라우저 열기
#         self.login_progress_signal.emit(30) : worker1에 시그널 방출
#         time.sleep(3)
#         self.login_progress_signal.emit(40)
#
#         # 로그인
#         id = self.browser.find_element_by_name("username")
#         self.login_progress_signal.emit(50)
#         id.send_keys(self.user_id)
#         self.login_progress_signal.emit(60)
#         pw = self.browser.find_element_by_name("password")
#         self.login_progress_signal.emit(70)
#         pw.send_keys(self.user_pw)
#         self.login_progress_signal.emit(80)
#         self.browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
#         self.login_progress_signal.emit(90)
#         time.sleep(4)
#         self.login_progress_signal.emit(100)
#
#
# class MainDialog(QDialog): : worker1
#     login_signal = pyqtSignal() : 시그널 생성
#
#     def __init__(self):
#         QDialog.__init__(self, None)
#         uic.loadUi(ui_file, self)
#
#         self.worker = SeleniumWorker() : worker2를 작업공간에 배치
#         self.thread = QThread()
#         self.worker.moveToThread(self.thread)
#         self.thread.start()
#
#         self.login_progressbar.setValue(0) : progressbar 초기 설정
#         self.search_progressbar.setValue(0)
#
#         self.login_button.clicked.connect(self.login_start)
#
#         self.login_signal.connect(self.worker.instagram_login) : instagram_login과 login_signal 연결
#         self.worker.login_progress_signal.connect(self.login_progressbar.setValue) : login_progressbar.setValue와 login_progress_signal 연결
#
#     def login_start(self):
#         self.login_status.setText("로그인 중...")
#         self.button_login.setEnabled(False) : 버튼 비활성화
#
#         self.worker.user_id = self.input_id.text() : worker2에 시그널 방출할 정보 준비
#         self.worker.user_pw = self.input_pw.text()
#         self.login_signal.emit() : worker2에 시그널 방출