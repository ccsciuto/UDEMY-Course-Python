# import random
# import turtle
# from turtle import Turtle, Screen
# from random import choice
#
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("pink2")
# tim.pensize(3)
# # for _ in range(15):
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
# #     tim.forward(10)
# # sides = 3
# # continue_drawing = True
# # while continue_drawing:
# #     for _ in range(sides):
# #         tim.forward(10)
# #         tim.right(360/sides)
# #     sides += 1
# #     if sides == 10:
# #         continue_drawing = False
#
# turns = [0, 90, 180, 270]
# tim.speed(100)
# turtle.colormode(255)
#
#
# def rand_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     new_color = (r, g, b)
#     return new_color
# #
# #
# # def random_direction():
# #     return tim.setheading(choice(turns))
# #
# #
# # for _ in range(100):
# #     tim.color(rand_color())
# #     random_direction()
# #     tim.forward(100)
#
#
# def draw_spiral_graph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#         tim.color(rand_color())
#
# draw_spiral_graph(random.randint(1,15))
#
#
#
# screen = Screen()
# screen.exitonclick()
import turtle as t
import colorgram
import random



tim = t.Turtle()

colors = colorgram.extract('colors.jpg', 144)
color_list = [(140, 163, 192), (216, 221, 231), (46, 104, 160), (217, 155, 107), (188, 153, 174), (243, 232, 236), (135, 69, 102), (133, 179, 146), (109, 108, 174), (146, 79, 56), (221, 195, 133), (207, 83, 122), (83, 162, 107), (41, 157, 189), (89, 133, 112), (181, 23, 53), (231, 137, 17), (237, 66, 36), (55, 57, 115), (208, 179, 189), (161, 210, 171), (230, 174, 165), (52, 50, 61), (144, 206, 225), (57, 47, 55), (188, 188, 202), (72, 49, 44), (84, 56, 49), (88, 62, 34), (250, 195, 2), (252, 5, 55), (23, 80, 101)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
t.colormode(255)
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
tim.hideturtle()


screen = t.Screen()
screen.exitonclick()