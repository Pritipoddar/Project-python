import turtle

# Setup screen explicitly for Skulpt canvas
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)

# Setup turtle pen
t = turtle.Turtle()
t.pensize(2)
t.color("green")
t.speed(0)

# Position turtle at the bottom-center of the canvas pointing UP
t.penup()
t.goto(0, -220)
t.setheading(90)  # Face upward
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

tree(80)
t.hideturtle()
