"""
This file generates a "labels" files with the classes IDs according to the sequence of the iamges
(used in clustering or classification)
"""

import os
import csv

# Source folder of the images
source_images = "D:\\images_source_file"
# labels file to be saved location
labels_file ="D:\\labels.txt"

class1_prefix = "class1_prefix"
class2_prefix = "class2_prefix"

class1 = 0
class2 = 1

# images from source
l = os.listdir(source_images)

# list that will contain the labels.
ground_truth = []

for image_name in l:
    print(image_name)
    if class1_prefix in image_name:
        ground_truth.append(class1)
    elif class2_prefix in image_name:
        ground_truth.append(class2)

# print labels
print(ground_truth)

ground_truth= [int(x) for x in ground_truth]

# save labels (ground truth)  to csv fil
with open(labels_file, 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    wr.writerow(ground_truth)




