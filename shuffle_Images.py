"""This file shuffles the images and readjusts the labels according to the new order"""

# Libraries
import os
import random
import shutil

# Prefix to be used on the images (for the class in case of multi-class)
prefix = ""

# source images location
source_images = "D:\\source_images_location"

# Shuffled images destination
destination_images = "D:\\shuffled_images_destination"

# If destination folder does not exist (Create it)
if not os.path.exists(destination_images):
    os.makedirs(destination_images)

# Get all images in the source location
l = os.listdir(source_images)
# Shuffle images
random.shuffle(l)
sequence = 1
for image in l:
    if image == "Shuffled": continue
    # Copy image to new location
    shutil.copyfile(source_images + "\\" + image, destination_images + "\\" + str(sequence).zfill(4) + ".png")
    sequence += 1
    print(image)
