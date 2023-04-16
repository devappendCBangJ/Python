import turtle as t #turtle 모듈을 t라는 별명으로 불러옴

t.shape("turtle") #붓의 모양 결정
for i in range(3): #아래 과정 3번 반복 >> 삼각형 형성
    t.forward(100) #앞으로 100이동
    t.left(120) #120도만큼 왼쪽으로 이동
t.circle(50) #지름 50인 원

srn=t.Screen()
srn.setup(500, 500)

tu = t.Turtle()
tu.shape("turtle")
tu.color('red','green')
for i in range(30):
    if(i<=2):
        tu.circle(i*20)
    elif(i<=10):
        tu.forward(50+i*5)
        tu.left(90)
    elif(i<=20):
        tu.forward(50+i*5)
        tu.left(120)
    else:
        tu.forward(50+i*5)
        tu.left(72)
srn.exitonclick()

t.done()