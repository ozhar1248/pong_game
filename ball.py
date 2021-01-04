from turtle import Turtle
import random
from paddle import Paddle

START_HEADING_ANGEL = 45
STEP = 20
COLLIDE_PADDLE_DISTANCE = 50

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.resetPosition()

    def resetPosition(self):
        self.goto(0,0)
        self.angel = random.randint(0, 360)
        self.setheading(self.angel)

    def move(self):
        self.forward(STEP)

    def isCollideY(self, bound):
        return self.ycor() >= bound or self.ycor() <= bound*(-1)

    def isRightLost(self, bound):
        return self.xcor() >= bound

    def isLeftLost(self, bound):
        return self.xcor() <= bound*(-1)

    def isCollideRightPaddle(self, paddle, bound):
        return self.distance(paddle) < COLLIDE_PADDLE_DISTANCE and self.xcor() > bound

    def isCollideLeftPaddle(self, paddle, bound):
        return self.distance(paddle) < COLLIDE_PADDLE_DISTANCE and self.xcor() < bound*(-1)

    def bounceY(self):
        self.angel = 360 - self.angel
        self.setheading(self.angel)

    def bouncePuddle(self):
        self.angel = 180 - self.angel
        self.setheading(self.angel)