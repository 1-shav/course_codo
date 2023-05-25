import turtle as t
import pandas
from random import choice
from time import sleep

screen = t.Screen()
screen.title("Indian states game")
screen.setup(width=713, height=837)

img = "india_map.gif"
screen.addshape(img)

t.shape(img)


data = pandas.read_csv("data.csv")

def learn():
    score = 0
    correct = []
    while len(correct) < 29:
        answer_state = screen.textinput(title=f"Learn state's location", prompt="What's another state name?").title()


        if answer_state == "Exit":
            break
        if answer_state in data.name.to_list():
            score += 1
            correct.append(answer_state)
            row = data[data.name == answer_state]
            x = int(row.x)
            y = int(row.y)
            timmy = t.Turtle()
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(x, y)
            timmy.write(answer_state, align="center", font=("FiraCode", 10, "normal"))

    to_learn = []
    for state in data.name.to_list():
        if state not in correct:
            to_learn.append(state)
    final_data = pandas.DataFrame(to_learn)
    final_data.to_csv("report.csv")

def test():
    all_buttons = []
    for state in data.name.to_list():
        button = t.Turtle()
        button.hideturtle()
        button.shape('circle')
        button.fillcolor('yellow')
        button.penup()
        row = data[data.name == state]
        button.goto(int(row.x), int(row.y))
        button.showturtle()
        all_buttons.append(button)
    

    states = []
    writing_t = t.Turtle()
    writing_t.hideturtle()
    writing_t.penup()
    writing_t.goto(200, 275)

    def check(x, y):
            button.color("green")
        
    while len(states) < 29:
        random_state = choice(data.name.to_list())
        while random_state in states:
            random_state = choice(data.name.to_list())
    writing_t.write(random_state, align="center",font=("FiraCode", 20, "normal"))
    index = data.name.to_list().index(random_state)
    all_buttons[index].onclick(check)
    sleep(5)
    writing_t.clear()



mode_choice = screen.textinput(title="Choose the mode", prompt="Learn / Test").title()
game_is_on = True
while game_is_on:
    if mode_choice == "Learn":
        learn()
        game_is_on = False
    elif mode_choice == "Test":
        test()
        game_is_on = False


screen.mainloop()