import os, sys
from PIL import Image, ImageDraw

block = Image.open('block.jpg')
block_width, block_height = block.size
apple_num_frames = 2589 #the bad apple rendered in 15 fps has 2589 frames
print("Rendering...")

for k in range(apple_num_frames):
    b = len(str(k))-1 #1-9 returns 0, 10-99 returns 1, 100-999 returns 2...
    zero = "0"*(5-b) #Sony vegas image sequences are name_000000
    name = "a_"+zero + str(k) #an example of name is a_000123 (frame 123)

    board = Image.open('board.jpg') #the background image
    source = Image.open("apple/"+name+".jpeg") #the source image
    pix = source.load() #load pixels info
    width, height = source.size
    x_res = 20 #check pixels every (width/x_res) pixels, x_res times in total.
    y_res = 10 #check vertical pixels every (height/y_res) pixels y_res times.

    for x in range(x_res):
        for y in range(y_res):
            tup = pix[x*(width//x_res),y*(height//y_res)]
            if tup[0] >= 128: #0 is black, 255 is white so 128 is gray
                board.paste(block,(x*block_width,y*block_height), block)
    board.save('end/'+name+'.jpg')

print("Done!")
