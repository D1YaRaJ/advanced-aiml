import turtle
t=turtle.Turtle()
t.circle(50)
t.penup()
t.goto(0,-50)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.penup()
t.goto(-150,0)
t.pendown()
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
turtle.done()