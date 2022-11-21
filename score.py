from turtle import Turtle

FONT = ("ariel",20,"normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color("black")
        self.speed("fastest")
        self.score = 0
        self.display()

    def update(self):
        self.score += 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score :{self.score}/50", align="center", font=FONT)

    def success(self):
        self.clear()
        self.goto(0,0)
        self.write(f"You Win", align="center", font=FONT)
