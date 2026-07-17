import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.hideturtle()

# Disable auto-animation so full petals appear instantly per step
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

# Build Color Sequence: Primaries -> Secondaries -> Final Baby Pink
primary_shades = [get_random_shade(col) for col in primary_bases]
secondary_shades = [get_random_shade(col) for col in secondary_bases]
color_sequence = primary_shades + secondary_shades + ["#F4C2C2"]

total_petals = 24
petals_per_color = max(1, total_petals // len(color_sequence))

def bloom_step(current_petal=1):
    if current_petal > total_petals:
        return  # Flower fully bloomed!

    t.clear()  # Re-render active flower structure so ALL petals match current color phase
    t.penup()
    t.goto(0, -20)
    t.pendown()

    # Determine current phase color (All petals match this exact color)
    color_idx = min((current_petal - 1) // petals_per_color, len(color_sequence) - 1)
    t.color(color_sequence[color_idx])

    # Draw all blooming petals up to current_petal as whole complete petals
    for i in range(current_petal):
        t.circle(80, 90)
        t.left(90)
        t.circle(80, 90)
        t.left(15)

    s.update()  # Render complete frame instantly

    # Schedule next petal bloom with color shift
    s.ontimer(lambda: bloom_step(current_petal + 1), 250)

# Start continuous bloom
bloom_step(1)
