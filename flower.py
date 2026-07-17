import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(3)  # Visible speed so you see every petal being created!

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

# Start drawing position
t.penup()
t.goto(0, -20)
t.pendown()

total_petals = 24
petals_per_color = max(1, total_petals // len(color_sequence))

# Draw ONE single flower continuously without wiping or yellow dots
for i in range(total_petals):
    # Pick current color phase based on petal progress
    color_idx = min(i // petals_per_color, len(color_sequence) - 1)
    t.color(color_sequence[color_idx])

    # Draw both sides of the petal in the SAME color
    t.circle(80, 90)
    t.left(90)
    t.circle(80, 90)
    t.left(15)  # Angle turn for next petal

t.hideturtle()
