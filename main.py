import time
from turtle import Screen
from paddle import Paddle
from pong_board import PongBoard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=1200, height=800)
screen.tracer(0)

left_paddle = Paddle((-560, 0))
right_paddle = Paddle((560, 0))
ball = Ball()
pong_board = PongBoard()

screen.listen()

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 540 or ball.distance(left_paddle) < 60 and ball.xcor() < -540:
        ball.bounce_x()

    if ball.xcor() > 610:
        ball.reset_screen()
        pong_board.left_point()

    if ball.xcor() < -610:
        ball.reset_screen()
        pong_board.right_point()

screen.exitonclick()
