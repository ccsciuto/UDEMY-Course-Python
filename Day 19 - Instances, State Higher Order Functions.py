# higher order functions take one function and impliments it into another function
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_clockwise():
#     tim.right(10)
#
#
# def turn_counter():
#     tim.left(10)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_clockwise)
# screen.onkey(key="d", fun=turn_counter)
# screen.onkey(key="c", fun=clear_screen)
#
#
# screen.listen()
# screen.exitonclick()
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
selection = screen.textinput(title="Make your bet!", prompt="Which color turtle will win the race: ")
colors = ["red", "blue", "green", "yellow", "orange", "black"]
y_pos = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

if selection:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == selection:
                print(f"You've Won!! The winning turtle is {winning_color}")
            else:
                print(f"You've Lost! The winning turtle is {winning_color}")
        paces = random.randint(0, 10)
        turtle.forward(paces)


screen.exitonclick()