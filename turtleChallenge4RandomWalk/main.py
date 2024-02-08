import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)  # Here turtle is not object it is the module name


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)  # Creating a tuple
    return random_colors


directions = [0, 90, 100, 270]
tim.width(15)
tim.speed("fastest")

for line in range(50):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
