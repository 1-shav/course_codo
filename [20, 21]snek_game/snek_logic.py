from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snek:
    def __init__(self):
        self.segments = []
        self.create_snek()
        self.head = self.segments[0]
    
    def create_snek(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("forest green")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snek()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].pos())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            position_tuple = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setpos(position_tuple)
        self.head.fd(MOVE_DISTACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)