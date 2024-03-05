import time
import turtle
from turtle import Screen
from crossing import Player, Scoreboard, CarManager


screen = Screen()
screen.bgcolor("white")
screen.title("Crossing")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
player = Player((0, -280))
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun=player.move_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # advance to next level
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_score()
        car_manager.increase_speed()

#     detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


