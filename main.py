# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
import random
import turtle as t

color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145)]
t.colormode(255)

timmy_the_turtle = t.Turtle()
timmy_the_turtle.ht()
t.pensize(20)
pos_x = -260
pos_y = -260
for i in range(10):
    t.penup()
    t.setpos(pos_x,pos_y)
    for j in range(10):
        t.penup()
        t.pencolor(random.choice(color_list))
        t.dot(20)
        t.penup()
        t.fd(50)
        j += 1
    pos_y += 50
    i += 1




screen = t.Screen()
screen.exitonclick()