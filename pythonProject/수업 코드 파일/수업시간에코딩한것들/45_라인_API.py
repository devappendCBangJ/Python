import requests

api_key = "MXB4zg8vHxRMN0gcJGLspMUWcDVCNQrZ7EzIj07wqYr"
h = {"Authorization" : "Bearer {}".format(api_key)}
d = {"message":"테스트중입니다!!!", }
requests.post("https://notify-api.line.me/api/notify", headers=h, data=d)