import turtle as tur
import random as r
import colorsys as cs
wn=tur.Screen()
wn.setup(1200,680)
wn.bgcolor("black")
t=tur.Turtle()
t.speed(50)
t.hideturtle()
hue=0.0

for i in range(10):
    x=r.randint(0,350)
    y=r.randint(0,350)
    t.penup()
    t.goto(x,y)
    t.pendown()

    size=r.randint(10,200)
    for i in range(36):
        color=cs.hsv_to_rgb(hue,1,1)
        t.pencolor(color)
        t.fd(size)
        t.bk(size)
        t.left(10)
        hue+=0.01
def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    style=('Stencil std',100,'italic')
    t.write(message,font=style)

write("happy diwali",(-380,0))
wn.mainloop()


