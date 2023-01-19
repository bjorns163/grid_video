import os
from PIL import Image, ImageDraw, ImageFont
import shutil

source_folder = r'C:\dglmodules\chatgpt\1-resized'
destination_folder = r'C:\dglmodules\chatgpt\2-nummers'

files = os.listdir(source_folder)
for file_name in files:
    shutil.copy(source_folder + '/' + file_name, destination_folder + '/' + file_name)
i = 1

for filename in os.listdir(destination_folder):
    #print (filename)
    nummer = filename.replace('dgl-102jaar-','').replace('_optimized.jpg','')
    nummer = filename.replace('DGL 102jaar-','').replace('.jpg','')
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(os.path.join(destination_folder, filename))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 50)
        #draw.text((10, image.size[1]-400), str(i), (255, 0, 0), font=font) # unique number
        draw.text((10, image.size[1]-60), str(nummer), (255, 0, 0), font=font) # filename number
        image.save(os.path.join(destination_folder, filename))
        i += 1