import os

from PIL import Image

prefix = ""
source_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes marines\\donneesbefore\\entrainement\\requinbaleine"
destination_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes marines\\donneesbefore\\entrainement\\requinbaleine2"

if not os.path.exists(destination_images):
    os.makedirs(destination_images)

size = 256, 256

l = os.listdir(source_images)
# random.shuffle(l)
sequence = 1
for image in l:
    print(image)
    if image == "Shuffled": continue
    im = Image.open(source_images + "\\" + image)
    im.thumbnail(size)
    im_rgb = im.convert('RGB')
    im_rgb.save(destination_images + "\\" + str(sequence).zfill(4) + ".jpg")
    sequence += 1
