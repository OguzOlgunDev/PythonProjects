from turtle import Screen, Turtle

screen = Screen()
class Score(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(position)
        self.hideturtle()
        self.write(f"{self.score}", align="Center", font=("Arial", 40, "normal"))


    def score_up(self,score):
        self.clear()
        self.write(f"{score}", align="Center", font=("Arial", 40, "normal"))



