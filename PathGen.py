from PIL  import Image
import matplotlib.pyplot as plt
import random

im = Image.new(mode = "RGBA",
                   size = (int(input("width of dungeon:")), int(input("height of dungeon:"))),
                   color = (0, 0, 0, 255))

PathLength = int(input("Path length:"))
seed = int(input("seed:"))

random.seed(seed)
width, height = im.size

direction = [random.randint(-1, 1),random.randint(-1, 1)]
if direction[0] == 0 and direction[1] == 0:
    direction[0] = 1

if direction[0] == -1:
    x = width - 8
elif direction[0] == 0:
    x = int(width/2)
else:
    x = 8

if direction[1] == -1:
    y = height - 8
elif direction[1] == 0:
    y = int(height/2)
else:
    y = 8

Knots = [[x, y]]

while PathLength > 0:

    direction = [random.randint(-1, 1),random.randint(-1, 1)]
    if direction[0] == 0 and direction[1] == 0:
        direction[0] = 1

    if direction[0] == -1:
        x = width - 8
    elif direction[0] == 0:
        x = int(width/2)
    else:
        x = 8

    if direction[1] == -1:
        y = height - 8
    elif direction[1] == 0:
        y = int(height/2)
    else:
        y = 8

    if len(Knots) == 0:
        Knots = [[x, y]]

    cords = Knots[-1]
    x = cords[0]
    y = cords[1]

    for step in range(PathLength):
        if random.randint(0,50) == 1:
            Knots.append([x,y])
        PathLength -= 1

        if x + 4 > width or x - 4 < 0 or y + 4 > height or y - 4 < 0:
            break
        im.putpixel( (x - 1, y - 1), (255, 255, 255, 255))
        im.putpixel( (x    , y - 1), (255, 255, 255, 255))
        im.putpixel( (x + 1, y - 1), (255, 255, 255, 255))
        im.putpixel( (x - 1, y    ), (255, 255, 255, 255))
        im.putpixel( (x    , y    ), (255, 255, 255, 255))
        im.putpixel( (x + 1, y    ), (255, 255, 255, 255))
        im.putpixel( (x - 1, y + 1), (255, 255, 255, 255))
        im.putpixel( (x    , y + 1), (255, 255, 255, 255))
        im.putpixel( (x + 1, y + 1), (255, 255, 255, 255))

        localdirection = [random.randint(-1,1), random.randint(-1,1)]
        if localdirection == direction:
            localdirection[0] *= -1

        x += direction[0] + localdirection[0]
        y += direction[1] + localdirection[1]
        if random.randint(0,100) == 10:
            break



for room in Knots:

    x = room[0]
    y = room[1]

    im.putpixel( (x - 1, y - 1), (255, 0, 0, 255))
    im.putpixel( (x    , y - 1), (255, 0, 0, 255))
    im.putpixel( (x + 1, y - 1), (255, 0, 0, 255))
    im.putpixel( (x - 1, y    ), (255, 0, 0, 255))
    im.putpixel( (x    , y    ), (255, 0, 0, 255))
    im.putpixel( (x + 1, y    ), (255, 0, 0, 255))
    im.putpixel( (x - 1, y + 1), (255, 0, 0, 255))
    im.putpixel( (x    , y + 1), (255, 0, 0, 255))
    im.putpixel( (x + 1, y + 1), (255, 0, 0, 255))

im.show()
