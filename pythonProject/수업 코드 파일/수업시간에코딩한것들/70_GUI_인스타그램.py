from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os
from selenium import webdriver
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import random
import urllib.request as req
from PyQt5.QtGui import QPixmap

ui_file = "./instagram.ui"

class SeleniumWorker(QObject):   # Worker2
    login_progress_signal = pyqtSignal(int)
    login_success_signal = pyqtSignal(bool)
    search_progress_signal = pyqtSignal(int)
    search_success_signal = pyqtSignal(bool)
    img_url_signal = pyqtSignal(str)
    content_signal = pyqtSignal(str)
    def __init__(self):
        self.browser = webdriver.Chrome("../../chromedriver")
        QObject.__init__(self, None)
        self.user_id = ""
        self.user_pw = ""
        self.user_keyword = ""

    def instagram_login(self):
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        self.login_progress_signal.emit(10)
        time.sleep(3)
        self.login_progress_signal.emit(20)
        id = self.browser.find_element_by_name("username")
        id.send_keys(self.user_id)
        self.login_progress_signal.emit(40)
        pw = self.browser.find_element_by_name("password")
        pw.send_keys(self.user_pw)
        self.login_progress_signal.emit(60)
        self.browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
        self.login_progress_signal.emit(80)
        time.sleep(4)
        self.login_progress_signal.emit(100)
        if self.browser.current_url == "https://www.instagram.com/":
            self.login_success_signal.emit(True)
        else:
            self.login_success_signal.emit(False)

    def search(self):
        # 해시태그 검색하기
        self.search_progress_signal.emit(20)
        url = "https://www.instagram.com/explore/tags/{}/".format(self.user_keyword)
        self.browser.get(url)
        self.search_progress_signal.emit(40)
        time.sleep(7)
        self.search_progress_signal.emit(60)
        # 첫번째 사진 클릭하기
        self.browser.find_element_by_css_selector("div._9AhH0").click()
        self.search_progress_signal.emit(80)
        time.sleep(3)
        self.search_progress_signal.emit(100)
        self.search_success_signal.emit(True)
        # 자동 좋아요 동작시키기
        row_num = 1
        while True:
            like = self.browser.find_element_by_css_selector("section.ltpMr.Slqrh button.wpO6b svg._8-yf5")
            value = like.get_attribute("aria-label")
            next = self.browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
            img = self.browser.find_element_by_css_selector("article.M9sTE.L_LMM.JyscU.ePUX4 img.FFVAD")
            ### 크롤링 ###
            nick_name = self.browser.find_element_by_css_selector("a.sqdOP.yWX7d._8A5w5.ZIAjV")
            content = self.browser.find_element_by_css_selector("div.C4VMK > span")
            self.content_signal.emit(content.text)
            self.img_url_signal.emit(img.get_attribute("src"))
            if value == "좋아요":
                like.click()
                time.sleep(random.randint(2, 5) + random.random())
                next.click()
                time.sleep(random.randint(2, 5) + random.random())
            elif value == "좋아요 취소":
                next.click()
                time.sleep(random.randint(2, 5) + random.random())


class MainDialog(QDialog):   # Worker1
    login_signal = pyqtSignal()
    search_signal = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)
        ####### worker2를 작업공간에 배치! ####
        self.worker = SeleniumWorker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()
        ####################################
        self.button_search.setEnabled(False)
        self.login_progressbar.setValue(0)
        self.search_progressbar.setValue(0)
        self.button_login.clicked.connect(self.login_start)
        self.login_signal.connect(self.worker.instagram_login)
        self.worker.login_progress_signal.connect(self.login_progressbar.setValue)
        self.worker.login_success_signal.connect(self.finish_login)
        self.button_search.clicked.connect(self.search_start)
        self.search_signal.connect(self.worker.search)
        self.worker.search_progress_signal.connect(self.search_progressbar.setValue)
        self.worker.search_success_signal.connect(self.finish_search)
        self.worker.content_signal.connect(self.show_content)
        self.worker.img_url_signal.connect(self.show_image)

    def show_image(self, img_url):
        data = req.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap = pixmap.scaled(250, 250)
        self.img_label.setPixmap(pixmap)

    def show_content(self, data):
        self.text_label.setText(data)

    def finish_search(self, data):
        if data == True:
            self.search_status.setText("자동 좋아요 누르는 중...")

    def search_start(self):
        self.search_status.setText("해시태그 검색 중...")
        self.button_search.setEnabled(False)
        self.worker.user_keyword = self.input_search.text()
        self.search_signal.emit()

    def finish_login(self, data):
        if data == True:
            self.login_status.setText("로그인 성공!")
            self.button_search.setEnabled(True)
        else:
            self.login_status.setText("로그인 실패! 다시 시도")
            self.button_login.setEnabled(True)

    def login_start(self):
        self.login_status.setText("로그인 중....")
        self.button_login.setEnabled(False)
        self.worker.user_id = self.input_id.text()
        self.worker.user_pw = self.input_pw.text()
        self.login_signal.emit()



QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())