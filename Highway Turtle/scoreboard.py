from turtle import Turtle,Screen

screen = Screen()

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-300,200)



    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Center", font=("Arial", 24, "normal"))
