import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_obj = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")  # Move the turtle with key press

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_obj.create_car()
    car_obj.move_cars()

    # Detect when turtle reaches the other side
    if player.ycor() > 300:
        car_obj.increase_cars_speed()
        player.reset_position()
        scoreboard.increase_score()

    # Detect turtle collision with car
    for car in car_obj.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
