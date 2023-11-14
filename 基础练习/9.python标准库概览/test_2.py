from random import *
from math import *
import time
from turtle import *
import turtle
import rose_data  # rose_data为存储数据的py文件
# 1:蜂窝六边形
for y in range(11):
    pen_y = 190 - 45 * y
    pen_x = -300 - 7.5 * sqrt(3) * pow(-1, y) + 7.5 * sqrt(3)
    penup()
    goto(pen_x, pen_y)
    pendown()
    for x in range(12):
        circle(30, steps=6)
        penup()
        forward(30 * sqrt(3))
        pendown()

# 2：玫瑰花_1


def draw_line(pix_list):
    turtle.penup()
    turtle.goto(pix_list[0])
    turtle.pendown()
    for pix in pix_list:
        turtle.goto(pix)


def draw_pic(pic_data):
    for i in range(1, len(pic_data) + 1):
        pix_list = pic_data[i]
        draw_line(pix_list)


def init():
    turtle.title('rose')
    turtle.pensize(2)
    turtle.hideturtle()
    turtle.color('red', 'red')
    turtle.setup(width=800, height=500, startx=0, starty=0)


if __name__ == '__main__':
    init()
    draw_pic(rose_data.data)
    turtle.mainloop()
# 2：玫瑰花_2
# 设置初始位置
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)
# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()
# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)
# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)
# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
turtle.pendown()
turtle.done()

# 3: color map
s = []
for i in range(0, 255):
    for j in range(0, 255):
        for k in range(0, 1255):
            s.append([i, j, k])
pensize(10)
for i in range(0, len(s)+1, 10):
    right(90)
    pendown()
    pencolor(s[i][0]/255, s[i][1]/255, s[i][2]/255)
    forward(100)
    penup()
    setx(i)
    sety(0)
    left(90)
done()

# 4:0-100 ten ints' list
s = []
for i in range(10):
    s.append(randint(0, 100))
print(s)
# 5:localtime transfer
print(time.strftime('%A,%d.%b %Y %I:%M%p', time.localtime()))