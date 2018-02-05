import os
from base64 import b64encode
from os import makedirs
from os.path import join, basename
from sys import argv
import requests

import io

import PIL
from PIL import Image, ImageDraw, ImageFont

#Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

counter_two = 0
client = vision.ImageAnnotatorClient()

for x in range(0, counter +1):
    counter_two += x 
    name = str(counter_two) + '.jpg'

    path = os.getcwd()
    with io.open(path + '/' + name, 'rb') as image_file:
        content = image_file.read();

    image = types.Image(content = content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    

    new = 'new' +str(counter_two)+'.jpg'
    image = Image.open(name)
    draw = ImageDraw.Draw(image)
    y_coordinate = 70
    for item in labels: 
        word = item.description

        y_coordinate += 10
        draw.text((200, y_coordinate), text = word, fill=(250,250,250))


    image.save(new)
    newcommand = "rm " +name;
    os.system(newcommand)


#    Using ffmpeg

os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")