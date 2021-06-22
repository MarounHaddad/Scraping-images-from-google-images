"""
This file converts the images to jpg
"""

import os

from PIL import Image

prefix = ""
source_images = "D:\\source_images_location"
destination_images = "D:\\destination_images_location"

# create directory if does not exist
if not os.path.exists(destination_images):
    os.makedirs(destination_images)

# Images size
size = 256, 256

# source images location
l = os.listdir(source_images)

# Shuffle images before converting them
# random.shuffle(l)

sequence = 1
for image in l:
    # print image name
    print(image)
    if image == "Shuffled": continue
    im = Image.open(source_images + "\\" + image)
    im.thumbnail(size)
    im_rgb = im.convert('RGB')
    im_rgb.save(destination_images + "\\" + str(sequence).zfill(4) + ".jpg")
    sequence += 1
