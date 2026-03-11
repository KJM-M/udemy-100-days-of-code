from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race?").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_pos = [(-380, -30), (-380, 30), (-380, -90), (-380, 90), (-380, -150), (-380, 150)]
turtles = []
is_race_on = False


if user_bet:
    is_race_on = True
    for each in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(colors[each])
        turtle.goto(starting_pos[each])
        turtle.penup()
        turtles.append(turtle)


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
