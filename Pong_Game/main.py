import turtle
import time
from paddle import Paddle
from ball import Ball
from score import Score

r_player_score = Score((30,230))
l_player_score = Score((-30,230))


screen = turtle.Screen()
screen.tracer(0)

screen.title("PONG")
screen.setup(width=800,height=600)
screen.bgcolor("black")

game_continue = True

ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))



screen.listen()
screen.onkey(key="w",fun=l_paddle.paddle_up)
screen.onkey(key="s",fun=l_paddle.paddle_down)
screen.onkey(key="o",fun=r_paddle.paddle_up)
screen.onkey(key="l",fun=r_paddle.paddle_down)


score_l =0
score_r = 0
sleep = 0.03
while game_continue:
    screen.update()
    ball.move()
    time.sleep(sleep)

    if (ball.xcor() >= 335 and ball.distance(r_paddle)<50):
        ball.ball_hit_paddle()
        sleep -= 0.0025
    if (ball.xcor() > 335):
        ball.reset_position()
        sleep =0.03
        score_l += 1
        l_player_score.score_up(score_l)


    if (ball.xcor() <= -335 and ball.distance(l_paddle)<50):
        ball.ball_hit_paddle()
        sleep -= 0.0025
    if (ball.xcor() < -335):
        ball.reset_position()
        sleep = 0.03
        score_r += 1
        r_player_score.score_up(score_r)








    if ball.ycor() >280 or ball.ycor() < -280:
        ball.ball_hit_wall()









screen.exitonclick()