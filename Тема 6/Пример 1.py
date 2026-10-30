from turtle import *
tracer(0)
colormode(255)
koef = 20
for i in range(3):
    forward(19 * koef)
    right(90)
    forward(3 * koef)
    right(90)

for i in range(3):
    forward(5 * koef)
    right(90)
    forward(11 * koef)
    right(90)


up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x * koef,y * koef)
        dot(3)
exitonclick()