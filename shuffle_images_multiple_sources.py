import os
import random
import shutil

source_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes Autoencoder\\preparation des donnees\\all\\zebre"
destination_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes Autoencoder\\preparation des donnees\\donnees\\entrainement"

if not os.path.exists(destination_images):
    os.makedirs(destination_images)

l = os.listdir(source_images)
random.shuffle(l)

sequence_all = 1

sequence_antilope = 1
sequence_cerf = 1
sequence_elephant = 1
sequence_girafe = 1
sequence_leopard = 1
sequence_lion = 1
sequence_rhino = 1
sequence_tigre = 1
sequence_zebre = 1

for image_name in l:
    if image_name == "Shuffled": continue
    elif "cerf" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "cerf" + "_" +  str(sequence_cerf) + ".png")
        sequence_cerf += 1
    elif "elephant" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "elephant" + "_" +  str(sequence_elephant) + ".png")
        sequence_elephant += 1
    elif "girafe" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "girafe" + "_" +  str(sequence_girafe) + ".png")
        sequence_girafe += 1
    elif "leopard" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "leopard" + "_" +  str(sequence_leopard) + ".png")
        sequence_leopard += 1
    elif "lion" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "lion" + "_" +  str(sequence_lion) + ".png")
        sequence_lion += 1
    elif "rhino" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "rhino" + "_" +  str(sequence_rhino) + ".png")
        sequence_rhino += 1
    elif "tigre" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "tigre" + "_" +  str(sequence_tigre) + ".png")
        sequence_tigre += 1
    elif "zebre" in source_images:
        shutil.copyfile(source_images + "\\" + image_name,
                        destination_images + "\\" + str(sequence_all).zfill(4) + "_" + "zebre" + "_" +  str(sequence_zebre) + ".png")
        sequence_zebre += 1
    sequence_all += 1
    print(image_name)
