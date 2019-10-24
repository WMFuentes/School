#This program circles and prints where a horizontal line intercepts a circle.
#by William Fuentes

from graphics import *
from math import *

def main():
    #We get the circle radius and Y value of the line.
    print("This program draws a circle with point(0,0) as center and plots a line to intercept the circle")
    r = int(input("Enter the radius of the circle (1-10):"))
    y = int(input("Enter the Y intercept of the intercepting line:"))
        
    #The pseudocode provided says to use a loop, but with the exception handling, it isnt necessary.
    #while y > r:
        #print("The Y intercept is larger than the radius")
        #y = int(input("Please enter a Y intercept smaller than the radius:"))

    #The circle and line are drawn based on user inputs.
    #Beginning of calculation, with the try/except exception handling.
    try:
        win = GraphWin("Circle Intercept", 600, 600)
        win.setCoords(-10.0,-10.0,10.0,10.0)
        circle = Circle(Point(0.0,0.0), r)
        circle.draw(win)
        line = Line(Point(-10,y), Point(10,y))
        line.draw(win)

        x1 = -sqrt(r**2 - y**2)
        x2 = sqrt(r**2 - y**2)

        circle2 = Circle(Point(x1,y), 0.5)
        circle3 = Circle(Point(x2,y), 0.5)
        circle2.draw(win)
        circle3.draw(win)

        #I was getting an issue where brackets were showing up in the picture,
        #so I googled it and found a Stackoverflow answer to use the string.format from Ch. 5.
        results = ("The intercepts are ({},{}) and ({},{}).").format(x1,y,x2,y)
        text1 = Text(Point(0,9), results)
        text1.draw(win)
        print("Please see the image for results.")

    #This is the catch-all error message, but I couldn't figure out how to
    #differentiate between no interception or a user inputting a letter, they are both ValueError.
    except:
        print("The line does not intercept the circle.")

    text2 = Text(Point(0,0), "Click to exit")
    text2.draw(win)
    win.getMouse()
    win.close()
        
main()
