import colorgram as cg

colors = cg.extract('spot-paint.webp', 6)
rgb_colors = []

for i in colors:
    red = i.rgb.r
    green = i.rgb.r
    blue = i.rgb.b
    rgb_tuple = (red, green, blue)

    rgb_colors.append(rgb_tuple)

print(colors)
