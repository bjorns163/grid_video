import glob
import cv2
import os
from natsort import natsorted

folder_path = r'C:\dglmodules\chatgpt\3-grid'
destination_folder = r'C:\dglmodules\chatgpt\4-video'
image_files = glob.glob(folder_path + '/*.jpg') + glob.glob(folder_path + '/*.png')
each_image_duration = 10 # in secs

os.chdir(destination_folder)
# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('slideshow3.mp4', fourcc, 1, (1920,853))

image_files = natsorted(image_files) #soort list
#print (image_files)
for img in image_files:
    for _ in range(each_image_duration):
        image = cv2.imread(img)
        image = cv2.resize(image, (1920, 853))
        img_height, img_width = image.shape[:2]
        text = "Een foto digitaal thuis ontvangen? Mail naar 100jaar@degraaflogistics.nl"
        font = cv2.FONT_HERSHEY_DUPLEX
        font_scale = 1
        thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, thickness)
        text_width, text_height = text_size[0]
        text_x = int((img_width - text_width) / 2)
        text_y = int(img_height - text_height - 40)
        color = (0, 255, 0)
        cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness) 
        video.write(image)

video.release()
