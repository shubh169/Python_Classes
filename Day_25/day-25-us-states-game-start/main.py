import turtle
import pandas as pd
import warnings

# Suppress FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Screen Setup.
screen = turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data from given file.
data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]


while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state name?").title()
    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




