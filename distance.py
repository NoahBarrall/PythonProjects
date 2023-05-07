#distance.py
#This program will allow us to calculate the sidance between two points


from math import *

from graphics import *


def main():
    win = GraphWin("Distance", 640, 480) #graphwin
    win.setBackground("white")#win color
    
    p1 = win.getMouse() # Pause to view result
    p2 = win.getMouse()
    
    Line(p1, p2).draw(win)
    print("The distance is: ", distance(p1.getX(), p1.getY(), p2.getX(), p2.getY()))

    win.getMouse()

    win.close()    # Close window when done

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
main()
