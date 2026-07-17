import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.hideturtle()

# Turn off auto-tracer for instant individual petal rendering
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

# Build Color Palette: Primary Shades -> Secondary Shades -> Baby Pink
primary_shades = [get_random_shade(col) for col in primary_bases]
secondary_shades = [get_random_shade(col) for col in secondary_bases]
color_sequence = primary_shades + secondary_shades + ["#F4C2C2"]

total_petals = 24
petals_per_color = max(1, total_petals // len(color_sequence))

def generate_blooming_flower(petal_count=1):
    if petal_count > total_petals:
        return  # Fully bloomed!

    t.clear()
    
    # Determine the color phase for this current stage of blooming
    color_idx = min((petal_count - 1) // petals_per_color, len(color_sequence) - 1)
    current_color = color_sequence[color_idx]

    # Draw all petals created so far in the exact same uniform color
    for i in range(petal_count):
        t.penup()
        t.goto(0, -20)
        t.setheading(i * 15)  # Lock fixed angle per petal position so it never spins
        t.pendown()
        t.color(current_color)

        # Draw full single petal
        t.circle(80, 90)
        t.left(90)
        t.circle(80, 90)

    s.update()  # Refresh frame

    # Add next petal after 180ms delay
    s.ontimer(lambda: generate_blooming_flower(petal_count + 1), 180)

# Start generating the flower petal by petal
generate_blooming_flower(1)
