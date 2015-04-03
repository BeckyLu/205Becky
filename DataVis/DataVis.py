from graphics import *
from random import randint

window = GraphWin("DataVis", 500, 500)

dataFile = open("data.txt", 'r')

def main():
    window.getMouse()
    window.close()

def dataVis():
    while True:
        for line in dataFile:
            print(line)

            circle = line
            val = float(circle)

            posX = randint(0,500)
            posY = randint(0,500)

            #r = randint(0,255)
            #g = randint(0,255)
            #b = randint(0,255)

            ball = Circle(Point(posX,posY), val)

            ball.setFill(color_rgb(val,val,val))
            ball.draw(window)
            
        else:
            return

dataVis()
main()
