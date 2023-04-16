# 42, 69 실습 파일

# class 내부에서 만들어진 변수는 반드시 self. 붙이기
# connect 안의 함수는 () 사용 하지 않는 것이 규칙

from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from selenium import webdriver
import time
import random

import urllib.request as req
from PyQt5.QtGui import QPixmap

ui_file = "./GUI/instagram.ui"

# Worker2
class SeleniumWorker(QObject):
    # 시그널 생성(int형)
    login_progress_signal = pyqtSignal(int) # pyqtSignal()함수는 반드시 class 바로 밑에만 선언
    login_success_signal = pyqtSignal(bool)
    search_progress_signal = pyqtSignal(int)
    search_success_signal = pyqtSignal(bool)
    img_url_signal = pyqtSignal(str)
    content_signal = pyqtSignal(str)

    def __init__(self):
        # 시그널 받을 준비
        self.user_id = ""
        self.user_pw = ""
        self.user_keyword = ""

        QObject.__init__(self, None)

    def instagram_login(self):
        # 브라우저 열기
        self.browser = webdriver.Chrome("./chromedriver.exe")
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        self.login_progress_signal.emit(30)
        time.sleep(3)
        self.login_progress_signal.emit(40)

        # 로그인
        id = self.browser.find_element_by_name("username")
        self.login_progress_signal.emit(50)
        id.send_keys(self.user_id)
        self.login_progress_signal.emit(60)
        pw = self.browser.find_element_by_name("password")
        self.login_progress_signal.emit(70)
        pw.send_keys(self.user_pw)
        self.login_progress_signal.emit(80)
        self.browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
        self.login_progress_signal.emit(90)
        time.sleep(4)
        self.login_progress_signal.emit(100)

        # 로그인 성공 시, 실패 시 시그널 방출
        if self.browser.current_url == "https://www.instagram.com/":
            self.login_success_signal.emit(True)
        else:
            self.login_success_signal.emit(False)

    def search(self):
        # hash_tag 검색
        self.search_progress_signal.emit(20)
        url = "https://www.instagram.com/explore/tags/{}/".format(self.user_keyword)
        self.browser.get(url)
        self.search_progress_signal.emit(40)
        time.sleep(7)
        self.search_progress_signal.emit(60)

        # 첫번째 사진 클릭
        self.browser.find_element_by_css_selector("div._9AhH0").click()
        self.search_progress_signal.emit(80)
        time.sleep(3)
        self.search_progress_signal.emit(100)
        self.search_success_signal.emit(True)

        # row_num = 1

        # 자동 좋아요 실행 & 닉네임과 내용 엑셀파일에 저장
        while True:
            # 만약에 좋아요가 안 눌려져 있다면?(aria-label의 속성값이 "좋아요"라면?)
            #     좋아요 누르고
            #     다음 사진 넘어가고
            # 만약 좋아요가 눌려져 있다면?(aria-label의 속성값이 "좋아요 취소"라면?)
            #     다음 사진 넘어가고

            # 요소 가져오기
            like = self.browser.find_element_by_css_selector("span.fr66n > button.wpO6b > div.QBdPU svg._8-yf5")
            likevalue = like.get_attribute("aria-label")
            next = self.browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
            img = self.browser.find_element_by_css_selector("article.M9sTE.L_LMM.JyscU.ePUX4 img.FFVAD")
            nick_name = self.browser.find_element_by_css_selector(
                "a.sqdOP.yWX7d._8A5w5.ZIAjV ")  # a.sqdOP.yWX7d._8A5w5.ZIAjV에 해당하는 요소가 많지만, select를 사용하면 제일 위에 것만 불러오므로 상관없음
            content = self.browser.find_element_by_css_selector(
                "div.C4VMK > span")  # div.C4VMK > span에 해당하는 요소가 많지만, select를 사용하면 제일 위에 것만 불러오므로 상관없음

            self.content_signal.emit(content.text)
            self.img_url_signal.emit(img.get_attribute("src"))
            # content_normalize = unicodedata.normalize("NFC", content.text)  # 한글의 자음 모음 분리 현상 해결

            # # 닉네임과 내용 엑셀파일에 저장
            # sheet.cell(row=row_num, column=1).value = nick_name.text
            # sheet.cell(row=row_num, column=2).value = content_normalize
            # row_num += 1
            # book.save("./인스타그램.xlsx")

            # 자동 좋아요 실행
            if likevalue == "좋아요":
                like.click()  # likevalue.click() : 속성값을 클릭하는 것이 되므로 안됨 / like.click() : css 선택자 전체를 누르는 것이므로 좋아요 버튼을 클릭하는 것이 됨
                time.sleep(random.randint(2, 5) + random.random())
                next.click()
                time.sleep(random.randint(2, 5) + random.random())
            elif likevalue == "좋아요 취소":
                next.click()
                time.sleep(random.randint(2, 5) + random.random())

# Worker1
class MainDialog(QDialog):
    # 시그널 생성
    login_signal = pyqtSignal()
    search_signal = pyqtSignal()

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)
        
        # worker2를 작업공간에 배치
        self.worker = SeleniumWorker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        self.search_button.setEnabled(False)
        
        # progressbar 초기 설정
        self.login_progressbar.setValue(0)
        self.search_progressbar.setValue(0)

        # 버튼 누르면 연결
        self.login_button.clicked.connect(self.login_start)
        self.search_button.clicked.connect(self.search_start)
        # worker2와 시그널 연결
        self.login_signal.connect(self.worker.instagram_login) # 여기 connect 안의 함수는 () 사용 하지 않는 것이 규칙
        # worker1과 시그널 연결
        self.worker.login_progress_signal.connect(self.login_progressbar.setValue)
        self.worker.login_success_signal.connect(self.login_finish)
        self.search_signal.connect(self.worker.search)
        self.worker.search_progress_signal.connect(self.search_progressbar.setValue)
        self.worker.search_success_signal.connect(self.search_finish)
        self.worker.content_signal.connect(self.show_content)
        self.worker.img_url_signal.connect(self.show_image)

    def login_start(self):
        self.login_status.setText("로그인 중...")

        # 로그인 버튼 비활성화
        self.login_button.setEnabled(False)

        # worker2에 시그널 방출할 정보 준비
        self.worker.user_id = self.input_id.text()
        self.worker.user_pw = self.input_pw.text()
        # worker2에 시그널 방출
        self.login_signal.emit()

    # login_status 값, 서치 버튼 바꾸기
    def login_finish(self, data):
        if data == True:
            self.login_status.setText("로그인 성공!")
            self.login_button.setEnabled(True)
            self.search_button.setEnabled(True)
        else:
            self.login_status.setText("로그인 실패! 다시 시도")
            self.login_button.setEnabled(True)

    def search_start(self):
        self.search_status.setText("해시태그 검색 중...")

        # 서치 버튼 비활성화
        self.search_button.setEnabled(False)

        self.worker.user_keyword = self.input_search.text()
        # worker2에 시그널 방출
        self.search_signal.emit()

    def search_finish(self, data):
        if data == True:
            self.search_status.setText("자동 좋아요 누르는 중...")

    def show_content(self, data):
        self.text_label.setText(data)

    def show_image(self, img_url):
        data = req.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap = pixmap.scaled(250, 250)
        self.img_label.setPixmap(pixmap)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)

main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())