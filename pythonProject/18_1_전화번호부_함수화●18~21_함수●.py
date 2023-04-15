# <문장 정리 함수>
# .strip() : 문자열 양 끝 공백과 개행문자 지움

# <특정 문자 기준 리스트형 변환 함수>
# .split("기준으로 할 문자") : 문자 기준으로 값을 나눔 >> 리스트형으로 반환

phoneList = []
f = open("./phone_book.txt", "r", encoding='UTF8') #전화번호 불러오기     #20_파일입력 함수
data = f.readlines()
for i in data:
    i = i.strip() #.strip() : 문자열 양 끝에 있는 공백, 개행문자 지워줌
    # print(i) #확인용 코드
    i = i.split(",") #split(",") : ","를 기준으로 값을 나눈 후 리스트형으로 반환
    # print(i) #확인용 코드
    # (inputData 함수 정의 할때 ,를 기준으로 name과 number를 구별했으므로)
    phoneList.append({"name" : i[0], "number" : i[1]})
    #phoneList에 사람들의 데이터가 딕셔너리 자료형으로 차곡차곡 쌓임. 실행할때마다 불러오고 시작함
numOfData = len(phoneList) #리스트 자료형에 len()함수 사용 >> 원소 개수 반환

def inputData(): #전화번호 입력
    name = input("이름 입력 : ")
    number = input("번호 입력 : ")
    phoneList.append({"name": name, "number": number})  # 위에서 만든 PhoneList틀은 리스트형인데, 자료는 리스트형 안에 딕셔너리 형이 있는 것처럼 저장됨
    f = open("./phone_book.txt", "a") #20_파일출력함수
    f.write(name + "," + number + "\n") #20_파일출력함수
    global numOfData #지역에서 전역변수 값 변경 하는 것을 허락 받음
    numOfData += 1

def searchData(): #전화번호 검색
    search_name = input("검색할 이름 입력 >> ")
    is_find = False
    for data in phoneList:
        if data["name"] == search_name:  # 딕셔너리형에서 이름을 가져옴
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            print("이름 : ", data["name"])
            print("전화번호 : ", data["number"])
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            is_find = True  # 검색에 성공함
        # else:       #이렇게 하면 전화번호를 검색한 이후에 무조건 이 명령어를 실행하게 되므로, 찾는 이름이 존재하지 않습니다라는 메시지가 떠버림
        #     print("찾는 이름이 존재하지 않습니다")
        if is_find == False:  # 검색에 실패했다면?
            print("찾는 이름이 없습니다.")

def deleteData(): #전화번호 삭제
    delete_name = input("검색할 이름 입력 >> ")
    is_find = False
    for data in phoneList:
        if data["name"] == delete_name:  # 딕셔너리형에서 이름을 가져옴
            phoneList.remove(data)  # 변수 데이터 자체가 딕셔너리니까 요렇게 삭제 가능
            global numOfData
            numOfData -= 1
            is_find = True  # 검색에 성공함
        # else:       #이렇게 하면 전화번호를 검색한 이후에 무조건 이 명령어를 실행하게 되므로, 찾는 이름이 존재하지 않습니다라는 메시지가 떠버림
        #     print("찾는 이름이 존재하지 않습니다")
        if is_find == False:  # 검색에 실패했다면?
            print("찾는 이름이 없습니다.")

def showAllData(): #전화번호 전체 출력
    for data in phoneList:  # for문과 list자료형은 궁합이 잘 맞는다
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        print("이름 : {}".format(data["name"]))
        print("전화번호 : {}".format(data["number"]))

        # print("이름 : " + data["name"])  #이것도 위와 같은 결과
        # print("전화번호 : " + data["number"])

        # print("이름 :", data["name"])  #이것도 위와 같은 결과
        # print("전화번호 :", data["number"])

while True:
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("현재 데이터 개수 : {}개".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체룰력")
    print("5. 종료")
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    menu = int(input("선택 >> "))
    if menu == 1:
        inputData()
    elif menu == 2:
        searchData()
    elif menu == 3:
        deleteData()
    elif menu == 4:
        showAllData()
    elif menu == 5:
        print("종료 되었습니다")
        break
    else:
        print("올바른 선택이 아닙니다.")