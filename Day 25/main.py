import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.addshape(image)

turtle.shape(image)

# Get coordinates on screen
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")

correct_guesses = []

def move_to_and_write():
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    x_loc = data[data.state == state]["x"].values[0]
    y_loc = data[data.state == state]["y"].values[0]
    writer.goto(x_loc, y_loc)
    writer.write(state, align="center", font=("Courier", 10, "normal"))

while len(correct_guesses) < 50:
    answer_state = screen.textinput(f"{len(correct_guesses)}/50 States Correct", "What's another state's name?").title()

    for state in data["state"]:
        if answer_state is None or answer_state == "Exit":
            break

        if state in correct_guesses:
            continue

        elif answer_state == state:
            correct_guesses.append(state)
            move_to_and_write()
