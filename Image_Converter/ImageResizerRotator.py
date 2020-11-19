import PIL

import glob
from PIL import Image

filepath = r'C:\\Users\\katya\\Desktop\\Test'
new_filepath = r'C:\Users\katya\Desktop\Test'
extension = "\*.jpg"


def imageProcessing(filepath, extension):
    counter = 1
    try:
        for file in glob.iglob(filepath + extension):

            # Open an image
            im = Image.open(file)
            # Rotate and resize an image
            new_im = im.rotate(270).resize((128,128))
            # Save an image in a specific format in a separate directory
            new_im.save(new_filepath + f'\modified\image_resized{counter}.jpg')
            counter += 1
        return "everything is OK"
    except IOError:
        print("cannot convert", file)

print(imageProcessing(filepath, extension))

