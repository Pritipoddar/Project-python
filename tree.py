import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.color("green")
t.speed(0)

t.penup()
t.goto(0, -200)
t.setheading(90)
t.pendown()

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color("brown")
        t.left(30)
        tree(3 * i / 4)
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        t.backward(i)

tree(70)
t.hideturtle()
