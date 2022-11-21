from turtle import Turtle

FONT = ("ariel",10,"normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")

    def update(self, x_cor, y_cor, state):
        self.goto(x_cor, y_cor)
        self.write(state, align="center", font=FONT)
