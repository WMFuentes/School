#cupandball.py

#The game objective is to pick the cup that hides the ball. If the
#right cup is picked, you win.

#by William Fuentes

#pseudocode:
#**DONE** create the play window with 3 upside down cups and a ball (circle).
    #**DONE**two buttons at the bottom, quit and reset game.
    #reset game randomizes the ball.
#place a ball randomly in position 1, 2 or 3.
#upon click, selected cup raises, revealing ball or no ball.
    #if ball is in the position, inciment a win.
    #else inciment a loss.

from graphics import *
from random import randrange

class Cup:
    def __init__(self, pos):
        self.center = position(pos)
        x,y = self.center.getX(), self.center.getY()
        self.xmax, self.xmin = x+3, x-3
        self.ymax, self.ymin = y+3, y-3

    def draw(self,win):
        x = self.center.getX()
        y = self.center.getY()
        self.body = Polygon(Point(x-6,y+7),Point(x+6,y+7),Point(x+8,y-9),Point(x-8,y-9))
        self.body.setFill("red")
        self.body.draw(win)
        self.bottom = Oval(Point(x-8,y-8),Point(x+8,y-9))
        self.bottom.draw(win)

    def clicked(self, p):
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def undraw(self, win):
        self.body.undraw()
        self.bottom.undraw()

class Ball:
    def __init__(self):
        self.center = position(randrange(1,4))
        x,y = self.center.getX(), self.center.getY()
        self.xmax, self.xmin = x+6, x-6
        self.ymax, self.ymin = y+6, y-6

    def draw(self,win):
        self.ball = Circle(self.center, 5)
        self.ball.setFill("green")
        self.ball.draw(win)

    def clicked(self, p):
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def undraw(self, win):
        self.ball.undraw()

class Button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

def position(pos):
    if pos == 1:
        center = Point(20,50)
    elif pos == 2:
        center = Point(50,50)
    elif pos == 3:
        center = Point(80,50)
    return center

def main():
    #create app window
    win = GraphWin("Ball and Cup Game",500,500)
    win.setCoords(0,0,100,100)
    win.setBackground("Light Goldenrod")

    #draw the text
    title1 = Text(Point(50,95), "Click A Cup And")
    title2 = Text(Point(50,90), "Find The Ball!")
    title1.setSize(18)
    title1.draw(win)
    title2.setSize(18)
    title2.draw(win)

    wins = 0
    loss = 0
    wTracker = Text(Point(85,95), "Wins:")
    wCounter = Text(Point(95,95), wins)
    lTracker = Text(Point(85,90), "Losses:")
    lCounter = Text(Point(95,90), loss)
    wTracker.draw(win)
    wCounter.draw(win)
    lTracker.draw(win)
    lCounter.draw(win)

    pos1 = Text(Point(20,70), "1")
    pos1.setSize(24)
    pos1.draw(win)
    pos2 = Text(Point(50,70), "2")
    pos2.setSize(24)
    pos2.draw(win)
    pos3 = Text(Point(80,70), "3")
    pos3.setSize(24)
    pos3.draw(win)

    #draw a random ball
    ball = Ball()
    ball.draw(win)

    #draw the cups
    cup1 = Cup(1)
    cup1.draw(win)
    cup2 = Cup(2)
    cup2.draw(win)
    cup3 = Cup(3)
    cup3.draw(win)

    #draw the quit and reset buttons
    quitButton = Button(win, Point(70,20), 20, 10, "Quit")
    resetButton = Button(win, Point(30,20), 20, 10, "Reset")

    #event loop
    while True:
        pt = win.getMouse()

        if (cup1.clicked(pt) or cup2.clicked(pt) or cup3.clicked(pt)) and ball.clicked(pt):
            cup1.undraw(win)
            cup2.undraw(win)
            cup3.undraw(win)
            wins = wins + 1
            wCounter.undraw()
            wCounter.draw(win)
            print("wins:",wins)
        elif (cup1.clicked(pt) or cup2.clicked(pt) or cup3.clicked(pt)) and not ball.clicked(pt):
            cup1.undraw(win)
            cup2.undraw(win)
            cup3.undraw(win)
            loss = loss + 1
            lCounter.undraw()
            lCounter.draw(win)
            print("losses:",loss)
        elif resetButton.clicked(pt):
            ball.undraw(win)
            del ball
            ball = Ball()
            ball.draw(win)
            cup1.draw(win)
            cup2.draw(win)
            cup3.draw(win)
        elif quitButton.clicked(pt):
            break
    win.close()
    #If cup clicked, undraw cup
    #if ball clicked, incriment win
    #else, inciment loss

    #if resetButton clicked, undraw then draw cups and random ball

    #if quitButton clicked, win.close()

if __name__ == '__main__':
    main()
