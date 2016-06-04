import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.shape("turtle")
t1.color("green")
turtle.bgcolor("black")
t2.color("white")
oldhead=t1.heading()
def giyuk(size):
    t2.fd(size)
    t2.right(90)
    t2.fd(size)
def line(size):
    t2.fd(size)
def Maze():
    t2.speed(20)
    t2.penup()
    t2.goto(-350,300)
    t2.pendown()
    t2.goto(350,300)
    t2.penup()
    t2.goto(350,250)
    t2.pendown()
    t2.goto(350,50)
    t2.penup()
    t2.pendown()
    t2.goto(350,250)
    t2.penup()
    t2.goto(350,-0)
    t2.pendown()
    t2.goto(350,-250)
    t2.penup()
    t2.goto(350,-300)
    t2.pendown()
    t2.goto(-350,-300)
    t2.goto(-350,250)
    giyuk(100)
    t2.penup()
    t2.goto(-350,100)
    t2.pendown()
    t2.setheading(0)
    line(150)
    t2.penup()
    t2.goto(-350,0)
    t2.pendown()
    line(300)
    t2.penup()
    t2.goto(-100,0)
    t2.pendown()
    t2.setheading(90)
    line(170)
    t2.penup()
    t2.goto(0,300)
    t2.pendown()
    t2.right(180)
    line(200)
    t2.penup()
    t2.goto(-350,-250)
    t2.setheading(0)
    t2.pendown()
    line(100)
    t2.left(90)
    line(200)
    t2.penup()
    t2.goto(-250,-150)
    t2.setheading(0)
    t2.pendown()
    line(50)
    t2.penup()
    t2.goto(-150,-300)
    t2.setheading(90)
    t2.pendown()
    line(200)
    t2.penup()
    t2.goto(50,-300)
    t2.pendown()
    line(400)
    t2.penup()
    t2.goto(250,300)
    t2.pendown()
    t2.right(180)
    line(75)
    t2.penup()
    t2.goto(350,150)
    t2.right(90)
    t2.pendown()
    line(200)
    t2.penup()
    t2.goto(50,50)
    t2.pendown()
    t2.left(180)
    line(125)
    t2.penup()
    t2.goto(350,0)
    t2.pendown()
    t2.right(180)
    line(180)
    t2.penup()
    t2.goto(200,0)
    t2.left(90)
    t2.pendown()
    line(200)
    t2.penup()
    t2.goto(120,-300)
    t2.left(180)
    t2.pendown()
    line(100)
    t2.penup()
    t2.goto(250,-100)
    t2.right(90)
    t2.pendown()
    line(100)
    t2.penup()
    t2.right(180)
    t2.goto(350,-250)
    t2.pendown()
    line(100)
    t1.penup()
    t1.goto(-350,300)
    t1.pendown()
    t2.penup()

def giyuk(size):
    t2.fd(size)
    t2.right(90)
    t2.fd(size)
def line(size):
    t2.fd(size)
    
def rspPlay(): 
    u1=raw_input(" r,s or p : ")
    u2=raw_input(" r,s or p : ")
    if u1 == u2: 
        res="draw" 
    elif u1 == 'scissor': 
        if u2 == 'rock': 
            res="rock won." 
        else: 
            res="scissor won." 
    elif u1 == 'rock': 
        if u2 == 'paper': 
            res="paper won." 
        else: 
            res="rock won." 
    elif u1 == 'paper': 
        if u2 == 'rock': 
            res="paper won." 
        else: 
            res="scissor won." 
    else: 
        res="Error: select one of scissor, rock or paper!" 
    print res
    
def highlowgame():
    import random
    guessesTaken = 0
    myName = raw_input("Hi!, what is your name? : ") 
    number = random.randint(1,200)
    print('well, '+ myName + ', I am thinking of a number 1 and 200.')
    while guessesTaken < 10:
        print ('Taken a guess')
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < number:
            print ('Your guess is too low')
        if guess > number:
            print ('Your guess is too high')
        if guess == number:
            print ('That is right')
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print ('Great, ' + myName + '! You guessed my number in' + guessesTaken +'guesses!')
    
    if guess != number:
        number = str(number)
        print ('Nope. The number I was thinking of was ' + number)

def drawSquareFill(size, color): 
    t2.goto(350,300)
    angle = 90 
    t2.fillcolor("skyblue") 
    t2.begin_fill() 
    for side in range(4): 
        t2.left(angle)
        t2.forward(size)  
    t2.end_fill() 
    
def drawCircleFill(size, color):
    t2.goto(400,-250)
    t2.pendown()
    t2.begin_fill()
    t2.circle(25)
    t2.fillcolor("yellow")   
    t2.end_fill() 
    
def drawHexagonFill(size,color):
    t2.penup()
    t2.goto(400,50)
    t2.pendown()
    t2.fillcolor("orange") 
    t2.begin_fill()
    def draw(size,n):
        for i in range(n):
            degree=360/n
            t2.forward(size)
            t2.left(degree)
    draw(30,6)
    t2.end_fill()
    
def isInSquare(curpos,coord): 
    xs=coord[0][0] 
    xe=coord[1][0] 
    ys=coord[0][1] 
    ye=coord[1][1] 
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye 

def isInCircle(center,radius,pos): 
    c=center 
    return 0<(math.sqrt(math.pow(c[0]-pos[0],2)+ math.pow(c[1]-pos[1],2)))<(radius) 
def keyup(): 
    t1.forward(30) 
    pt=t1.pos() 
    if isInSquare(pt,((350,200),(450,300))):
        t1.write(" Let's Play rsp!! ")
        rspPlay()
    elif isInCircle((375,10),30,pt):
        t1.write("!Game over!")
    elif isInCircle((375,-275),25,pt): 
        t1.write(" Let's play highlowgame! ")
        highlowgame()
def keyleft(): 
    t1.left(45) 
def keyright(): 
    t1.right(45) 
def keydown(): 
    t1.backward(30) 
    pt=t1.pos() 
    if isInSquare(pt,((350,200),(450,300))):
        t1.write(" Let's Play rsp!! ")
        rspPlay()
    elif isInCircle((375,10),40,pt):
        t1.write("!Game over!")
    elif isInCircle((375,-275),25,pt): 
        t1.write(" Let's play highlowgame! ")
        highlowgame()
        
def addKeys(): 
    wn.onkey(keyup, "Up") 
    wn.onkey(keyleft, "Left") 
    wn.onkey(keyright, "Right") 
    wn.onkey(keydown, "Down") 
    wn.onkey(wn.bye, "q") 

def MinGame(): 
    Maze() 
    drawSquareFill(100,"skyblue")
    drawCircleFill(25,"yellow")
    drawHexagonFill(50,"orange")
    addKeys() 
    wn.listen() 
    turtle.mainloop() 

def main(): 
    MinGame() 

if __name__=="__main__": 
    main()  

