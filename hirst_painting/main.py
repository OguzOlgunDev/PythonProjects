import random
import turtle


turtle.colormode(255)
obj = turtle.Turtle()


# colors = colorgram.extract('HirstD-Flumequine.jpg',10)
# rgb_color =[]
# for color in colors:
#     rgb_color.append(color.rgb)
#
# print(rgb_color)

rgb_colors = [(239, 241, 240), (246, 243, 237), (224, 234, 242), (243, 225, 74), (179, 78, 29),
              (49, 36, 26), (219, 151, 76), (146, 28, 41), (22, 25, 69), (44, 43, 120)]

# turtle.goto(-300,-250)
# turtle.shape("turtle")
# turtle.penup()

def up_left():
    obj.setheading(90)
    obj.forward(40)
    obj.setheading(180)
    obj.forward(700)
    obj.setheading(0)


obj.speed("fastest")
obj.hideturtle()
obj.penup()
obj.setheading(220)
obj.forward(475)





for i in range(16):
    for number in range(15):
        obj.setheading(0)
        obj.dot(20, random.choice(rgb_colors))
        obj.penup()
        if number < 14:
            obj.forward(50)
    up_left()







screen = turtle.Screen()
screen.exitonclick()

