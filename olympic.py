import turtle as to
to.hideturtle()
to.pensize(5)

to.color('blue')
to.penup()
to.goto(-110, -25)
to.pendown()
to.circle(45)

to.color('black')
to.penup()
to.goto(0, -25)
to.pendown()
to.circle(45)

to.color('red')
to.penup()
to.goto(110, -25)
to.pendown()
to.circle(45)

to.color('yellow')
to.penup()
to.goto(-55, -75)
to.pendown()
to.circle(45)

to.color('green')
to.penup()
to.goto(55, -75)
to.pendown()
to.circle(45)

screen = to.Screen()
screen.exitonclick()