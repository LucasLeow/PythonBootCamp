from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RIGHT_PADDLE_POS = 350
LEFT_PADDLE_POS = -350

WALL_TOLERANCE = 10
PADDLE_TOLERANCE = 20



if __name__ == '__main__':
    scn = Screen()
    scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scn.bgcolor('black')
    scn.title('Pong')
    scn.tracer(n=0)

    r_paddle = Paddle(RIGHT_PADDLE_POS, 0)
    l_paddle = Paddle(LEFT_PADDLE_POS, 0)
    b = Ball()
    b.direction = 'right_up'

    scn.listen()
    scn.onkeypress(key="Up", fun=r_paddle.move_paddle_up)
    scn.onkeypress(key="Down", fun=r_paddle.move_paddle_down)
    scn.onkeypress(key="w", fun=l_paddle.move_paddle_up)
    scn.onkeypress(key="s", fun=l_paddle.move_paddle_down)


    game_is_on = True
    while game_is_on:
        scn.update()
        b.move()
        # Detect collision with walls
        if (
            b.ycor() >= (SCREEN_HEIGHT // 2) - WALL_TOLERANCE or
            b.ycor() <= -(SCREEN_HEIGHT // 2) + WALL_TOLERANCE
        ):
            b.wall_bounce()

        # Detect collision with paddle
        if (
            b.distance(r_paddle) <= 50 and b.xcor() > RIGHT_PADDLE_POS - PADDLE_TOLERANCE or
            b.distance(l_paddle) <= 50 and b.xcor() < LEFT_PADDLE_POS + PADDLE_TOLERANCE
        ):
            b.paddle_bounce()

        if (
            b.distance(r_paddle) > 50 and b.xcor() > RIGHT_PADDLE_POS + WALL_TOLERANCE
        ):
            b.reset_ball()
            scn.update()
            # Put timer here
            time.sleep(1)
        if (
            b.distance(l_paddle) > 50 and b.xcor() < LEFT_PADDLE_POS - WALL_TOLERANCE
        ):
            b.reset_ball()
            scn.update()
            # Put timer here
            time.sleep(1)

        time.sleep(0.05)


    scn.exitonclick()
