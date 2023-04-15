# 커서 깜빡이 여러 개 생성 : shift+alt+드래그
# 문장 끝으로 이동 : End
# 지나감 : pass

phoneList = []
numOfData = 0
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
    if menu == 1: #전화번호 추가
        name = input("이름 입력 : ")
        number = input("번호 입력 : ")
        phoneList.append({"name" : name, "number" : number}) #위에서 만든 PhoneList틀은 리스트형인데, 자료는 리스트형 안에 딕셔너리 형이 있는 것처럼 저장됨
        numOfData +=1
    elif menu == 2: #전화번호 검색
        search_name = input("검색할 이름 입력 >> ")
        is_find = False
        for data in phoneList:
            if data["name"] == search_name: #딕셔너리형에서 이름을 가져옴
                print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("이름 : ", data["name"])
                print("전화번호 : ", data["number"])
                print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                is_find = True #검색에 성공함
            # else:       #이렇게 하면 전화번호를 검색한 이후에 무조건 이 명령어를 실행하게 되므로, 찾는 이름이 존재하지 않습니다라는 메시지가 떠버림
            #     print("찾는 이름이 존재하지 않습니다")
            if is_find == False: #검색에 실패했다면?
                print("찾는 이름이 없습니다.")
    elif menu == 3: #전화번호 삭제
        delete_name = input("검색할 이름 입력 >> ")
        is_find = False
        for data in phoneList:
            if data["name"] == delete_name: #딕셔너리형에서 이름을 가져옴
                phoneList.remove(data) #변수 데이터 자체가 딕셔너리니까 요렇게 삭제 가능
                numOfData -=1
                is_find = True #검색에 성공함
            # else:       #이렇게 하면 전화번호를 검색한 이후에 무조건 이 명령어를 실행하게 되므로, 찾는 이름이 존재하지 않습니다라는 메시지가 떠버림
            #     print("찾는 이름이 존재하지 않습니다")
            if is_find == False: #검색에 실패했다면?
                print("찾는 이름이 없습니다.")
    elif menu == 4: #전화번호 전체출력
        for data in phoneList: #for문과 list자료형은 궁합이 잘 맞는다
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            print("이름 : {}".format(data["name"]))
            print("전화번호 : {}".format(data["number"]))

            # print("이름 : " + data["name"])  #이것도 위와 같은 결과
            # print("전화번호 : " + data["number"])

            # print("이름 :", data["name"])  #이것도 위와 같은 결과
            # print("전화번호 :", data["number"])
    elif menu == 5: #종료
        print("종료 되었습니다")
        break
    else: #다른 값 입력
        print("올바른 선택이 아닙니다.")