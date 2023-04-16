# zip 공부 : https://www.daleseo.com/python-zip/

# zip 함수
    # 인자 : 여러 개의 순회 가능한(iteralbe) 객체
    # 반환 : 각 개체가 담고 있는 원소를 튜플 형태로 차례로 접근할 수 있는 반환자(iterator) 반환

# zip 기본
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

# zip과 같은 코드 - index 변수 이용
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for i in range(3):
    pair = (numbers[i], letters[i])
    print(pair)

# zip 병렬처리
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)

# zip 사전 반환
keys = [1, 2, 3]
values = ["A", "B", "C"]
dic_zip = dict(zip(keys, values))
print(dic_zip)

# zip 원소 개수 다를 때 : 가장 짧은 인자 기준으로 묶고 나머지 버림
numbers = ["1", "2", "3"]
letters = ["A"]
pairs = list(zip(numbers, letters))
print(pairs)

# unzip
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
print(pairs)

numbers, letters = zip(*pairs)
print(numbers)
print(letters)
