from turtle import *
pensize(3)
circle(20)
circle(40)
circle(80)
circle(160)

color('red', 'red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
for i in range(7):
    c = colors[i]
    color(c,c)
    begin_fill()
    rt(360/7)
    circle(50)
    end_fill()

done()
