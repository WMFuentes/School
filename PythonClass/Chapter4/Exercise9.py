# Exercise 9 of chapter 4. This program will draw a rectangle
# and print out the area and peremeter of the shape.

#by William Fuentes

from graphics import *

def main():
    win = GraphWin("rectangle", 500,500)
    win.setCoords(0,0,10,10)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rect = Rectangle(p1,p2)
    rect.draw(win)
    
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())

    area = length * width
    peremeter = 2 * (length + width)

    print("Area =",area,", Peremeter =",peremeter,".")

main()
