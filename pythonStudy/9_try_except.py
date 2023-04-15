# 예외처리 공부 : https://dojang.io/mod/page/view.php?id=2398

# 드래그 후 Alt + Shift + E : 드래그한 부분의 코드만 실행
# 커서 설정 후 Alt + Shift + E : 커서 둔 부분부터 1줄씩 코드 실행

# ● 예외(exception) 처리
    # 1. 개념 : 에러 발생시 스크립트 중단하지 않고 계속 실행하기 위해
    # 2. 특징
        # 1) 예외 처리
            # - 예외 발생시 코드 실행 중단 후, except 가서 코드 실행
            # - 예외가 여러개 발생할 경우, 먼저 발생한 예외 처리 코드 or 예외 중에서 높은 계층에 있는 예외부터 처리된다
                # (기반 클래스 -> 파생 클래스 순서대로 예외 처리)
        # 2) 예외 발생
        # 3) 사용자 설정 예외
            # - Exception 기반 클래스 상속 받아서 새로운 파생 클래스로 사용자 설정 예외 생성
    # 3. 사용방법
        # 1) 예외 처리
            # try:      # 예외 발생시 아래 코드 실행 중단 후, except 가서 코드 실행
                # 실행할 코드
            # except:
                # 예외 발생 시 처리할 코드
        # 1) 특정 예외 처리
            # try:
                # 실행할 코드
            # except 특정 예외명:        # 특정 예외명 : AttributeError, NameError, TypeError, ZeroDivisionError, IndexError 등
                # 예외 발생 시 처리할 코드
        # 1) 특정 예외 처리 + 변수에 예외 에러 메시지 저장
            # try:
                # 실행할 코드
            # except 특정 예외명 as 변수:
                # 예외 발생 시 처리할 코드
        # 1) 예외 처리 + 예외 없을때 처리
            # try:      # try >> except >> else 순서
                # 실행할 코드
            # except:       # except 생략 불가
                # 예외 발생 시 처리할 코드
            # else:
                # 예외가 발생하지 않을 시 실행할 코드
        # 1) 예외 처리 + 예외 없을때 처리 + 예외 상관없이 처리
            # try:
                # 실행할 코드
            # except:       # except 생략 가능
                # 예외 발생시 처리 코드
            # else:     # else 생략 가능
                # 예외가 발생하지 않을 시 실행할 코드
            # finally:
                # 예외 발생 여부과 상관없이 항상 실행할 코드
        # 2) 예외 발생
            # raise 특정 예외명()
        # 2) 예외 발생 + 예외 에러 메시지 설정
            # raise 특정 예외명('예외 에러 메시지')
        # 3) 현재 예외 다시 발생
            # raise     # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
        # 4) 사용자 설정 예외
            # class 사용자 설정 예외명(Exception)     # Exception 상속
                # def __init__(self):
                    # super().__init__('예외 에러 메시지')     # 기반 클래스의 __init__메서드 호출

print('ㅡㅡㅡㅡㅡㅡㅡ예외 처리ㅡㅡㅡㅡㅡㅡㅡ')
try:
    x = int(input('나눌 숫자를 입력하세요 : '))
    y = 10 / x
    print(y)
except:
    print('예외가 발생했습니다.')

print('ㅡㅡㅡㅡㅡㅡㅡ특정 예외 처리ㅡㅡㅡㅡㅡㅡㅡ')
y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스, 나눌 숫자를 순서대로 입력하세요 : ').split())
    print(y[index] / x)
except ZeroDivisionError:       # 숫자를 0으로 나눠서 에러가 발생했을 때 실행
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:      # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행
    print('잘못된 인덱스입니다.')

print('ㅡㅡㅡㅡㅡㅡㅡ특정 예외 처리 + 변수에 예외 에러 메시지 저장ㅡㅡㅡㅡㅡㅡㅡ')
y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요 : ').split())
    print(y[index] / x)
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('잘못된 인덱스입니다.', e)

print('ㅡㅡㅡㅡㅡㅡㅡ예외 처리 + 예외 없을 때 처리ㅡㅡㅡㅡㅡㅡㅡ')
try:
    x = int(input('나눌 숫자를 입력하세요 : '))
    y = 10 / x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)

print('ㅡㅡㅡㅡㅡㅡㅡ예외 처리 + 예외 없을 때 처리 + 예외 상관없이 처리ㅡㅡㅡㅡㅡㅡㅡ')
try:
    x = int(input('나눌 숫자를 입력하세요 : '))
    y = 10 / x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)
finally:
    print('코드 실행이 끝났습니다.')

print('ㅡㅡㅡㅡㅡㅡㅡ예외 발생 + 예외 에러 메시지 설정ㅡㅡㅡㅡㅡㅡㅡ')
try:
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')     # 예외 발생시 코드 실행 중단 후, except 가서 코드 실행. 없으면 상위 코드 블럭으로 거슬러 올라가면서 찾음
    print(x)
except Exception as e:
    print('예외가 발생했습니다.', e)

print('ㅡㅡㅡㅡㅡㅡㅡ예외 발생 + 예외 에러 메시지 설정2ㅡㅡㅡㅡㅡㅡㅡ')
def three_multiple():
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')     # 예외 발생시 코드 실행 중단 후, except 가서 코드 실행. 없으면 상위 코드 블럭으로 거슬러 올라가면서 찾음
    print(x)

try:
    three_multiple()
except Exception as e:
    print('예외가 발생했습니다.', e)

print('ㅡㅡㅡㅡㅡㅡㅡ예외 발생 + 예외 에러 메시지 설정3ㅡㅡㅡㅡㅡㅡㅡ')
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요 : '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise       # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김

try:
    three_multiple()
except Exception as e:
    print('스크립트 파일에서 예외가 발생했습니다.', e)

print('ㅡㅡㅡㅡㅡㅡㅡ사용자 설정 예외ㅡㅡㅡㅡㅡㅡㅡ')
class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요 : '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)

three_multiple()

print('ㅡㅡㅡㅡㅡㅡㅡ예외 연습문제ㅡㅡㅡㅡㅡㅡㅡ')
try:
    file = open('maria.txt', 'r')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close()