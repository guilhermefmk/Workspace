from graphics import *          
    
def main():
    win=GraphWin("Animação",200,200,autoflush=False)

    a = Circle(Point(0,50),10)
    a.setFill("black")
    a.draw(win)

    b = Circle(Point(0,100),10)
    b.setFill("blue")
    b.draw(win)

    c = Circle(Point(0,150),10)
    c.setFill("red")
    c.draw(win)

    tick=0

    while(tick>=0):

        a.move(1,0)
        b.move(0.5,0)
        c.move(1.5,0)
        
        update(50)
        if win.checkMouse():
            tick=-1
        else:
            tick=tick+1
        
    win.close()

if __name__=="__main__":
    main()
