import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.color("red")

# Center and scale properly for browser view
t.penup()
t.goto(0, -100)
t.pendown()

t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
t.hideturtle()
