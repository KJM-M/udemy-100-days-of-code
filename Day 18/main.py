# import colorgram
import turtle
from turtle import Turtle
import random

# colors = colorgram.extract('color_palette.jpg', 100)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

kilppari = Turtle()

color_list = [(208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203),
              (45, 55, 104), (158, 46, 83), (169, 160, 39), (128, 189, 143), (83, 20, 44), (38, 42, 67),
              (186, 93, 105), (187, 140, 171), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91),
              (195, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (58, 130, 121), (217, 176, 188),
              (220, 182, 167), (166, 207, 165), (179, 188, 212), (147, 37, 35), (46, 73, 71), (45, 65, 62)]

turtle.colormode(255)
kilppari.shape("circle")
kilppari.speed("fastest")
kilppari.penup()
kilppari.hideturtle()
cur_y_pos = -260
cur_x_pos = -360


for _ in range(10):
    kilppari.teleport(cur_x_pos, cur_y_pos)

    for _ in range(10):
        kilppari.forward(50)
        kilppari.dot(20, random.choice(color_list))
    cur_y_pos += 50


screen = turtle.Screen()

screen.setup(width=800, height=600)
screen.exitonclick()
