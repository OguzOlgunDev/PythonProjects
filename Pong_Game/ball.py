from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_y = 5
        self.move_x = 5



    def move(self):
        new_x = self.xcor() +self.move_x
        new_y = self.ycor() +self.move_y
        self.goto(new_x,new_y)


    def ball_hit_wall(self):
        self.move_y *= -1

    def ball_hit_paddle(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0,0)