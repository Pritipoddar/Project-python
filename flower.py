import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

# Turn off automatic screen updates for clean color transitions
s.tracer(0)

# Base Primary and Secondary color categories (Excluding Green)
primary_bases = ["red", "blue", "yellow"]
secondary_bases = ["orange", "purple", "magenta", "cyan"]

# Helper function to generate dynamic shades
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

# Generate sequence: Primary Shades -> Secondary Shades -> Baby Pink
primary_shades = [get_random_shade(col) for col in primary_bases]
secondary_shades = [get_random_shade(col) for col in secondary_bases]
color_sequence = primary_shades + secondary_shades + ["#F4C2C2"]  # Final Baby Pink

# Function to draw the complete flower in one single uniform color
def draw_full_flower(color_hex):
    t.clear()
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.color(color_hex)
    
    # Draw all 24 petals in the EXACT same color
    for _ in range(24):
        t.circle(80, 90)
        t.left(90)
        t.circle(80, 90)
        t.left(15)
        
    s.update() # Render the completed flower on screen

# Animate color progression step by step
def animate_color_transition(step=0):
    if step < len(color_sequence):
        draw_full_flower(color_sequence[step])
        # Change color every 600ms
        s.ontimer(lambda: animate_color_transition(step + 1), 600)

# Start animation
animate_color_transition(0)
