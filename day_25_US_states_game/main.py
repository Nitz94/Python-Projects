import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ########getting coordinates from mouse clicks #############
# def get_mouse_click_coor(x, y):                           #
#     print(x, y)                                           #
#                                                           #
#                                                           #
# turtle.onscreenclick(get_mouse_click_coor)                #
#                                                           #
# turtle.mainloop() # alternate way to keep screen on       #
# ###########################################################
data = pandas.read_csv("50_states.csv")

all_states = data.state.tolist()
# state_names = data["state"].tolist()  # converting the states, x and y cor to separate lists to work with
# state_x_cor = data["x"].tolist()
# state_y_cor = data["y"].tolist()

# game_is_on = True

score = 0
correct_guesses = []
# while len(correct_guesses) < 50:
     # answer_state = (screen.textinput(title=f"{score}/50  Enter The State Names", prompt="Another State")).title()
    # state_index = state_names.index(answer_state)  # finding thr index of answer state in state names
    # state_x_index = state_x_cor[state_index]       # using state index to find x and y values
    # state_y_index = state_y_cor[state_index]
    #
    # if answer_state in state_names:
    #     score += 1
    #     correct_guesses.append(answer_state)       # saving correctly guessed states to a list
    #     new_turtle = turtle.Turtle()
    #     new_turtle.penup()
    #     new_turtle.hideturtle()
    #     new_turtle.goto(state_x_index, state_y_index)
    #     new_turtle.write(answer_state)

# MORE SIMPLIFIED CODE
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's Another State Name").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        # using list comprehension to make code shorter
        # missing_states = []

        # for state in all_states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)  # saving missing states to a list
        new_data.to_csv("Missed-States-To_Learn.csv")
        break
        # missing_states = [ state for state in all_state if state not in correct_guesses]


    if answer_state in all_states:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # getting hold of the roe which contain answer state
        t.goto(int(state_data.x), int(state_data.y))   # getting x and y values from that row
        t.write(answer_state)


screen.exitonclick()
