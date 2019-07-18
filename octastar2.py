import turtle
turtle.bgcolor("#24323e")

x = turtle.Turtle()
x.width(5)
x.speed(1)

x.color("#99aef1")
for i in range(8):
    x.color()
    x.forward(50)
    x.left(45)
    x.forward(50)
    x.right(90)
x.penup()
x.forward(42.42+12.935)
x.right(90)
x.forward(12.935)
x.left(90)
x.pendown()
x.width(10)

x.color("#e9a463")
for i in range(8):
    x.forward(60)
    x.right(45)

x.speed(10)
x.color("#e9a463")
for i in range(8):
    x.penup()
    x.forward(22.93)
    x.left(45)
    x.width(7)
    x.pendown()
    x.begin_fill()
    for j in range(4):
        x.forward(10)
        x.right(90)
    x.right(45)
    x.end_fill()
    x.penup()
    x.forward(60-22.93)
    x.right(45)

x.speed(1)
x.penup()
x.back(1)
x.right(90)
x.forward(42)
x.left(90)
x.pendown()
x.width(3)
x.color("#99aef1")
x.begin_fill()
for i in range(8):
    x.forward(18)
    x.left(45)
    x.forward(18)
    x.right(90)
    
x.end_fill()
x.hideturtle()
turtle.done()
