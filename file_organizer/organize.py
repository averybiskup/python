import os
import shutil

files = [f for f in os.listdir('./') if os.path.isfile(os.path.join('./', f))]


def move_file(src, dest, filename):
    if os.path.isdir(src) and os.path.isdir(dest):
        if shutil.move(src + filename, dest + filename):
            print('File Moved: ' + filename)
        else:
            print('Something went wrong :(')
    elif not os.path.isdir(dest):
        print('No such directory: ' + dest)

IMAGE_EXT = ['.png', '.jpeg', '.jpg']

FILE_MOVED = False

SRC = './'

for f in files:
    filename, ext = os.path.splitext(f)
    ext = ext.lower()   
    print(ext)
    if ext == '.txt':
        move_file(SRC, './txt/', f)
        FILE_MOVED = True
    elif ext in IMAGE_EXT:
        move_file(SRC, './image/', f)
        FILE_MOVED = True
    elif ext == '.pdf':
        move_file(SRC, './pdf/', f)
    elif ext == '.docx':
        move_file(SRC, './docx', f)
    
if not FILE_MOVED:
    print('ALL CLEAN')
