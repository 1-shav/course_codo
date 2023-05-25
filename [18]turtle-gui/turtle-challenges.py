from turtle import Turtle, Screen, colormode
from random import choice, randint

kachue = Turtle()
colormode(255)
# kachue.shape("turtle")
# kachue.color("royal blue")
# for i in range(0,4):
#     kachue.fd(100)
#     kachue.right(90)
# for _ in range(10):
#     kachue.fd(10)
#     kachue.pu()
#     kachue.fd(10)
#     kachue.pd()
# for x in range(3):
#     kachue.fd(30)
#     kachue.rt(120)
#     kachue.fd(30

# for sides in range(3,11):
#     angle = 360/sides
#     kachue.pencolor(choice(colours))
#     for _ in range(sides):
#         kachue.forward(90)
#         kachue.rt(angle)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

kachue.hideturtle()
kachue.pensize(10)
kachue.speed(0)

for _ in range(200):
    kachue.color(random_color())
    kachue.seth(choice(directions))
    kachue.fd(20)
def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        kachue.color(random_color())
        kachue.circle(100)
        kachue.lt(gap)

# draw_spirograph(5)


dabba = Screen()
dabba.exitonclick()