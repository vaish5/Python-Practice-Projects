from turtle import Turtle, Screen

t = Turtle()
for i in range(15):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

screen = Screen()
screen.exitonclick()
