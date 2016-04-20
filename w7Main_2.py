import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("green")
wn.bgcolor("black")


t1.penup()
mytracks=list()
t1.goto(-400,300)
mytracks.append(t1.pos())
t1.pendown() 
t1.pencolor("white") 
t1.right(90) 
t1.fd(400)
mytracks.append(t1.pos())
t1.left(90) 
t1.fd(300) 
mytracks.append(t1.pos())
t1.left(90) 
t1.fd(200)  
mytracks.append(t1.pos())
t1.right(90) 
t1.fd(300)
mytracks.append(t1.pos())
t1.right(90)
t1.fd(200)
mytracks.append(t1.pos())

    
return mytracks

for t in mytracks:
    print t
def replayTracks(mytracks):
    for t in mytracks:
        t1.penup()
        t1.pencolor("red")
        t1.goto (t)
        
print replayTracks(mytracks)


def lab7():
    mytracks=saveTracks
    replayTracks(mytracks)
    
def main():
    lab7()

main()
wn.exitonclick()