import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

# Pure Python HSV-to-RGB conversion (No colorsys library required)
def hsv_to_rgb(h, s_val, v):
    i = int(h * 6)
    f = (h * 6) - i
    p = v * (1 - s_val)
    q = v * (1 - f * s_val)
    t_val = v * (1 - (1 - f) * s_val)
    i %= 6
    if i == 0: return v, t_val, p
    if i == 1: return q, v, p
    if i == 2: return p, v, t_val
    if i == 3: return p, q, v
    if i == 4: return t_val, p, v
    if i == 5: return v, p, q

h = 0
for i in range(160):
    r, g, b = hsv_to_rgb(h, 1, 1)
    t.color(r, g, b)
    h += 0.005
    t.circle(120, 90)
    t.left(90)
    t.circle(120, 90)
    t.left(18)
t.hideturtle()
