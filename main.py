import sys
import time
import configparser
import cv2
import numpy as np
import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

def load_config(file):
    global config
    config = config.ConfigParser()
    config = config.read("~/.config/suicide/config.ini")

flags = [flags for flags in sys.argv[1:] if flags.startswith("-")]
args = [args for args in sys.argv[1:] if not args.startswith("-")]

cutoff = float(args[0]) * 60

stream = cv2.VideoCapture(0)

def transcend(cutoff, stream, mode, dest=None)
    flow, frame =  stream.read()
    start = time.time()
    while float((time.time() - start)) < cutoff and flow:
         flow, frame = stream.read()
    if mode == 'w':
        cv2.imwrite(dest, frame)
    else:
        return frame

def dankness(img):
    # Load config variables 
    top = config["USR_DEF"]["top"]
    bottom = config["USR_DEF"]["bottom"]
    font = config["USR_DEF"]["font"]
    font_size = int(config["USR_DEF"]["font-size"]
    font = ImageFont.truetype(font, font_size)
    h, w = img.shape[1::-1]
    w = w/2
    # Add text 
    draw = ImageDraw.Draw(img)
    draw.text((position('t', top, h, w, img), top, font=font, fill='rgb(0, 0, 0)')
    draw.text((position('b', bottom. h. w. img), bottom, font=font, fill='rgb(0, 0, 0)') 
    return img

def position(place, text, h, w, img):
    draw = ImageDraw.Draw(img)
    width_text, height_text = draw.textsize(text, font)

    offset_x, offset_y = font.getoffset(text)
    width_text += offset_x
    height_text += offset_y

    top_left_x = w / 2 - width_text / 2
    if place == 't':
        top_left_y = 100 - height_text / 2
    elif place == 'b':
        top_left_y = (h-100) - height_text / 2
    xy = top_left_x, top_left_y
    return xy

def discord(img):
    

