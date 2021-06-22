"""
This file takes images from multiple sources and moves them to a new destination
Used for multi-class.
"""
# Libraries
import os
import random
import shutil

# Source class image
source_images = "D:\\source_class_image"

# Destination folder for all shuffled images (example training_folder)
destination_images = "D:\\destination_folder_for_all_images"

# Create destination folder if does not exist
if not os.path.exists(destination_images):
    os.makedirs(destination_images)

l = os.listdir(source_images)
# shuffle images
random.shuffle(l)

sequence_all = 1

sequence_class1 = 1
sequence_class2 = 1

prefix_class1 = "class1_prefix"
prefix_class2 = "class2_prefix"

for image_name in l:
    if image_name == "Shuffled": continue
    elif prefix_class1 in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + prefix_class1 + "_" +  str(sequence_class1) + ".png")
        sequence_class1 += 1
    elif prefix_class2 in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + prefix_class2 + "_" +  str(sequence_class2) + ".png")
        sequence_class2 += 1
    sequence_all += 1
    print(image_name)
