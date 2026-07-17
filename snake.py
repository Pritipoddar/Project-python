import turtle
import random

s = turtle.Screen()
s.bgcolor("black")

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lightgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0, 80)

segments = []
score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Score: 0", align="center", font=("Arial", 16, "bold"))

def go_up():
    if head.direction != "down": head.direction = "up"
def go_down():
    if head.direction != "up": head.direction = "down"
def go_left():
    if head.direction != "right": head.direction = "left"
def go_right():
    if head.direction != "left": head.direction = "right"

def move():
    if head.direction == "up": head.sety(head.ycor() + 20)
    if head.direction == "down": head.sety(head.ycor() - 20)
    if head.direction == "left": head.setx(head.xcor() - 20)
    if head.direction == "right": head.setx(head.xcor() + 20)

s.listen()
s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_left, "Left")
s.onkey(go_right, "Right")

def game_loop():
    global score
    
    if head.xcor() > 260: head.setx(-260)
    elif head.xcor() < -260: head.setx(260)
    if head.ycor() > 260: head.sety(-260)
    elif head.ycor() < -260: head.sety(260)

    if head.distance(food) < 20:
        food.goto(random.randint(-10, 10) * 20, random.randint(-10, 10) * 20)
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("green")
        new_seg.penup()
        segments.append(new_seg)
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()
    s.ontimer(game_loop, 120)

game_loop()
