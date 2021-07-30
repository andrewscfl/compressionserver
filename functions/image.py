from PIL import Image
import math
import os

def image(file, in_dir, out_dir):
    img = Image.open(in_dir + '/' + file)
    img.save(out_dir + '/' + file, optimize=True, quality=50)
    os.remove(in_dir + '/' + file)
    return
