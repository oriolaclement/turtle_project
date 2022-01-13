from turtle import*
import turtle as t
t.hideturtle()
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
    end_fill()
    t.Terminator

screen = t.Screen()
screen.exitonclick()
