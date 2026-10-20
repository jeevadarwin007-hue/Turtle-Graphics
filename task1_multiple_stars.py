import random
import turtle

# Screen configuration
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Task 1: Multiple Colorful Stars")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.hideturtle()


# Basic function to draw a single 5-pointed star
def draw_star(x, y, size, fill_color):
  # Pen control: lift pen so it does not draw while moving
  t.penup()
  t.goto(x, y)
  t.pendown()

  # Set color and begin fill
  t.color(fill_color)
  t.fillcolor(fill_color)
  t.begin_fill()

  # 5-pointed star requires a 144-degree turn at each corner
  for _ in range(5):
    t.forward(size)
    t.right(144)

  t.end_fill()


# List of vibrant colors
colors = [
    "#FF5733",
    "#33FFCE",
    "#FF33F6",
    "#F3FF33",
    "#3380FF",
    "#FF8333",
    "#A833FF",
]

# Loop to draw multiple stars in different colors and positions
positions = [
    (-250, 150),
    (-100, 200),
    (100, 180),
    (250, 120),
    (-200, -50),
    (0, 0),
    (200, -80),
    (-150, -200),
    (120, -180),
]

for i, (x, y) in enumerate(positions):
  chosen_color = colors[i % len(colors)]
  star_size = random.randint(40, 75)
  draw_star(x, y, star_size, chosen_color)

turtle.done()