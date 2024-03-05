from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(position)

    def move_up(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")