from turtle import Turtle


move_distance = 15

class Player(Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.setheading(90)
        self.goto(0,-200)



    def move(self):
        self.forward(move_distance)