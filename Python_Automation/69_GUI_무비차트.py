# 25, 46 실습 파일

# <변수 for문 돌리기>
# 잘못된 예 : self."text{}".format(i+1).setText(title[i].string)
# 옳은 예 : getattr(self, "text{}".format(i + 1)).setText(title[i].string)

from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap

import urllib.request as req
from bs4 import BeautifulSoup

ui_file = "./GUI/movie_chart.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.button.clicked.connect(self.crawling_movie_chart)

    def crawling_movie_chart(self):
        code = req.urlopen("http://www.cgv.co.kr/movies/")
        soup = BeautifulSoup(code, "html.parser")

        title = soup.select("div.sect-movie-chart strong.title")
        poster_image = soup.select("span.thumb-image > img")

        for i in range(len(title)):
            img_url = poster_image[i].attrs["src"] # 이미지 불러오기
            data = req.urlopen(img_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(185, 260)

            getattr(self, "img{}".format(i+1)).setPixmap(pixmap)

            # self."text{}".format(i+1).setText(title[i].string) # 변수는 문자열 포맷팅 사용해서 for문 돌리기 불가능
            getattr(self, "txt{}".format(i+1)).setText("{}위 : {}".format(i+1, title[i].string)) # 파이썬에서 제공하는 변수 for문 돌리기 기능

QApplication.setStyle("fusion")
app = QApplication(sys.argv)

main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())