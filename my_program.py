import sys
import os
from PIL import Image

#grap first and second argument
f1 = sys.argv[1]
f2 = sys.argv[2]

#check if new/ exists, if not create
file_exists = os.path.exists(f2)
if file_exists:
  print('File already created')

else:
    directory = f2
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

#loop through pokedex
directory2 = f1
for filename in os.listdir(directory2):
        img = Image.open(f'./{directory2}/{filename}')
        clean = os.path.splitext(filename)[0]
        #convert image to png
        img.save(f'{directory}/{clean}.png', 'png')

#save to the new folder