from turtle import *
import colorsys

# settings
bgcolor("black")
tracer(2)
pensize(2)
h = 0.42
scale_facor = 0.30

for i in range(195):
    color = colorsys.hsv_to_rgb(h, 0.9, 1)
    h += 0.0015
    pencolor(color)

    # scaling coordinates manually
    x, y = pos()
    x *= scale_facor
    y *= scale_facor
    goto(x, y)

    lt(179)
    backward(i * 0.1 * scale_facor)
    circle(i * 3 * scale_facor, 120)
    rt(14)
    forward(i * 0.1 * scale_facor)
    circle(i * 0.3 * scale_facor, 120)

done()