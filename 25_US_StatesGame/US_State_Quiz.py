import turtle

# Constants
IMG_PATH = 'blank_states_img.gif'
SCN_HEIGHT = 1000
SCN_WIDTH = 1000

scn = turtle.Screen()
scn.setup(width=SCN_WIDTH, height=SCN_HEIGHT)
scn.title('US State Quiz')

scn.addshape(IMG_PATH)
t = turtle.shape(IMG_PATH)

user_ans = scn.textinput(title='Guess the State',
                         prompt="Enter a state name")

scn.exitonclick()









# To get x, y coords on map
# def get_x_y_coords(x, y):
#     print(x, y)
#
# t.onscreenclick(get_x_y_coords)
# t.mainloop()