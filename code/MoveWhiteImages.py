"""
Sometimes when downloading images from har, we get empty files (Sometimes not always the case)
This script detects the emtpy files and moves them to a seperate folder to be discarded
"""

# Libraries
from PIL import Image
from os import listdir
from os.path import isfile, join
import shutil

# Source image location
source_images = "D:\\source_images_location"
# White images destination (to be discarded later)
filterd_images = "D:\\white_images_location"

def detect_white_images(image):
    try:
        # Try to open file as image
        im = Image.open(source_images + "\\" + image)
    except:
        # if opening the file is not possible
        #  move the image to the white images folder.
        print(image)
        shutil.move(source_images + "\\" + image, filterd_images + "\\" + image)

image_files = [f for f in listdir(source_images) if isfile(join(source_images, f))]
for image in image_files:
    detect_white_images(image)


