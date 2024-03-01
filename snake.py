from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            next_piece = Turtle(shape="square")
            next_piece.color("white")
            next_piece.penup()
            next_piece.goto(position)
            self.pieces.append(next_piece)

    def move(self):
        for piece in range(len(self.pieces) - 1, 0, -1):
            new_x = self.pieces[piece - 1].xcor()
            new_y = self.pieces[piece - 1].ycor()
            self.pieces[piece].goto(new_x, new_y)
        self.pieces[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)