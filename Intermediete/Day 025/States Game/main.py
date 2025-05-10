import pandas as pd
from background import Background
from user_guess import UserGuess
from turtle import Screen, Turtle

# read the data
df = pd.read_csv("50_states.csv")

# create a background
background = Background()
user_guess = UserGuess()

guess_list = []
all_state = df.state.to_list()

game_is_on = True
while game_is_on:
    # ask the user
    answer_state = user_guess.ask_user()

    # if cancel button clicked
    if answer_state is None:
        # create a report in txt format
        with open("user_result.txt", mode="w") as file:
            file.write(f"The user successfully guessed: {guess_list}.\nHere are the remaining ({len(all_state)}) states the user did not guess: {all_state}.")
        background.close_screen()
        break

    # if the user guessing
    else:
        # make it title case
        answer_state = answer_state.title()
        # if it is correct
        if answer_state in all_state:
            # add it to guess_list
            guess_list.append(answer_state)
            # remove the state from all_state
            all_state.remove(answer_state)
            # find the state's info in the dataframe
            series_state = df[df.state == answer_state]
            # get the x coordinate
            xcor = series_state.x.values[0]
            # get the y coordinate
            ycor = series_state.y.values[0]
            # print the state's name on the map
            user_guess.correct_answer(answer_state, xcor, ycor)

        # if the player guessed all the states
        if user_guess.correct == 50:
            user_guess.game_over()
            game_is_on = False
            with open("user_result.txt", mode="w") as file:
                file.write(f"The user successfully guessed all the states in US, here is the list: {guess_list}.")

background.mainloop_screen()