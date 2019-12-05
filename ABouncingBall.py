from graphics import *
from random import randrange
class BBall:
    def __init__(self,color,center,dir=1):
        
        self.circle=Circle(center,1)
        self.circle.setFill(color)
        self.direction=dir
        
        

    def draw(self,win):
        self.circle.draw(win)

    def move(self,win):
        
        if self.circle.getCenter().getY()==9:
            self.direction=-1
        elif self.circle.getCenter().getY()==-9:
            self.direction=1
        self.circle.move(0,self.direction)

    def changeColor(self):
        colors=["red","orange","yellow","green","blue","indigo","violet"]
        num=randrange(0,len(colors))
        colorPos=colors[num]
        self.circle.setFill(colorPos)
        
        

    
    
    

def main():
    win=GraphWin("A Bouncing Ball",750,750)
    win.setBackground("tan")
    win.setCoords(-10,-10,10,10)

    c=Point(0,-9)
    bouncyBall=BBall("red",c)
    bouncyBall.draw(win)
    d=Point(5,9)
    downBall=BBall("blue",d)
    downBall.draw(win)
    e=Point(-3,0)
    midUp=BBall("green",e)
    midUp.draw(win)
    f=Point(-6,0)
    midDown=BBall("yellow",f,-1)
    midDown.draw(win)
    
    while win.checkKey()!='q':
        bouncyBall.move(win)
        downBall.move(win)
        midUp.move(win)
        midDown.move(win)
        if win.checkMouse()!=None:
            bouncyBall.changeColor()
            downBall.changeColor()
            midUp.changeColor()
            midDown.changeColor()
            
    win.close()

main()
    
