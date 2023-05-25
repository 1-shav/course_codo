# from colorgram import extract

# colors = extract("/home/1_shav/storage warehouse/code_py/[18]turtle-gui/hirst.jpeg", 20)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)

from turtle import Turtle, Screen, colormode
from random import choice

color_list = [(187, 18, 44), (243, 231, 66), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50)]
t = Turtle()
s = Screen()
colormode(255)

t.speed(0)

t.ht()

def draw_dots():
    for _ in range(10):
        t.dot(20, choice(color_list))
        t.ht()
        t.penup()
        t.fd(50)

def go_up():
    t.pendown()
    draw_dots()
    t.setheading(90)
    t.fd(50)
    t.setheading(180)
    t.fd(500)
    t.setheading(0)


t.penup()
t.goto(-218.12,-224.98)

for _ in range(10):
    go_up()

s.exitonclick()