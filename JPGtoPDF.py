from genericpath import isdir
from PIL import Image
from fnmatch import fnmatch
from os import listdir, mkdir, path

# Image_List


ext = ('.jpg', '.jpeg', '.png')
if not path.isdir("./pdf/"):
    mkdir("./pdf/")

for file in listdir('.'):
    if file.endswith((ext)):
        print(file)
        image1 = Image.open(file)
        new_name = file.replace(".jpg","").replace(".png","").replace(".jpeg","")
        # im1 = image1.convert('RBG')
        image1.save("./pdf/" + new_name + ".pdf", "PDF" ,resolution=100.0, save_all=True)