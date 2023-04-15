# 정규표현식 공부 : https://dojang.io/mod/page/view.php?id=2435

# ● 정규 표현식(regular expression)
    # 1. 개념 : 일정한 규칙(패턴)을 가진 문자열 표현
    # 2. 특징
        # - 복잡한 문자열에서 특정 규칙으로 된 문자열 검색 + 추출 or 변경
        # - 문자열이 정해진 규칙에 맞는지 판단
    # 3. 사용방법
        # ■ 존재, 위치 판단
        # 1) 문자열에서 패턴 존재여부
            # import re
            # re.match('패턴', '문자열')
            
        # 1) 문자열에서 패턴 제일앞 위치여부 : re.search('^패턴', '문자열')
        # 1) 문자열에서 패턴 제일뒤 위치여부 : re.search('패턴$', '문자열')
        
        # ■ 개수 판단
        # 1) 문자열에서 패턴 하나라도 포함여부 : re.match('패턴1|패턴2...', '문자열')
        # 1) 문자열에서 숫자 패턴 0개 이상 포함여부 : re.match('[시작숫자-끝숫자]*', '숫자')
        # 1) 문자열에서 숫자 패턴 1개 이상 포함여부 : re.match('[시작숫자-끝숫자]+', '숫자')
        # 1) 문자열에서 패턴 0개 이상 포함여부 : re.match('패턴1*패턴2', '문자열')       # 뭔 소리??? ♣
        # 1) 문자열에서 패턴 1개 이상 포함여부 : re.match('패턴1+패턴2', '문자열')       # 뭔 소리??? ♣
        # 1) 문자열에서 패턴 0개 or 1개인지 판단 : re.match('패턴?', '문자열')
        # 1) 문자열에서 패턴 1개인지 판단 : re.match('패턴.', '문자열')
        # 1) 문자열에서 문자열 패턴 n개인지 판단 : re.match('(패턴){개수}', '문자열')     # 문자열 중에서 앞부분에 있는 문자열만 판단 ♣
#         # 1) 문자열에서 숫자 패턴 n개인지 판단 : re.match('[시작숫자-끝숫자]{개수}', '문자열')        # 문자열 중에서 앞부분에 있는 문자열만 판단 ♣
#         # 1) 문자열에서 문자열 패턴 n1개~n2개 사이인지 판단 : re.match('(패턴){시작개수,끝개수}', '문자열')       # 시작개수와 끝개수 사이 ,만 넣어야함. 띄어쓰기 넣으면 작동안함 ♣
#         # 1) 문자열에서 숫자 패턴 n1개~n2개 사이인지 판단 : re.match('[시작숫자-끝숫자]{시작개수,끝개수}', '문자열')       # 시작개수와 끝개수 사이 ,만 넣어야함. 띄어쓰기 넣으면 작동안함 ♣

        # ■ 기타 판단
        # 1) 문자열에서 숫자, 문자열 범위패턴 0개 이상 포함여부 : re.match('[a-zA-Z0-9]*', '문자열')
        # 1) 문자열에서 숫자, 문자열 범위패턴 1개 이상 포함여부 : re.match('[a-zA-Z0-9]+', '문자열')
        # 1) 문자열에서 특정 범위패턴 제외하여 판단 : re.match('[^패턴범위]*', '문자열')
        # 1) 문자열에서 특정 범위패턴 제외하여 판단 : re.match('[^패턴범위]+', '문자열')
        # 1) 문자열에서 특정 범위패턴 제일앞 위치여부 : re.search('^[패턴범위]+', '문자열')
        # 1) 문자열에서 특정 범위패턴 제일뒤 위치여부 : re.search('[패턴범위]+$', '문자열')
        # 1) 문자열에서 특수문자 판단 : \특수문자
        # 1) 문자열에서 숫자여부, 문자여부 판단
            # \d : [0-9]와 같음. 모든 숫자
            # \D : [^0-9]와 같음. 숫자를 제외한 모든 문자
            # \w : [a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄문자
            # \W : [^a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄문자 제외한 모든 문자
        # 1) 문자열에서 공백 판단
            # ' '
            # \s : [ \t\n\r\f\v]와 같음. 공백을 포함하고 스페이스, \t, \n, \r, \f, \v 포함
                # 공백(스페이스), \t(탭), \n(새 줄, 라인피드), \r(케리지 리턴), \f(폼피드), \v(수직 탭) 포함
            # \S : [^\t\n\r\f\v]와 같음. 공백을 제외하고 \t, \n, \r, \f, \v 포함

        # ■ 문자 그룹지정
        # 2) 문자열에서 문자 그룹지정 : (정규표현식 그룹1 패턴) (정규표현식 그룹2 패턴) ...
            # 그룹n에 매칭된 문자열 반환 : a.group(n)
            # 매칭된 문자열 한꺼번에 반환 : a.group() = a.group(0)
            # 각 그룹에 해당하는 문자열을 튜플형태로 한꺼번에 반환 : a.groups()
        # 2) 문자열에서 문자 그룹지정 + 그룹 이름 지정 : (?P<그룹1 이름>정규표현식 그룹1) (?P<그룹2 이름>정규표현식 그룹2) ...
            # 그룹n에 매칭된 문자열 반환 : a.group('그룹n 이름')
            # 각 그룹에 해당하는 문자열을 튜플형태로 한꺼번에 반환 : a.groups()
        # 2) 문자열에서 그룹지정 없이 패턴에 매칭되는 '모든' 문자열 가져오기 : re.findall('패턴', '문자열')
            # - 문자열을 리스트 형태로 가져온다

        # ■ 문자열 대체
        # 3) 문자열 대체(지정된 횟수만큼 대체) : re.sub('패턴', '대체할 문자열', '문자열', 바꿀횟수)
        # 3) 문자열 대체(찾은 문자열 모두 대체) : re.sub('패턴', '대체할 문자열', '문자열')
        # 3) 문자열 대체(지정된 횟수만큼 대체) + 교체 함수
            # 교체함수(매치객체)
            # re.sub('패턴', 교체함수, '문자열', 바꿀횟수)
        # 3) 문자열 대체(찾은 문자열 모두 대체) + 교체 함수
            # 교체함수(매치객체)
            # re.sub('패턴', 교체함수, '문자열')

        # ■ 문자열 그룹 재배치
        # 3) 문자열 그룹 재배치 by 그룹 숫자 : re.sub('(정규표현식 그룹1 패턴) (정규표현식 그룹2 패턴) ...', '\\g<그룹 이름> \\g<그룹 이름> ...', '문자열')
            # - 형식은 무한히 바뀔수 있으니 위에 나와있는 틀에서만 생각하지 말기
            # - 예제 반드시 참고
        # 3) 문자열 그룹 재배치 by 그룹 이름 : re.sub('(정규표현식 그룹1 패턴) (정규표현식 그룹2 패턴) ...', '\\g<그룹 이름> \\g<그룹 이름> ...', '문자열')
            # - 형식은 무한히 바뀔수 있으니 위에 나와있는 틀에서만 생각하지 말기
            # - 예제 반드시 참고

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 존재여부ㅡㅡㅡㅡㅡㅡㅡ')
import re
a = re.match('Hello', 'Hello, world!')
print(a)
b= re.match('Python', 'Hello, world!')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 위치여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.search('^Hello', 'Hello, world!')
print(a)
b = re.search('world!$', 'Hello, world!')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 하나라도 포함여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('Hello|world', 'Hello')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ숫자에서 범위숫자 0개 이상 포함여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[0-9]*', '1234')
print(a)
b = re.match('[0]*', '1234')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ숫자에서 범위숫자 1개 이상 포함여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[0-9]+', '1234')
print(a)
b = re.match('[0-9]+', 'abcd')
print(b)


print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 1개 이상 포함여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('a+b', 'b')
print(a)
b = re.match('a+b', 'aab')
print(b)
c = re.match('a+bbbbb', 'abbbbb')
print(c)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 2개 이상 포함여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('a*b', 'b')
print(a)
b = re.match('a*b', 'aab')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 0개 or 1개인지 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('H?', 'H')
print(a)
b = re.match('H?', 'Hi')
print(b)
c = re.match('H?', 'kkk')
print(c)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 1개인지 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('H.', 'Hi')
print(a)
b = re.match('H.', 'H')
print(b)
c = re.match('H.', 'kkk')
print(c)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 n개인지 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('h{3}', 'hhhello')
print(a)
b = re.match('h{3}', 'hhhhhhhhhhello')      # 이건 왜 되냐??? 문자열 중에서 앞부분에 있는 문자열만 판단 ♣
print(b)
c = re.match('h{3}', 'hellohhhhhhhhhh')     # 이건 왜 None이냐??? 문자열 중에서 앞부분에 있는 문자열만 판단 ♣
print(c)
d = re.match('h{3}', 'hhello')
print(d)

e = re.match('(hello){3}', 'hellohellohellohellohellohellohelloworld')      # 이건 왜 되냐??? 문자열 중에서 앞부분에 있는 문자열만 판단 ♣
print(e)
f = re.match('(hello){3}', 'aaahellohellohello')     # 이건 왜 None이냐??? 문자열 중에서 앞부분에 있는 문자열만 판단 ♣
print(f)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 n개인지 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')
print(a)
b = re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 패턴 n1~n2개 사이인지 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000')
print(a)
b = re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 숫자, 문자열 패턴 1개 이상 포함여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[a-zA-Z0-9]+', 'Hello1234')
print(a)
b = re.match('[A-Z0-9]+', 'hello')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 특정 범위패턴 제외하여 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[^A-Z]+', 'Hello')
print(a)
b = re.match('[^A-Z]+', 'hello')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 특정 범위패턴 제일앞 위치여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.search('^[A-Z]+', 'Hello')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 특정 범위패턴 제일앞 위치여부ㅡㅡㅡㅡㅡㅡㅡ')
a = re.search('[0-9]+$', 'Hello1234')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 특수문자 판단 : \특수문자ㅡㅡㅡㅡㅡㅡㅡ')
a = re.search('\*+', '1 ** 2')
print(a)
b = re.match('[$()a-zA-Z0-9]+', '$(document)')
print(b)
c = re.match('[$(){}a-zA-Z0-9]+', '$(document)')
print(c)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 숫자여부, 문자여부 판단 : \d \D \w \Wㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('\d+', '1234')
print(a)
b = re.match('\D+', '1234')
print(b)
c = re.match('\w+', '1234')
print(c)
d = re.match('\W+', '1234')
print(d)
a = re.match('\d+', 'Hello_1234')
print(a)
b = re.match('\D+', 'Hello_1234')
print(b)
c = re.match('\w+', 'Hello_1234')
print(c)
d = re.match('\W+', 'Hello_1234')
print(d)
e = re.match('\W+', '(:)')
print(e)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 공백 판단ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('[a-zA-Z0-9 ]+', 'Hello 1234')
print(a)
b = re.match('[a-zA-Z0-9\s]+', 'Hello 1234')
print(b)
c = re.match('[a-zA-Z0-9]+', 'Hello 1234')
print(c)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 문자 그룹짓기ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('([0-9]+) ([0-9]+)', '10 295')
print(a.group(1))
print(a.group(2))
print(a.group(0))
print(a.group())
print(a.groups())

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 문자 그룹짓기 + 그룹 이름 짓기ㅡㅡㅡㅡㅡㅡㅡ')
a = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
print(a.group('func'))
print(a.group('arg'))

print('ㅡㅡㅡㅡㅡㅡㅡ문자열에서 그룹지정 없이 패턴에 매칭되는 모든 문자열 가져오기ㅡㅡㅡㅡㅡㅡㅡ')
a = re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열 대체(지정된 횟수만큼 바꿈)ㅡㅡㅡㅡㅡㅡㅡ')
a = re.sub('apple|orange', 'fruit', 'apple box orange tree')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열 대체(찾은 문자열 모두 바꿈)ㅡㅡㅡㅡㅡㅡㅡ')
a = re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열 대체(찾은 문자열 모두 대체) + 교체 함수1ㅡㅡㅡㅡㅡㅡㅡ')
def multiple10(m):
    n = int(m.group())
    return str(n * 10)

a = re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열 대체(찾은 문자열 모두 대체) + 교체 함수2ㅡㅡㅡㅡㅡㅡㅡ')
a = re.sub('[0-9]+', lambda m: str(int(m.group()) * 10), '1 2 Fizz 4 Buzz Fizz 7 8')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열 그룹 재배치 by 그룹 숫자ㅡㅡㅡㅡㅡㅡㅡ')
a = re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234')
print(a)

b = re.sub('({\s*)"(\w+)":\s"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }')
print(b)

print('ㅡㅡㅡㅡㅡㅡㅡ문자열 그룹 재배치 by 그룹 이름ㅡㅡㅡㅡㅡㅡㅡ')
a = re.sub('({\s*)"(?P<key>\w+)":\s"(?P<value>\w+)"(\s*})', '<\\g<key>>\\g<value></\\g<key>>', '{ "name": "james" }')
print(a)

print('ㅡㅡㅡㅡㅡㅡㅡ정규 표현식 연습문제ㅡㅡㅡㅡㅡㅡㅡ')
import re

p = re.compile('\w+\@example\.\w+') # 이렇게 하면 안된다!!!
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
for email in emails:
    print(p.match(email) != None, end = ' ')