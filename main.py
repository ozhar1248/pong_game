from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH_WINDOW = 800
HEIGHT_WINDOW = 600
PUDDLE_POSITION = 350
COLLIDE_PADDLE_XBOUND = 320
SPEED_FACTOR = 0.9
INITIAL_SPEED = 0.1

screen = Screen()
screen.setup(width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(PUDDLE_POSITION, 0)
left_paddle = Paddle(PUDDLE_POSITION*(-1), 0)
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

board = Scoreboard()

game_on = True
speed = INITIAL_SPEED

while game_on:
    screen.update()

    time.sleep(speed)
    ball.move()
    if ball.isCollideY(HEIGHT_WINDOW/2-20):
        ball.bounceY()
    if ball.isCollideRightPaddle(right_paddle, COLLIDE_PADDLE_XBOUND) or \
            ball.isCollideLeftPaddle(left_paddle, COLLIDE_PADDLE_XBOUND):
        ball.bouncePuddle()
        speed *= SPEED_FACTOR
    if ball.isRightLost(WIDTH_WINDOW/2 - 20):
        board.left_update()
        time.sleep(1.5)
        ball.resetPosition()
    if ball.isLeftLost(WIDTH_WINDOW/2 - 20):
        board.right_update()
        time.sleep(1.5)
        ball.resetPosition()
    speed = INITIAL_SPEED

screen.exitonclick()
