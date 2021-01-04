from turtle import Turtle

XPLACE = 100
YPLACE = 200

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.reset_board()

    def left_update(self):
        self.l_score += 1
        self.reset_board()

    def right_update(self):
        self.r_score += 1
        self.reset_board()

    def reset_board(self):
        self.clear()
        self.goto(XPLACE * (-1), YPLACE)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(XPLACE, YPLACE)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))