from turtle import Turtle, Screen

def draw_dash(num_dashes, dash_length):
    t = Turtle()
    t.shape('turtle')
    for _ in range(num_dashes, dash_length):
        t.forward(dash_length)
        t.penup()
        t.forward(dash_length)
        t.pendown()

    scn = Screen()
    scn.exitonclick()

draw_dash(10, 50)




