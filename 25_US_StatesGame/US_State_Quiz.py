import turtle
import pandas as pd

# Constants
IMG_PATH = 'blank_states_img.gif'
SCN_HEIGHT = 1000
SCN_WIDTH = 1000

correct_count = 0

scn = turtle.Screen()
scn.setup(width=SCN_WIDTH, height=SCN_HEIGHT)
scn.title('US State Quiz')
scn.addshape(IMG_PATH)

t = turtle.shape(IMG_PATH)
t = turtle.Turtle()
t.hideturtle()

df = pd.read_csv('50_states.csv')
df['state'] = df['state'].str.lower()
states = list(map(str.lower, df['state'].tolist()))
print(states)

def write_state(state, x, y):
    t.penup()
    t.goto(x, y)
    t.write(state)

user_ans = scn.textinput(title='Guess the State',
                         prompt="Enter a state name").lower()

while len(states) != 0:

    if user_ans in states:
        correct_count += 1
        states.remove(user_ans)
        x_cor = df[df['state'] == user_ans]['x'].values[0]
        y_cor = df[df['state'] == user_ans]['y'].values[0]
        write_state(user_ans.title(), x_cor, y_cor)

        user_ans = scn.textinput(title=f'{correct_count}/{df.shape[0]} States Correct',
                                 prompt="Enter another state name").lower()

    else:
        user_ans = scn.textinput(title=f'{correct_count}/{df.shape[0]} States Correct',
                                 prompt="Enter another state name").lower()


scn.exitonclick()









# To get x, y coords on map
# def get_x_y_coords(x, y):
#     print(x, y)
#
# t.onscreenclick(get_x_y_coords)
# t.mainloop()