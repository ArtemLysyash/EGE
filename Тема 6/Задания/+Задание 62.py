# Решение
from turtle import *
screensize(20000,20000)
tracer(0)
koef = 10
right(180)
for i in range(9):
    forward(59 * koef)
    left(90)
    forward(84 * koef)
    left(90)
up()
forward(18* koef)
left(90)
forward(38* koef)
right(90)
down()
for i in range(9):
    forward(120 * koef)
    right(90)
    forward(99 * koef)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()



answer = 158

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))