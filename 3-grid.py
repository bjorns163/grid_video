import glob
import cv2
import os
import numpy as np
from natsort import natsorted 

source_folder = r'C:\dglmodules\chatgpt\2-nummers'
destination_folder = r'C:\dglmodules\chatgpt\3-grid'
image_files = glob.glob(source_folder + '/*.jpg') + glob.glob(source_folder + '/*.png')
images = []
i = 0
os.chdir(destination_folder)
image_files = natsorted(image_files) #soort list
for img in image_files:
    images.append(cv2.imread(img))
    if len(images) == 6:
        image_height = max([img.shape[0] for img in images])
        image_width = max([img.shape[1] for img in images])

        grid_height = image_height * 2
        grid_width = image_width * 3

        grid_image = 255 * np.ones((grid_height, grid_width, 3), np.uint8)

        x_offset = 0
        y_offset = 0

        for img in images:
            grid_image[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
            x_offset += image_width
            if x_offset >= grid_width:
                x_offset = 0
                y_offset += image_height
        cv2.imwrite(f"grid_image{i}.jpg", grid_image)
        i += 1
        images = []