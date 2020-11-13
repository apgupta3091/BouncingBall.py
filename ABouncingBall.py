#import the graphics library
from graphics import *
#import randrange from the random library
from random import randrange

# BBall class created to create different balls of different color/location
class BBall:
    def __init__(self,color,center,dir=1):
        
        self.circle = Circle(center,1)
        self.circle.setFill(color)
        self.direction = dir
   
    #Function draws the circle/balls in the window
    def draw(self,win):
        self.circle.draw(win)
        
    #Function moves the ball within the window 
    def move(self,win):
        # If the center of the Y of the circle is = 9 or -9, then set self.direction to 1 or -1
        #else keep the self.direction as 1
        if self.circle.getCenter().getY() == 9:
            self.direction = -1
        elif self.circle.getCenter().getY() == -9:
            self.direction = 1
        self.circle.move(0,self.direction)
        
    # Function changes the color of the balls based on the random position generated in the num variable
    def changeColor(self):
        colors = ["red","orange","yellow","green","blue","indigo","violet"]
        randomNum = randrange(0,len(colors))
        colorSelected = colors[randomNum]
        self.circle.setFill(colorSelected)

#Start Main loop        
def main():
    #Creates the graphics window with the title A Bouncing Ball with the coordinates mentioned below
    win = GraphWin("A Bouncing Ball",750,750)
    win.setBackground("tan")
    win.setCoords(-10,-10,10,10)
    
    #Creates each ball of different colors from the BBall class and draws them into the window
    firstBallCenter = Point(0,-9)
    firstBall = BBall("red",c)
    firstBall.draw(win)
    
    secondBallCenter = Point(5,9)
    secondBall = BBall("blue",d)
    secondBall.draw(win)
    
    thirdBallCenter = Point(-3,0)
    thirdBall = BBall("green",e)
    thirdBall.draw(win)
    
    fourthBallCenter = Point(-6,0)
    fourthBall = BBall("yellow",f,-1)
    fourthBall.draw(win)
    
    #While loop that checks if the user has clicked the letter 'q'
    #If clicked, then the window will be closed
    #If not clicked then the balls will be in continuos motion in the window
    while win.checkKey()!='q':
        firstBall.move(win)
        secondBall.move(win)
        thirdBall.move(win)
        fourthBall.move(win)
        
        #If the mouse is clicked, then the balls will randomly change color with the changeColor() function
        #else nothing will change with the balls when the mouse isn't clicked
        if win.checkMouse()!=None:
            firstBall.changeColor()
            secondBalll.changeColor()
            thirdBall.changeColor()
            fourthBall.changeColor()
            
    win.close()
#close main
main()
    
