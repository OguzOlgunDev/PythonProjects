from turtle import Turtle,Screen
import random

screen = Screen()
screen.colormode(255)

class Food(Turtle):

    def __init__(self,color):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.4,0.4)
        self.penup()
        self.refresh(color)



    def refresh(self,colorb):
        food_x_cor = random.randint(-280,250)
        food_y_cor = random.randint(-280,240)
        self.goto(food_x_cor,food_y_cor)
        self.colora = colorb
        self.color(self.colora)
