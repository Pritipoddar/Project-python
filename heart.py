import turtle

# Setup screen
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)

# Setup turtle pen (visible arrow drawing animation)
t = turtle.Turtle()
t.shape("turtle")      # Shows the turtle cursor drawing!
t.color("red")
t.speed(3)             # Speed 3 allows you to watch it draw smoothly (1 = slow, 3 = normal, 10 = fast)
t.pensize(3)

# Move pen to center before drawing (penup prevents drawing line during move)
t.penup()
t.goto(0, -100)
t.pendown()

# Draw Heart Shape Step-by-Step
t.begin_fill()
t.fillcolor("red")

t.left(140)
t.forward(180)
t.circle(-90, 200)

t.setheading(60)
t.circle(-90, 200)
t.forward(180)

t.end_fill()

# Keep arrow visible at the end or hide it
t.hideturtle()
