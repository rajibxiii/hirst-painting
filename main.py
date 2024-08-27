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
turtle_obj.speed("fastest")
turtle_obj.setheading(225)
turtle_obj.forward(300)
turtle_obj.setheading(0)

numberOfDots = 50

for i in range (1, numberOfDots+1):
    turtle_obj.dot(20, random.choice(rgb_colors))
    turtle_obj.forward(50)

    if i % 10 == 0:
        turtle_obj.setheading(90)
        turtle_obj.forward(50)
        turtle_obj.setheading(180)
        turtle_obj.forward(500)
        turtle_obj.setheading(0)



screen_obj = t.Screen()
screen_obj.exitonclick()
