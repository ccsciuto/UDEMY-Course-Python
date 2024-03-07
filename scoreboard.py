from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        with open("snakehs.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.goto(x=0, y=270)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.hs = str(self.high_score)
            with open("snakehs.txt", mode="w") as file:
                file.write(self.hs)
        self.score = 0
        self.update_scoreboard()
