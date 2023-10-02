import time
import turtle


turtle.shape('turtle')
turtle.speed(4)

turtle.penup()
turtle.goto(80, 80)
turtle.left(180)
turtle.pendown()

n = 13
def zdezda(nn):
    turtle.begin_fill()
    for ww in range(n):
        turtle.forward(210)
        angel = 180-180/n
        turtle.left(angel)
    turtle.end_fill()

zdezda(1)

turtle.exitonclick()
