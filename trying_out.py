import turtle as t
t.hideturtle()

def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

def triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

def star():
    for i in range(5):
        t.forward(150)
        t.right(144)

t.pencolor('blue')
t.pensize(10)
t.penup()
t.goto(150, 150)
t.pendown()
square()

t.pencolor('red')
t.penup()
t.goto(-150, 150)
t.pendown()
triangle()

t.pencolor('green')
t.penup()
t.goto(-90, -100)
t.pendown()
star()


screen = t.Screen()
screen.exitonclick()