import turtle
turtle.bgcolor('black')
p=turtle.Turtle()
wn=turtle.screen()
p.pencolor('red')
p.hideturtle()

def curve01(a,d):
    for i in range(d):
        p.right(a)
        p.forward(1)

p.width(15)
p.pen()
p.right(90)
p.forward(85)
p.left(90)
p.forward(35)
p.pendown()
p.fillcolor('white')
p.begin_fill()
p.left(55)
curve01(0.0,100)
curve01(0.2,100)
p.forward(70)
p.right(90)
curve01(00,30)
curve01(0.3,50)
curve01(0.6,50)
p.forward(50)
p.right(47)
curve01(0.1,95)
p.end_fill()

p.penup()
p.left(36)
p.forward(70)
p.pendown()


def curve02(a,d):
    for i in range(d):
        p.left(a)
        p.forward(1)
   

p.fillcolor("white")
p.begin_fill()
p.right(55)
curve02(0.09,100)
curve02(0.2,100)
p.forward(70)
p.left(90)
curve02(0.5,100)
curve02(00,30)

p.width(15)
p.pen()
p.left(90)
p.forward(85)
p.right(90)
p.forward(35)
p.pendown()
p.fillcolor('white')
p.begin_fill()
p.right(55)
curve02(0.0,100)
curve02(0.2,100)
p.forward(70)
p.left(90)
curve02(00,30)
curve02(0.3,50)
curve02(0.6,50)
p.forward(50)
p.right(47)
curve02(0.1,95)
p.end_fill()

p.penup()
p.left(36)
p.forward(70)
p.pendown()



