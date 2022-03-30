import turtle as t
import random

tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
          "SeaGreen"]

direction = [0, 90, 180, 270]

for _ in range(500):
    tim.speed("fastest")
    tim.pensize(10)
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))
