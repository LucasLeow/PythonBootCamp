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

    game = Paddle()
    game.setup_paddles()


    scn.listen()
    scn.onkeypress(key="Up", fun=game.right_paddle_up)
    scn.onkeypress(key="Down", fun=game.right_paddle_down)

    game_is_on = True
    while game_is_on:
        scn.update()

    scn.exitonclick()
