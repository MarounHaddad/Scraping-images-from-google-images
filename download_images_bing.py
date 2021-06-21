# Libraries
import datetime
import re
import urllib.request as ur
from os import listdir
from os.path import isfile, join

# URL image searcher
# BING
# image_URL = "https://www.bing.com/th?id="
# GOOGLE
image_URL="/images?"

# Image Path location
images_save_path = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes marines\\data orignial\\phoqueoriginal"
# har folder Path location
har_file_Path = "D:\\UNIVERSITY\\Masters\\Assistant\\TPs\\Multi-especes marines\\data orignial\\phoqueoriginal\\har"
# list of har files in the har_file_Path folder
harfiles = [f for f in listdir(har_file_Path) if isfile(join(har_file_Path, f))]

pat = '((http|https)((?!(http|https)).)*?.(jpeg|jpg|png))'
def download_images(harfile, folderindex):
    """ This Function Takes the name of an .har file and the index of the folder in which
    the image will be saved it uses regex to get all the URLs of the images and download them"""
    with open(har_file_Path + "\\" + harfile, 'r', encoding="utf8") as myfile:
        data = myfile.read()
        # urls = re.findall(r'(https?://[^\s]+)', data)
        urls = [x.group() for x in re.finditer(pat,data)]

    index = 0
    for url in urls:
        print(url)
        try:
            url = url.replace("\"", "").replace(",", "")
            # if image_URL not in url:
            #     continue
            print(url)
            datenow: datetime = datetime.datetime.now()
            image_name = images_save_path + "\\" + str(folderindex) + "_" + datenow.strftime(
                '%Y%m%d%H%M%S%f') + "_" + str(index) + ".png"
            ur.urlretrieve(url, image_name)
        except:
            a = 1

        index += 1


folder_Index = 1
# loop through all har files and download them
for harfile in harfiles:
    download_images(harfile, folder_Index)
    print(folder_Index)
    folder_Index += 1
