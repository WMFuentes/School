# This is a 5 click house, as instructed by Exercise 11 of our textbook.
# Clicks 1 and 2 draw the opposite corners of the house frame.
# Click 3 is the top center of the door frame, 1/5th width of the house.
# Click 4 is the center of the square window.
# Click 5 is the peak of the roof.

#by Wlliam Fuentes

from graphics import *

def main():
    #First we create the space we will work in.
    win = GraphWin("Five Click House", 500, 500)
    win.setCoords(0,0,10,10)

    #Here we gather points for the house frame.
    p1 = win.getMouse()
    p2 = win.getMouse()

    #Gathering x & y coords for later use.
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    #Doing a little calculation to be used on the door and window.
    width = x2 - x1
    tenth = width / 10

    #Now we can draw the house rectange.
    house = Rectangle(p1,p2)
    house.draw(win)
    house.setFill("antique white")

    #Here we calculate the coordinates for the door based on the top center.
    #For ease, I am using a 5 point polygon.
    p3 = win.getMouse()
    x3 = p3.getX()
    y3 = p3.getY()
    p4 = Point(x3 - tenth,y3)
    p5 = Point(x3 + tenth,y3)
    p6 = Point(x3 - tenth,y1)
    p7 = Point(x3 + tenth,y1)

    #Drawing door.
    door = Polygon(p4,p3,p5,p7,p6)
    door.draw(win)
    door.setFill("Dark Red")

    #Now to get and calculate the window, half as wide as the door, or house/10.
    p8 = win.getMouse()
    x8 = p8.getX()
    y8 = p8.getY()
    
    p9 = Point(x8 + (tenth/2), y8 + (tenth/2))
    p10 = Point(x8 - (tenth/2), y8 + (tenth/2))
    p11 = Point(x8 + (tenth/2), y8 - (tenth/2))
    p12 = Point(x8 - (tenth/2),y8 - (tenth/2))

    window = Polygon(p9,p10,p12,p11)
    window.draw(win)
    window.setFill("white")
    
    #Last click is the peak of the roof, which will connect to the top of the house.
    p13 = win.getMouse()
    p14 = Point(x1,y2)

    roof = Polygon(p13,p14,p2)
    roof.draw(win)
    roof.setFill("dim gray")

    #Now a wait function to close the window.
    win.getMouse()
    win.close()

main()
