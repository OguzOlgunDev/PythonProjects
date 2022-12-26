from turtle import Turtle,Screen

screen = Screen()
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("best_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}",  align="Center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("best_score.txt", mode="w") as file:
                 file.write(f"{self.high_score}")
        self.score=0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

