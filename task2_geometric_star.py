import turtle as t

# 1. Setup screen and pen properties [00:00:06]
t.bgcolor("black")
t.speed(0)  # Maximum animation speed [00:00:09]
t.pensize(2)  # Pen width [00:00:11]
t.hideturtle()  # Hide turtle cursor [00:00:51]

# 2. Color list for cycling [00:00:13]
colors = [
    "red",
    "yellow",
    "blue",
    "purple",
    "green",
    "#fe019a",
    "white",
    "cyan",
    "orange",
    "lime",
    "magenta",
    "deepskyblue",
]

distance = 150  # Branch length [00:00:48]

# 3. Nested loops to create rotating multi-colored star arms [00:00:54]
for color in colors:
  t.color(color)  # Change pen color for current layer [00:01:00]

  # 8 points per complete rotation (360 / 8 = 45 degrees) [00:01:06]
  for j in range(8):
    t.left(45)

    # Draw the diamond/rhombus facet [00:01:15]
    for i in range(2):
      t.forward(distance)
      t.left(60)
      t.forward(distance)
      t.left(120)

# Keep the window open until closed manually [00:01:37]
t.done()