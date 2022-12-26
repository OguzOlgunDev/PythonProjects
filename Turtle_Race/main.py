import turtle
import random


finished = False
screen = turtle.Screen()
final =turtle.Turtle()
screen.setup(width=800,height=400)
final.hideturtle()
user_bet =screen.textinput(title="Race of Turtles" ,prompt="Bet for your turtle which color win")
colors =["red","orange","pink","black","green","blue"]

y_cordinate=[-150,-90,-30,30,90,150]

all_turtles = []

final.penup()
final.goto(300,-180)
final.pendown()
final.goto(300,180)

for turtle_idx in range(0,6):
    turt = turtle.Turtle(shape="turtle")
    turt.color(colors[turtle_idx])
    turt.penup()
    turt.goto(-360, y_cordinate[turtle_idx])
    all_turtles.append(turt)

while not finished:
    for turtle in all_turtles:
        turtle.forward(random.randint(10,40))
        if turtle.xcor()>300:
            finished = True
            print(f"The winner turtle is {turtle.color()}")





screen.exitonclick()