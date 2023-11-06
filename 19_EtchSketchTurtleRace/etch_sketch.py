from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(20)


def move_backward():
    t.backward(20)


def rotate_clockwise():
    new_hdg = t.heading() - 10
    t.setheading(new_hdg)


def rotate_counter_clockwise():
    new_hdg = t.heading() + 10
    t.setheading(new_hdg)


s.listen() # Start listening for events
s.onkeypress(key="w", fun=move_forward)
s.onkeypress(key="s", fun=move_backward)
s.onkeypress(key="d", fun=rotate_clockwise)
s.onkeypress(key="a", fun=rotate_counter_clockwise)
s.onkeypress(key="c", fun=t.reset)
s.exitonclick()
