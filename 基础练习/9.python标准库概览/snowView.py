from turtle import *
from random import *


def drawSnow():
    hideturtle()
    pensize(2)
    for i in range(200):
        r, g, b = random(), random(), random()
        pencolor(r, g, b)
        penup()
        setx(randint(-350, 350))
        sety(randint(-20, 270))
        pendown()
        dens = randint(8, 12)
        snowsize = randint(10, 14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)


def drawGround():
    hideturtle()
    for i in range(400):
        pensize(randint(1, 5))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r, g, b = -y/280, -y/280, -y/280
        pencolor(r, g, b)
        penup()
        goto(x, y)
        pendown()
        forward(randint(40, 100))


def main():
    setup(800, 600, 200, 200)
    tracer(False)
    bgcolor('black')
    drawGround()
    drawSnow()
    done()


main()
