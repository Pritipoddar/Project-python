import turtle
import random

# Game Settings & Window Setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#1e1e2e")  # Dark sleek background
wn.setup(width=600, height=600)
wn.tracer(0)           # Smooth animation updates

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#a6e3a1")  # Vibrant green
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#f38ba8")  # Soft red/pink
food.penup()
food.goto(0, 100)

segments = []
score = 0

# Score Board UI
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#cdd6f4")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 20, "bold"))

# Movement Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard Bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Main Game Loop
for _ in range(500):
    wn.update()

    # Wrap around borders (Screen wraps like original curses version)
    if head.xcor() > 280:
        head.setx(-280)
    elif head.xcor() < -280:
        head.setx(280)
    if head.ycor() > 280:
        head.sety(-280)
    elif head.ycor() < -280:
        head.sety(280)

    # Check for eating food
    if head.distance(food) < 20:
        # Move food to new random location
        x = random.randint(-13, 13) * 20
        y = random.randint(-13, 13) * 20
        food.goto(x, y)

        # Add a body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#94e2d5")  # Slightly lighter green body
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 20, "bold"))

    # Move body segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Connect first segment to head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self-collision check
    for segment in segments:
        if segment.distance(head) < 10:
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)  # Move off-screen
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: 0", align="center", font=("Courier", 20, "bold"))
