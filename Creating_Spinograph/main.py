import turtle
from turtle import Turtle,Screen
import random

ob = Turtle()
turtle.colormode(255)
ob.speed("fastest")
def random_color():
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    color = (r,g,b)
    return color
ob.pensize(2)
ob.hideturtle()



def draw_spiragroph(size_of_gap):
    for number in range(int(360/size_of_gap)):
        ob.color(random_color())
        ob.circle(100)
        current_heading = ob.heading()
        ob.setheading(current_heading+size_of_gap)

draw_spiragroph(4)









screen = Screen()
screen.exitonclick()