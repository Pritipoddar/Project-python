from turtle import *  
import colorsys
speed(0)
pensize(2)
bgcolor('black')
hue=1.8
for i in range (300):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.0
    circle(5-i,100)
    lt (500)
    circle(5-i,100)
    rt(100)


