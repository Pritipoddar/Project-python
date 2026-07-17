import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

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

# Sequence: Primary Shades -> Secondary Shades -> Baby Pink
primary_shades = [get_random_shade(col) for col in primary_bases]
secondary_shades = [get_random_shade(col) for col in secondary_bases]
color_sequence = primary_shades + secondary_shades + ["#F4C2C2"]

def draw_seed():
    """Draws the center seed (beej) growing before blooming"""
    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def bloom_flower(color_index=0):
    """Animates the flower blooming petal by petal"""
    if color_index >= len(color_sequence):
        return  # Fully bloomed!

    t.clear()
    
    # 1. First, plant/draw the center seed (beej)
    draw_seed()

    # 2. Prepare turtle position for petal blooming
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.color(color_sequence[color_index])

    # 3. Bloom the 24 petals visibly one by one
    total_petals = 24
    for _ in range(total_petals):
        t.circle(80, 90)
        t.left(90)
        t.circle(80, 90)
        t.left(15)

    # 4. Progressively transition to the next blooming color phase
    s.ontimer(lambda: bloom_flower(color_index + 1), 700)

# Start execution: seed grows and blooms into a flower!
bloom_flower(0)
