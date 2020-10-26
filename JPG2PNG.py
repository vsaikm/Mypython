import sys
import os #or else we import pathlib module
from PIL import Image

#grab the first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if the new folder exists or else create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through the images folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')

#convert the images into png

#save to the new folder


#img = Image.open(r 'images\')
#img.save(r ' new\')
         
