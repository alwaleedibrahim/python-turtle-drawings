import turtle
turtle.bgcolor("#24323e")
turtle.setup(800,600)
x = turtle.Turtle()
x.width(3)
x.speed(5)

def sq(l, c):
    x.color(c)
    for i in range(4):
        x.forward(l)
        x.right(90)

def nestedSq(l, a, b):
    sq(l+20, b)
    x.penup()
    x.forward(10)
    x.right(90)
    x.forward(10)
    x.left(90)
    x.pendown()
    x.begin_fill()
    sq(l, a)
    x.end_fill()
    x.penup()
    x.back(10)
    x.left(90)
    x.forward(10)
    x.right(90)
    x.pendown()
x.penup()
x.right(45)
x.forward(50)
x.pendown()
x.speed(15)
for y in range(4):
    for i in range(8):
        if i != 0:
            x.penup()
            x.forward(50)
            x.right(90)
            x.forward(50)
            x.left(45)               
            x.pendown()
        nestedSq(30, "#e9a463", "#99aef1")
        
    
        
    x.penup()
    x.left(135)
    x.forward(50)
    x.left(90)
    x.back(50)
    x.pendown()
    
x.hideturtle()
turtle.done()

    