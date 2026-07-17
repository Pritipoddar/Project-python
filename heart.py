import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(3)
t.color("red")

t.penup()
t.goto(0, -100)
t.pendown()

t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(150)
t.circle(-75, 200)
t.setheading(60)
t.circle(-75, 200)
t.forward(150)
t.end_fill()

t.hideturtle()
