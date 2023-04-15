import urllib.request as req
from bs4 import BeautifulSoup
import requests

code = req.urlopen("http://www.cgv.co.kr/movies/")
soup = BeautifulSoup(code, "html.parser")
title = soup.select("div.sect-movie-chart strong.title")
poster_image = soup.select("span.thumb-image > img")

token = "n7jsTJPZ7WtEMECr7lyEBIwtYjqxfNnPrbN77YGRogr"
h = {"Authorization": "Bearer {}".format(token)}
for i in range(len(title)):
    d = {"message": "{}위 : {}".format(i+1, title[i].string),
         "imageThumbnail" : poster_image[i].attrs["src"],
         "imageFullsize" : poster_image[i].attrs["src"]}
    requests.post("https://notify-api.line.me/api/notify", data=d, headers=h)  # POST