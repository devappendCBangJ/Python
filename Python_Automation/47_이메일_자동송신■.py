# 네이버 메일함 >> 하단 환경설정 >> POP3/IMAP 설정 >> POP3/IMAP 사용

import openpyxl
import smtplib # 메일 서버 연결 모듈
from email.mime.text import MIMEText # 메시지를 편지봉투에 담는 모듈
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# 메일 서버 로그인
naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465) #보안 연결 SSL 필요할 때 : SMTP_SSL 사용 / 아닌 경우는 SMTP 사용
                                                  #smtplib.SMTP_SSL(SMTP 서버명, SMTP 포트 번호) : 네이버 메일 서버와 연결
naver_server.login("asdf123223", "qwer1232231!") #smtplib.SMTP_SSL(SMTP 서버명, SMTP 포트 번호).login(아이디, 비밀번호) : 네이버 메일 서버 로그인

cnt = 0

# 엑셀 파일 불러오기
book = openpyxl.load_workbook("./list.xlsx")
sheet = book.active
for row in sheet.rows: #for문 어떻게 작동되는거지?
    if row[4].value == "X": #value??
        continue # 5번째 열이 O인 경우에만 아래로 내려감 / X인 경우에는 바로 for문으로 올라가버림
    date = row[0].value
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value

# 메일 제목, 내용 설정
    title = "{}님, XX 쇼핑몰입니다.".format(name)
    content = """
안녕하세요. XX 쇼핑몰입니다.
결제 완료 안내 메일입니다.

성함 : {}
날짜 : {}
상품 : {}""".format(name, date, product)

    # 제목, 내용, 첨부파일을 택배, 편지봉투에 담아 이메일 송신
    email_content = MIMEMultipart()
    email_content["From"] = "asdf123223@naver.com"
    email_content["To"] = your_mail
    email_content["Cc"] = "asdf123223@naver.com, asdf123223@naver.com" # Cc : 참조자 지정
    email_content["Subject"] = title
    
    # 편지봉투 포장
    msg = MIMEText(content, _charset="euc-kr")
    email_content.attach(msg)
    
    # 첨부파일 포장
    # 여기 절대 외울 필요 없음. 필요할 때 복사 붙여넣기 해서 사용하면 됨
    part = MIMEBase("application", "octet-stream") # application 택배 박스에는 파일이 들어가 있다는 의미
    part.set_payload(open("./attachment_file.xlsx", "rb").read()) # rb : 바이너리 형식(2진법)으로 데이터를 주고 받겠다
    encoders.encode_base64(part) # 이메일을 보낼 때는 압축을 해서 보내야한다
    part.add_header("Content-Disposition", "attachment; filename=attachment_file.xlsx")
    email_content.attach(part)


    # 제목, 내용을 편지봉투에 담아 이메일 송신
    # msg = MIMEText(content, _charset="euc-kr") # MIMEText(내용, _charset="euc-kr") : 메시지를 편지봉투에 담음 / _charset="euc-kr : 한글이 깨지지 않도록 해줌
    # msg["From"] = "asdf123223@naver.com" # MIMEText(내용, _charset="euc-kr")["From"] : 메시지를 편지봉투에 담음 + From
    # msg["To"] = your_mail # MIMEText(내용, _charset="euc-kr")["To"] : 메시지를 편지봉투에 담음 + To
    # msg["Subject"] = title # MIMEText(내용, _charset="euc-kr")["Subject"] : 메시지를 편지봉투에 담음 + Subject
    # # print(msg.as_string()) #확인용 코드
    
    naver_server.sendmail("asdf123223@naver.com", your_mail, email_content.as_string()) #smtplib.SMTP_SSL(SMTP 서버명, SMTP 포트 번호, 저장된 msg 값).sendmail(보낼 이메일, 받는 이메일) : 네이버 메일 보내기
    print("{}님께 메일을 보냈습니다.".format(name))


    cnt += 1
    if cnt % 20 ==0: # 네이버에서 많은 양의 메일 전송을 시도할 경우 오류 발생하므로 로그아웃 후 재 로그인으로 해결
        naver_server.quit() #smtplib.SMTP_SSL(SMTP 서버명, SMTP 포트 번호).quit() : 네이버 메일 서버와 연결 끊음
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)  # 보안 연결 SSL 필요할 때 : SMTP_SSL 사용 / 아닌 경우는 SMTP 사용
        # smtplib.SMTP_SSL(SMTP 서버명, SMTP 포트 번호) : 네이버 메일 서버와 연결
        naver_server.login("asdf123223",
                           "qwer1232231!")  # smtplib.SMTP_SSL(SMTP 서버명, SMTP 포트 번호).login(아이디, 비밀번호) : 네이버 메일 서버 로그인