import turtle
import random

wn = turtle.Screen()
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
food.goto(0, 80)

segments = []
score = 0
game_is_over = False

# Score Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Game Over Popup Pen
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.hideturtle()

# Navigation Functions
def go_up():
    if head.direction != "down" and not game_is_over:
        head.direction = "up"

def go_down():
    if head.direction != "up" and not game_is_over:
        head.direction = "down"

def go_left():
    if head.direction != "right" and not game_is_over:
        head.direction = "left"

def go_right():
    if head.direction != "left" and not game_is_over:
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

# Bind Keys
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

def trigger_game_over():
    global game_is_over
    game_is_over = True
    head.direction = "stop"
    
    # Display Game Over Popup Box
    game_over_pen.goto(0, 20)
    game_over_pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
    
    game_over_pen.color("yellow")
    game_over_pen.goto(0, -20)
    game_over_pen.write(f"Final Score: {score}", align="center", font=("Arial", 18, "normal"))

# Game Loop
def game_loop():
    global score, game_is_over

    if game_is_over:
        return  # Stop execution loop completely on game over

    # Screen Border Wraparound
    if head.xcor() > 270: head.setx(-270)
    elif head.xcor() < -270: head.setx(270)
    if head.ycor() > 270: head.sety(-270)
    elif head.ycor() < -270: head.sety(270)

    # Move trailing body segments BEFORE moving the head
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move head forward
    move()

    # Check for body collision (Touching own skin)
    # Skip checking index 0/1 right next to head to avoid false collisions when turning
    if head.direction != "stop":
        for segment in segments[2:]:
            if head.distance(segment) < 15:
                trigger_game_over()
                return

    # Food Collision
    if head.distance(food) < 20:
        food.goto(random.randint(-12, 12) * 20, random.randint(-12, 12) * 20)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

    # Re-call loop every 100 milliseconds
    wn.ontimer(game_loop, 100)

# Start execution
game_loop()
