import turtle
tu=turtle.Turtle()
turtle.hideturtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color("green")
tu.left(90)
tu.backward(100)
tu.speed(400)
tu.shape("turtle")
def tree(i):
    if i<10:
        return
    else:
        tu.forward(i)
        tu.color("red")
        tu.circle(2)
        tu.color("brown")
        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)
tree(100)
turtle.done()
