from turtle import Turtle

WIDTH = 5
LENGTH = 1
STEP_UP = 20


class Paddle(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.goto(x_cord, y_cord)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + STEP_UP)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - STEP_UP)
