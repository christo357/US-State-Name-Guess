import turtle
import pandas as pd
from player import Player
from score import Score


screen = turtle.Screen()
player = Player()
score = Score()

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
guess = []

# Return coordinate on screen

# def cooor(x,y):
#     print(x,y)
#
# screen.onscreenclick(cooor)

game_on = True
df = pd.read_csv("50_states.csv")
state_list = df["state"].to_list()

while(game_on):
    state = screen.textinput("Guess a state","Your guess:").title()
    print(state)
    if state == "Exit":
        break




    if state in state_list:
        state_data = df[df.state == state]
        x_cordinate = int(state_data.x)
        y_cordinate = int(state_data.y)
        print(x_cordinate,y_cordinate)
        player.update(x_cordinate, y_cordinate, state) #or use state_list.state.item() instead of state
        score.update()

        if state not in guess:
            guess.append(state)


        if len(guess) == 50:
            score.success()



missing_states = [state for state in state_list if state not in guess]            # missing_states = []
                                                                                # for state in state_list:
                                                                                #     if state not in guess:
                                                                                #         missing_states.append(state)

m_states = pd.DataFrame(missing_states)
m_states.to_csv("States to learn")




turtle.mainloop()