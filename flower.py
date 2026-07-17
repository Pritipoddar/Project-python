import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

# Start centered with smaller radius
t.penup()
t.goto(0, 0)
t.pendown()

colors = ["red", "purple", "blue", "green", "yellow", "orange"]

for i in range(120):
    t.color(colors[i % 6])
    t.circle(70, 90)
    t.left(90)
    t.circle(70, 90)
    t.left(15)

t.hideturtle()
