from graphics import *
from random import randint

window = GraphWin("DataVis", 500, 500)

dataFile = open("data.txt", 'r')


while True:
    for line in dataFile:
        print(line)
        
        circle = line
        val = float(circle)
        
        
        posX = randint(500,500)
        posY = randint(500,500)
        
        ball = Circle(Point(posX,posY), 50)
        
        
        ball.setfill(color_rgb(255,255,255))
        ball.draw(window)
        
        
    
window.getmouse()
close()
