import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def drawSquareAtSave(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks
print drawSquareAtSave(100,(0,0))

def savedot():
    tu=((100,0),(100,100),(0,100),(0,0))
    
def drawSquareFrom(tracks):
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        t1.goto(tracks[i])
        
def lab7a():
    mytrackA=drawSquareAt(100,(0,0))
    print mytrackA
def lab7b():
    mytrackB=drawSquareFrom(tu)
    print mytrackB
def main():
    drawSquareFrom()