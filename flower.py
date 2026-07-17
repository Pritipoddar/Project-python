import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

# Start centered
t.penup()
t.goto(0, -20)
t.pendown()

# Base Primary and Secondary colors (Excluding Green as requested)
primary_bases = ["red", "blue", "yellow"]
secondary_bases = ["orange", "purple", "magenta", "violet", "cyan"]

# Helper function to generate a random hex shade from base colors
def get_random_shade(color_type):
    # Generates vibrant shades while avoiding green tones
    if color_type == "red":
        return f"#{random.randint(200, 255):02x}{random.randint(0, 50):02x}{random.randint(0, 50):02x}"
    elif color_type == "blue":
        return f"#{random.randint(0, 50):02x}{random.randint(50, 120):02x}{random.randint(200, 255):02x}"
    elif color_type == "yellow":
        return f"#{random.randint(220, 255):02x}{random.randint(200, 240):02x}{random.randint(0, 50):02x}"
    elif color_type == "orange":
        return f"#{random.randint(230, 255):02x}{random.randint(100, 160):02x}{random.randint(0, 30):02x}"
    elif color_type == "purple":
        return f"#{random.randint(140, 200):02x}{random.randint(0, 50):02x}{random.randint(180, 255):02x}"
    elif color_type == "cyan":
        return f"#{random.randint(0, 50):02x}{random.randint(200, 255):02x}{random.randint(220, 255):02x}"
    else: # Magenta / Violet
        return f"#{random.randint(200, 255):02x}{random.randint(0, 80):02x}{random.randint(180, 255):02x}"

# Create a sequence of colors for each full petal layer
# 1. Primary shades
primary_shades = [get_random_shade(col) for col in primary_bases]
# 2. Secondary shades
secondary_shades = [get_random_shade(col) for col in secondary_bases]

# Combine: Primaries -> Secondaries -> Final Baby Pink layer
color_palette = primary_shades + secondary_shades + ["#F4C2C2"] # Baby Pink

# Total petals and petals per color phase
total_petals = 24
petals_per_layer = max(1, total_petals // len(color_palette))

for i in range(total_petals):
    # Determine the color for the entire petal layer
    color_index = min(i // petals_per_layer, len(color_palette) - 1)
    t.color(color_palette[color_index])

    # Draw one full petal (both sides) in the same color
    t.circle(80, 90)
    t.left(90)
    t.circle(80, 90)
    t.left(15)  # Rotate for the next petal position

t.hideturtle()
