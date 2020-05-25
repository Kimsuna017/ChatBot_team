import turtle
import random
import sqlite3

##전역 변수 선언 부분(turtle)##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7

##전역 변수 선언 부분(DB)##
con, cur, row, col = None, None, None, None
data1, data2, data3, data4, data5, data6, data7 = 0, 0, 0, 0, 0, 0, 0

i = 0
sql = ""
count = 0

##메인 코드 부분##
con = sqlite3.connect("C:/DB/turtleDB")  ##DB생성
cur = con.cursor()  ##커서생성

#cur.execute("CREATE TABLE turtable(ID int,색상R float,색상G float,색상B int,순번 int,X 좌표 int,Y 좌표 int)")
turtle.title('거북이가 맘대로 다니기(DB)')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)

# 실행전 데이터 삭제
cur.execute("delete from turTable")

while (True):
    count += 1
    data1 = count
    data5 = count
    r = random.random()
    g = random.random()
    b = random.random()

    data2 = str(r)
    data3 = str(g)
    data4 = str(b)

    turtle.pencolor((r, g, b))
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)  ##이동
    turtle.forward(dist)

    curX = int(turtle.xcor())  ##현재 거북이 위치 구함
    curY = int(turtle.ycor())
    data6 = str(curX)
    data7 = str(curY)

    sql = "INSERT INTO turTable VALUES(" + str(
        data1) + ", '" + data2 + "' , '" + data3 + "' , '" + data4 + "', " + str(
        data5) + " , '" + data6 + "', '" + data7 + "')"
    cur.execute(sql)
    print("%5s %5s %5s %5s %5s %5s %5s" % (data1, data2, data3, data4, data5, data6, data7))

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        count += 1
        x=0
        data1 = count
        data5 = count
        data2, data3, data4 = str(x), str(x), str(x)
        data6 =str(x)
        data7 = str(x)
        sql = "INSERT INTO turTable VALUES(" + str(
            data1) + ", '" + data2 + "' , '" + data3 + "' , '" + data4 + "', " + str(
            data5) + " , '" + data6 + "', '" + data7 + "')"
        cur.execute(sql)
        print("%5s %5s %5s %5s %5s %5s %5s" % (data1, data2, data3, data4, data5, data6, data7))
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        exitCount += 1
        if exitCount >= 5:
            break
con.commit()

# con.close()
turtle.clear()

cur.execute("select * from turTable order by ID desc")

row = cur.fetchone()
row = cur.fetchone()

data6 = row[5]
data7 = row[6]

turtle.penup()
turtle.goto(int(data6), int(data7))
turtle.pendown()

while (True):
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    row = cur.fetchone()

    if row == None:
        break

    data1 = row[0]
    data6 = row[5]
    data7 = row[6]

    if (data6==0 and data7==0) :
        turtle.goto(int(data6), int(data7))
        row = cur.fetchone()
        data6 = row[5]
        data7 = row[6]
        turtle.penup()
        turtle.goto(int(data6), int(data7))
        turtle.pendown()
        continue
    r = data2
    g = data3
    b = data4
    turtle.pencolor((float(data2), float(data3), float(data4)))

    turtle.goto(int(data6), int(data7))


turtle.pencolor((float(data2), float(data3), float(data4)))
turtle.goto(0, 0)

turtle.done()