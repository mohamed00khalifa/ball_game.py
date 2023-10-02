from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard
score_board = ScoreBoard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("bing bong")
screen.tracer(0)
paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
game_is_on = True
score_r = 0
score_l = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        score_board.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        score_board.r_point()
        ball.reset_position()
screen.exitonclick()
