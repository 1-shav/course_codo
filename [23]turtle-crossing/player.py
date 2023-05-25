from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.seth(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def dead(self):
        self.pencolor("red")
        self.pendown()
        self.pensize(6)
        xcord = self.xcor() - 100
        ycord = self.ycor()
        self.goto(xcord, ycord)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)