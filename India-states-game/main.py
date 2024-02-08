from turtle import Screen, Turtle
import pandas

map_img = Turtle()
pointer = Turtle("circle")
pointer.shapesize(0.3)
pointer.color("blue")
pointer.penup()
screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.title("India States Game")
image = "blank_states_img.gif"
screen.addshape(image)
map_img.shape(image)

correct_guesses = []
while len(correct_guesses) < 28:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/28 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.lower()

    data = pandas.read_csv("28_states.csv")
    all_states = data.state.to_list()

    csv_answer = data[data["state"].str.lower() == answer_state]
    # print(csv_answer.values[0][0])  # Gets the value of a specific item from a dataframe
    csv_answer_state = csv_answer.values[0][0]
    csv_answer_state_lower = csv_answer_state.lower()
    csv_answer_x = csv_answer.values[0][1]
    csv_answer_y = csv_answer.values[0][2]

    score = 0

    if answer_state == csv_answer_state_lower:
        pointer.goto(csv_answer_x, csv_answer_y)
        pointer.write(csv_answer_state, font=('Arial', 8, 'normal'))
        correct_guesses.append(csv_answer_state)

    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")
        break

win_pointer = Turtle()
win_pointer.hideturtle()
win_pointer.color("green")
win_pointer.penup()
win_pointer.goto(80.0, 205.0)
win_pointer.write("You Won! 🎉", font=('Arial', 18, 'normal'))

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()
