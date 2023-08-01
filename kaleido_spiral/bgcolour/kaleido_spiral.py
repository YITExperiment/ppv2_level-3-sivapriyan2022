import turtle
from itertools import cycle

colors_b = cycle(['#f0ffff', '#ff0fff', '#fff0ff', '#ffff0f', '#fffff0', '#0fffff'])
colors_p = cycle(['Gold', 'orange', 'Lawn Green'])

def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors_b))
    turtle.pencolor(next(colors_p))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle-15, shift)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(10)
draw_circle(30,0,1)