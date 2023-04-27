from PIL  import Image
import matplotlib.pyplot as plt
import random

im = Image.new(mode = "RGBA",
                   size = (int(input("width of dungeon:")), int(input("height of dungeon:"))),
                   color = (0, 0, 0, 255))

RoomSize = int(input("Room size:"))
RoomQuanity = int(input("Room quanity:"))
seed = int(input("seed:"))

random.seed(seed)
width, height = im.size

rooms = []
for room in range(RoomQuanity):
    for attempt in range(50):

        x = random.randint(0,width - RoomSize)
        y = random.randint(0,height - RoomSize)
        print(im.getpixel((x - 1,y - 1)))
        if im.getpixel((x - 1,y - 1)) == (255, 255, 255, 255):
            continue
        elif im.getpixel((x + 1,y - 1)) == (255, 255, 255, 255):
            continue
        elif im.getpixel((x - 1,y + 1)) == (255, 255, 255, 255):
            continue
        elif im.getpixel((x + 1,y + 1)) == (255, 255, 255, 255):
            continue

        RoomHeight = random.randint(0,RoomSize)
        RoomWidth = random.randint(0,RoomSize)

        for i in range(RoomWidth):
            for j in range(RoomHeight):
                im.putpixel( (x + i,y + j), (255, 255, 255, 255))
        im.show()

        NewRoom = [x,y]
        rooms.append(NewRoom)
        break

im.show()
