from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["medium blue", "light sea green", "sea green", "dark goldenrod", "dark red",
           "red", "deep pink", "dark magenta", "medium orchid", "medium slate blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(80)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    tim.width(4)
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
