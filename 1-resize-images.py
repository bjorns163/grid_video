import os
from PIL import Image

# Set the source and destination folders
src_folder = r'C:\dglmodules\chatgpt\orgineel'
dst_folder = r'C:\dglmodules\chatgpt\1-resized'

# Iterate through all files in the source folder
for filename in os.listdir(src_folder):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image file
        with Image.open(os.path.join(src_folder, filename)) as img:
            # Calculate the aspect ratio
            width, height = img.size
            aspect_ratio = width / height
            
            # Resize the image
            img = img.resize((int(600 * aspect_ratio), 600))
            
            # Save the image to the destination folder
            img.save(os.path.join(dst_folder, filename))
