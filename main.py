import colorgram as cg
import turtle as t
import random

# rgb_colors = []
# colors = cg.extract('spot-paint.webp', 6)

# for i in colors:
#     red = i.rgb.r
#     green = i.rgb.r
#     blue = i.rgb.b
#     rgb_tuple = (red, green, blue)

#     rgb_colors.append(rgb_tuple)

rgb_colors = [(233, 233, 232), (231, 231, 237), (235, 235, 233), (224, 224, 227), (207, 207, 82), (54, 54, 130)]

t.colormode(255)
turtle_obj = t.Turtle()
turtle_obj.setheading(180)

for i in range (10):
    turtle_obj.dot(20, random.choice(rgb_colors))
    turtle_obj.forward(50)






screen_obj = t.Screen()
screen_obj.exitonclick()
