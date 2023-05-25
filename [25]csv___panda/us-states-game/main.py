import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S states game")
screen.setup(width=725, height=491)

image = "./[25]csv_&_panda/us-states-game/blank_states_img.gif"
screen.addshape(image)

t.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# t.onscreenclick(get_mouse_click_coor)


data = pd.read_csv("./[25]csv_&_panda/us-states-game/50_states.csv")

score = 0
correct = []
while len(correct) < 50:
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in data.state.to_list():
        score += 1
        correct.append(answer_state)
        row = data[data.state == answer_state]
        x = int(row.x)
        y = int(row.y)
        timmy = t.Turtle()
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(x, y)
        timmy.write(answer_state, align="center", font=("FiraCode", 10, "normal"))

to_learn = []
for state in data.state.to_list():
    if state not in correct:
        to_learn.append(state)
final_data = pd.DataFrame(to_learn)
final_data.to_csv("./[25]csv_&_panda/us-states-game/report.csv")