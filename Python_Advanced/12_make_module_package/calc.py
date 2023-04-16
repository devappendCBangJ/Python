def add(a, b):
    return a + b

def mul(a, b):
    return a * b

if __name__=='__main__':    # 프로그램의 시작점일때만 아래 코드 실행
    print('스크립트 파일의 시작점!')
    print(add(10, 20))
    print(mul(10, 20))

if __name__ == 'calc':  # 모듈일때만 아래 코드 실행
    print('모듈로 사용!')