from turtle import Screen
from paddle import Paddle

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


if __name__ == '__main__':
    scn = Screen()
    scn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scn.bgcolor('black')
    scn.title('Pong')
    scn.tracer(n=0)

    r_paddle = Paddle(350, 0)
    l_paddle = Paddle(-350, 0)


    scn.listen()
    scn.onkeypress(key="Up", fun=r_paddle.move_paddle_up)
    scn.onkeypress(key="Down", fun=r_paddle.move_paddle_down)
    scn.onkeypress(key="w", fun=l_paddle.move_paddle_up)
    scn.onkeypress(key="s", fun=l_paddle.move_paddle_down)

    game_is_on = True
    while game_is_on:
        scn.update()

    scn.exitonclick()
