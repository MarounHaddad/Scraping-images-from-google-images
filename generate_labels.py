import os
import random
import shutil
import csv


source_images ="D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes Autoencoder\\preparation des donnees\\donnees\\entrainement"
labels_file ="D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes Autoencoder\\preparation des donnees\\ground_truth.txt"


l = os.listdir(source_images)
# l.sort(key=lambda x: int(x.split("_")[0]))
ground_truth = []
for image_name in l:
    print(image_name)
    if "antilope" in image_name:
        ground_truth.append(0)
    elif "cerf" in image_name:
        ground_truth.append(1)
    elif "elephant" in image_name:
        ground_truth.append(2)
    elif "girafe" in image_name:
        ground_truth.append(3)
    elif "leopard" in image_name:
        ground_truth.append(4)
    elif "lion" in image_name:
        ground_truth.append(5)
    elif "rhino" in image_name:
        ground_truth.append(6)
    elif "tigre" in image_name:
        ground_truth.append(7)
    elif "zebre" in image_name:
        ground_truth.append(8)

print(ground_truth)

ground_truth= [int(x) for x in ground_truth]

with open(labels_file, 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    wr.writerow(ground_truth)


