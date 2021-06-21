from PIL import Image
from os import listdir
from os.path import isfile, join
import numpy as np
import shutil

source_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi especes\\preparation des donnees\\images\\zebre"
filterd_images = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi especes\\preparation des donnees\\images\\zebre\\filtered"

def detect_white_images(image):
    try:
        im = Image.open(source_images + "\\" + image)
        # pixels = np.asarray(im.getdata())
        # n_white_pix = np.sum(pixels == 255)
        # if (n_white_pix / float(len(pixels))) >= 0.2:
        #     print(str(image))
            # shutil.move(source_images + "\\" + image, filterd_images + "\\" + image)
    except:
        print(image)
        shutil.move(source_images + "\\" + image, filterd_images + "\\" + image)

harfiles = [f for f in listdir(source_images) if isfile(join(source_images, f))]
for image in harfiles:
    detect_white_images(image)


