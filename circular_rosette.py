import turtle
turtle.setup(800,600)
x = turtle.Turtle()
turtle.bgcolor("#24323e")
x.speed(10)
x.width(2)
colorList = ["#99aef1", "#e9a463"]
for i in range(6):
    x.color(colorList[i%2])
    x.right(60)
    x.circle(50)    
    
cv = turtle.getcanvas()
cv.postscript(file="file_name.ps", colormode='color')

x.hideturtle()
turtle.done()