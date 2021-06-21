import os
import random
import shutil

prefix = ""
source_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes marines\\donnees\\test\\phoque"
destination_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes marines\\donnees\\test\\phoque"

if not os.path.exists(destination_images):
    os.makedirs(destination_images)

l = os.listdir(source_images)
random.shuffle(l)
sequence = 1
for image in l:
    if image == "Shuffled": continue
    shutil.copyfile(source_images + "\\" + image, destination_images + "\\" + str(sequence).zfill(4) + ".png")
    sequence += 1
    print(image)
