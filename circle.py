from turtle import *
import random 


x = 0
y = 0

circlesize = 70
colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for y in range (0,4):
    right(90)
    circlesize = 70
    
    for x in range (0,4):

        color = (random.choice(colors))
        pencolor(color)
        circle(circlesize)
        circlesize = circlesize - 20  
        
        x = x + 1
        
y = y +1
