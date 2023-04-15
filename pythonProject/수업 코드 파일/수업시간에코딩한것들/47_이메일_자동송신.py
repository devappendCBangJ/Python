import openpyxl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import smtplib

# 메일 서버 로그인
naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
naver_server.login("talingpython", "q1w2e3!@#")

book = openpyxl.load_workbook("./list.xlsx")
sheet = book.active
cnt = 0
for row in sheet.rows:
    if row[4].value == "X":
        continue
    date = row[0].value
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value
    title = "{} 님, XX 쇼핑몰입니다.".format(name)
    content = """
안녕하세요. XX 쇼핑몰입니다.
결제 완료 안내 메일입니다.

성함 : {}
날짜 : {}
상품 : {}""".format(name, date, product)

    email_content = MIMEMultipart() # 택배 + 편지
    email_content["From"] = "talingpython@naver.com"
    email_content["To"] = your_mail
    email_content["Cc"] = "talingpython@naver.com, talingpython@naver.com"
    email_content["Subject"] = title

    # 편지봉투 포장
    msg = MIMEText(content, _charset="euc-kr")
    email_content.attach(msg)

    # 첨부파일 포장
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open("./attachment_file.xlsx", "rb").read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=attachment_file.xlsx")
    email_content.attach(part)

    naver_server.sendmail("talingpython@naver.com", your_mail, email_content.as_string())
    print("{}님께 메일을 보냈습니다.".format(name))
    cnt += 1
    if cnt % 20 == 0:
        naver_server.quit() # 로그 아웃.
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
        naver_server.login("talingpython", "q1w2e3!@#")






