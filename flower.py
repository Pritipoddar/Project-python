import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.hideturtle()

# Turn off automatic drawing animation so frames transition smoothly
s.tracer(0)

# Base Primary and Secondary color categories (Excluding Green)
primary_bases = ["red", "blue", "yellow"]
secondary_bases = ["orange", "purple", "magenta", "cyan"]

def get_random_shade(color_type):
    if color_type == "red":
        return f"#{random.randint(200, 255):02x}{random.randint(0, 40):02x}{random.randint(0, 40):02x}"
    elif color_type == "blue":
        return f"#{random.randint(0, 40):02x}{random.randint(60, 140):02x}{random.randint(200, 255):02x}"
    elif color_type == "yellow":
        return f"#{random.randint(220, 255):02x}{random.randint(200, 245):02x}{random.randint(0, 40):02x}"
    elif color_type == "orange":
        return f"#{random.randint(230, 255):02x}{random.randint(100, 160):02x}{random.randint(0, 30):02x}"
    elif color_type == "purple":
        return f"#{random.randint(140, 200):02x}{random.randint(0, 50):02x}{random.randint(180, 255):02x}"
    elif color_type == "cyan":
        return f"#{random.randint(0, 50):02x}{random.randint(200, 255):02x}{random.randint(220, 255):02x}"
    else: # Magenta / Violet
        return f"#{random.randint(200, 255):02x}{random.randint(0, 80):02x}{random.randint(180, 255):02x}"

# Sequence: Primary Shades -> Secondary Shades -> Final Baby Pink
primary_shades = [get_random_shade(col) for col in primary_bases]
secondary_shades = [get_random_shade(col) for col in secondary_bases]
color_sequence = primary_shades + secondary_shades + ["#F4C2C2"]

def draw_static_flower(color_hex):
    """Draws the entire flower cleanly at a fixed position in a single color"""
    t.clear()
    t.penup()
    t.goto(0, -20)
    t.setheading(0)  # Fixed orientation so it never rotates
    t.pendown()
    t.color(color_hex)

    # Draw all 24 petals in exact fixed alignment
    for _ in range(24):
        t.circle(80, 90)
        t.left(90)
        t.circle(80, 90)
        t.left(15)

    s.update()  # Render frame instantly

def transition_color_phases(step=0):
    if step < len(color_sequence):
        # Update the entire flower's color simultaneously
        draw_static_flower(color_sequence[step])
        # Smoothly move to next color phase every 500ms
        s.ontimer(lambda: transition_color_phases(step + 1), 500)

# Start static blooming color shift
transition_color_phases(0)
