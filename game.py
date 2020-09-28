import turtle as t
import random





window = t.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic('images/background.png')
window.screensize(1200, 800)

def airplane(y):
    pen = t.Turtle()
    if y < 0:
        pen.color('red')
    else:
         pen.color('yellow')
    pen.shape('turtle')
    for current_x in [-200, 0, 200]:
        pen.penup()
        pen.setpos(x=current_x, y=y)
        pen.pendown()
        pen.circle(radius=random.randint(50, 70))
        pen.forward(100)
        #pen.circle(radius=100)

airplane(y=100)
airplane(y=-100)




window.mainloop()







