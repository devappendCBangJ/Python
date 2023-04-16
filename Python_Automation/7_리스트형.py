# <리스트형> 일반 리스트
# 리스트 선언 : list = [원소]
# 리스트 선언 : list = []
# 원소 불러오기 : list[정수] (0~)

# 원소 개수 : len(list)
# 원소 보유 여부 : 원소 in list >> True / False

# 원소 추가 : list.append(원소)
# 원소 추가 : list.insert(리스트 인덱스, 원소)
# 원소 제거 : list.remove(원소)
# 원소 제거 : del list[리스트 인덱스]
# 원소 모두 제거 : list.clear()

# 원소 복붙 : list1 = list2.copy() >> [원소2]
# 원소 합치기 : list1.extend(list2) >> [원소1, 원소2]
# 원소 합치기 : list1 + list2 >> [원소1, 원소2]
# 원소 합치기 : list1 * 횟수 >> [원소1, 원소1, 원소1, ...]

# 원소 오름차순 정렬 : list.sort()
# 원소 내림차순 정렬 : list.sort(reverse=True)
# 원소 기존의 역순 : list.reverse()


# 리스트 문자 입력 (공백 구분)
# list.append(input().split())
# 리스트 숫자 입력 (공백 구분)
# list.append(map(int, input().split()))
# 리스트 문자 입력 (엔터 구분)
# for i in range(N):
#     list.append(input())
# 리스트 숫자 입력 (엔터 구분)
# for i in range(N):
#     list.append(int(input()))

# 리스트 출력 : print(list) # for문 필요 없음

# <주석처리>
# 한꺼번에 주석처리 : 드래그 >> ctrl + /

hero = ["헐크","아이언맨","토르","캡틴아메리카"] #[] 리스트 선언... 일반적인 리스트
print(hero[0]) #리스트에서 ?번째 값을 불러옴
hero.append("스파이더") #원소 추가
print(hero)
hero.remove("헐크") #원소 제거
print(hero)
hero[0] = "짱구" #원소 수정
print(hero)