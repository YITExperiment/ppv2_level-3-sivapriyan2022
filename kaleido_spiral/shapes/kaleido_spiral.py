import turtle
from itertools import cycle

colors_b = cycle(['Seashell', 'Thistle', 'Hot Pink', 'Light Blue', 'blue', 'Yellow'])
colors_p = cycle(['Gold', 'orange', 'Lawn Green'])

def draw_circle(size,angle,shift,shape):
    turtle.bgcolor(next(colors_b))
    turtle.pencolor(next(colors_p))
    next_shapes = ''
    if shape == "circle":
        turtle.circle(size)
        next_shapes = 'square'
    elif shape == "square":
        for l in range(4):
            turtle.forward(size * 2)
            turtle.left(90)
            next_shapes = "circle"
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle-15, shift, next_shapes)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(20)
draw_circle(30,0,1,"circle")