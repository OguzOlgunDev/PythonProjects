import time
import turtle
import random


from score import Score_Board
from snake import Snake
from food import Food


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
screen.bgcolor("cyan")
game_continue = True
up_screene =screen.setup(width=600, height=600)
screen.colormode(255)
upper = turtle.Turtle()
upper.pencolor("black")
upper.hideturtle()
upper.penup()
upper.goto(-300,250)
upper.pendown()
upper.goto(300,250)


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    random_color = (r, g, b)
    return random_color



colors=[]
for i in range (0,100):
    random_color()
    is_color = random_color()
    colors.append(is_color)
food = Food(colors[0])

snake = Snake()
score =Score_Board()
def game_continuee():
    game_continue = True
    return game_continue


screen.listen()

screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_down, key="Down")
screen.onkey( fun=snake.turn_left, key="Left")
screen.onkey( fun=snake.turn_right, key="Right")
screen.onkey(fun =game_continuee,key="p")

a = 0
while game_continue:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.segments[0].distance(food)<15:
        snake.add_segment(colors[a])
        food.refresh(colors[a+1])
        a +=1
        print(a)
        score.score +=1
        score.update_score()
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>250 or snake.segments[0].ycor() <-280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            score.reset()
            snake.reset()



































screen.exitonclick()