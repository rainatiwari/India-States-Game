import turtle
import pandas as pd

SCORE = 0

screen = turtle.Screen()
image = "India.gif"
screen.title(f"India States Game, Current Score= {SCORE}:")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("india_states.csv")
all_state = data.state.to_list()


def update_score():
    global SCORE
    SCORE += 1


is_game_on = True

while is_game_on:
    screen.title(f"U.S. States Game, Score= {SCORE}:")
    answer_state = screen.textinput(title="Guess the State", prompt="What's another states name ?").title()

    if answer_state in all_state:
        update_score()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
