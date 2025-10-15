from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=800,height=600)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)

ball=Ball()
scoreboard=ScoreBoard()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on=True
while game_on:
    screen.update()
    ball.moving_ball()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision with r_paddle
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # Detect collision with r_paddle
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
screen.exitonclick()