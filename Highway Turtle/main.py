import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.setup(800,500)
screen.tracer(0)
screen.colormode(255)

def color_generator():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color



player = Player(color_generator())
car_manager = CarManager()
score = Score()

game_is_continue = True

screen.listen()

screen.onkey(key="Up",fun=player.move)


tim = 0.05

while game_is_continue:
    screen.update()
    time.sleep(tim)
    car_manager.move_cars()
    car_manager.creating_car(color_generator())
    score.write_score()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_continue = False

    if player.ycor()>200:
        tim -= 0.01
        score.level +=1
        player.goto(0,-200)












screen.exitonclick()
