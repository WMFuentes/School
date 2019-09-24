# triangle.pyw
from graphics import *

def main():
    win = GraphWin("Draw Shapes")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    print(p1.getX(), p1.getY())
    circle = Circle (p1, 3)
    p1.draw(win)
    circle.setFill("red")
    circle.draw(win)
    p2 = Point(5, 8)
    #p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    rectangle = Rectangle(p1, p3)
    rectangle.draw(win)


    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
