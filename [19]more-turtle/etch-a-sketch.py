from turtle import Turtle, Screen

speedy = Turtle()
display = Screen()
speedy.speed(0)
def move_forwards():
    speedy.fd(10)
    if remembering:
        remember_me.append(move_forwards)

def move_back():
    speedy.bk(10)
    if remembering:
        remember_me.append(move_back)

def turn_right():
    speedy.rt(10)
    if remembering:
        remember_me.append(turn_right)

def turn_left():
    speedy.lt(10)
    if remembering:
        remember_me.append(turn_left)

def clear_screen():
    display.resetscreen()


remembering = True
remember_me = []

def initiate_remembering():
    remembering = True

display.listen()
display.onkey(key="w", fun=move_forwards)
display.onkey(key="s", fun=move_back)
display.onkey(key="a", fun=turn_left)
display.onkey(key="d", fun=turn_right)
display.onkey(key="c", fun=clear_screen)
display.onkey(key="r", fun=initiate_remembering)
display.exitonclick()

print(remember_me)