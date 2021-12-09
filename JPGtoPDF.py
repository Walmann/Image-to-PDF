from PIL import Image
from fnmatch import fnmatch
from os import listdir
# Image_List



for file in listdir('.'):
    if file.endswith(('.jpg', '.png')):
        print(file)
        image1 = Image.open(file)
        new_name = file.replace(".jpg","").replace(".png","")
        # im1 = image1.convert('RBG')
        image1.save("./pdf/" + new_name + ".pdf", "PDF" ,resolution=100.0, save_all=True)