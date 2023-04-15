from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os
import urllib.request as req
from bs4 import BeautifulSoup
from PyQt5.QtGui import QPixmap

ui_file = "./movie_chart.ui"
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
            img_url = poster_image[i].attrs["src"]
            data = req.urlopen(img_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(185, 260)
            getattr(self, "img{}".format(i+1)).setPixmap(pixmap)
            getattr(self, "text{}".format(i+1)).setText("{}위 : {}".format(i+1, title[i].string))


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())