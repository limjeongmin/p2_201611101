import random
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.speed(0)
turtle.bgcolor("black")
t1.shape("turtle")
t1.pencolor("green")
colors = ["red", "yellow", "blue","green","orange", "white","gray", "purple"]
for i in range(10):
    t1.pencolor(random.choice(colors))
    size=random.randint(1,10)
    x=random.randrange(0,turtle.window_width()//2)
    y=random.randrange(0,turtle.window_height()//2)
    t1.penup()
    t1.setpos(x,y)
    t1.pendown()
    for s in range(size):
        t1.fd(s*2)
        t1.left(91)
    t1.penup()
    t1.setpos(-x,y)
    t1.pendown()
    for s in range(size):
        t1.fd(s*2)
        t1.right(91)
    t1.penup
    t1.setpos(-x,-y)
    t1.pendown()

    for s in range(size):
        t1.forward(s*2)
        t1.left(91)
        t1.penup()
        t1.setpos(x,-y)
        t1.pendown()
    for s in range(size):
        t1.forward(s*2)
        t1.left(91)
colors=["yellow","orange"]
family=[]
name=turtle.textinput("Eat", "
                      :")
                     
                     
while name !=" ":
    family.append(name)
    name=turtle.textinput("Yummy!","Bonus", "
                          :")
                         
for n in range(100):
    t1.pencolors(colors[n%len(family)])
    t1.penup()
    t1.forward(n*4)
    t1.pendown()
    t1.wrtie(family[n%len(family)])
    t1.left(360/len(family) + 2)