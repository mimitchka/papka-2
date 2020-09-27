import turtle as t
t.shape('turtle')
sides = 3
t.bgcolor('black')
t.pencolor('yellow')
t.pensize(2)

for k in range(6):
    for i in range(sides):
        t.forward(20)
        t.left(360/sides)
    t.left(60)
for k in range(6):
    for i in range(sides):
        t.forward(40)
        t.left(360 / sides)
    t.left(60)
for k in range(6):
    for i in range(sides):
        t.forward(60)
        t.left(360/sides)
    t.left(60)
for k in range(6):
    for i in range(sides):
        t.forward(80)
        t.left(360/sides)
    t.left(60)
for k in range(6):
    for i in range(sides):
        t.forward(100)
        t.left(360/sides)
    t.left(60)
t.penup()
t.forward(350)
t.left(angle=90)
t.pendown()
t.circle(60)



screen = t.Screen()
screen.exitonclick()
t.done