import turtle
import random

# Screen Setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lightgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0, 100)

segments = []
score = 0

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Score: 0", align="center", font=("Arial", 18, "bold"))

# Movement controls
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
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Key bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Main Game Loop function using ontimer (Browser Friendly!)
def game_loop():
    global score
    
    # Border wrapping
    if head.xcor() > 280: head.setx(-280)
    elif head.xcor() < -280: head.setx(280)
    if head.ycor() > 280: head.sety(-280)
    elif head.ycor() < -280: head.sety(280)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-12, 12) * 20
        y = random.randint(-12, 12) * 20
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check body collision
    for segment in segments:
        if segment.distance(head) < 10:
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: 0", align="center", font=("Arial", 18, "bold"))

    # Keep loop running every 100ms
    wn.ontimer(game_loop, 100)

# Start game loop
game_loop()
