# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import font_manager, rc #한글출력 설정
# font_name = font_manager.FontProperties(fname="./batang.ttf").get_name()
# plt.rc("font", family=font_name)
# plt.title("막대그래프(bar)")
# x_data=[1,3,5,7,9]
# y_data=[5,7,6,1,4]
# plt.bar(x_data,y_data) #bar(막대를 표시할 위치, 막대의 높이)
# plt.xlabel('숫자')
# plt.ylabel('횟수')
# plt.show()

#그래프 그리기 초기 설정
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc #한글출력 설정
font_name = font_manager.FontProperties(fname="./batang.ttc").get_name()
plt.rc("font", family=font_name)

plt.title("막대그래프(bar)")
plt.xlabel('숫자')
plt.ylabel('횟수')

x_data = []
for i in range(1, 46):
    x_data.append(i)
# print(x_data)

y_data = []
for i in range(1, 46):
    y_data.append(0)
# print(y_data)

x = np.arange(45)
# plt.bar(x_data,y_data) #bar(막대를 표시할 위치, 막대의 높이)
#그래프 명령어 2개 쓰면 겹쳐서 표시됨
plt.bar(x,y_data) #x개수의 y데이터 그리기
plt.xticks(x,x_data) #x개수의 x데이터 그리기
plt.show()