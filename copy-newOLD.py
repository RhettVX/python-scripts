import sys
import os
import re
import shutil

modes = {
    'models': r'\.dme',
	'materials': r'\.dma',
	'collisions?': r'\.(cdt|apx|dmv)',
    'textures': r'((?<!LOD\d)\.dds|\.tga)',
    'zones': r'\.((zone|vnfo|cnk.|tome)|areas\.xml)',
    'data': r'\.(xml|txt)',
    'scripts': r'(\.lua|scripts.txt)',
    'audio': r'.*\.(fsb|wav)',
    'images': r'\.(png|jpe?g|bmp)',
    'maps': r'\w*_Tile.*(LOD\d|\d_\d)*.*\.(dds|txt)',
    'nameless': r'\.bin',
    'scaleform': r'\.gfx',
	'actordefs': r'\.adr',
    'all':  r''
    }

dst_dir = 'DiffFiles-'
new_files = []

def menu(loc):
    for i in range(len(modes)):
        print(f'[{i}]: {list(modes.keys())[i]}')

    mode = list(modes.keys())[int(input('Choose a mode >'))]
    folder = mode
    
    if not os.path.exists(dst_dir+folder):
        os.makedirs(dst_dir+folder)
        
    for root, dirs, files in os.walk(loc):
        for file in files:
            if re.search(r'.*'+modes[mode], file, re.I):
                #if file in new_files:
                print(file)
                shutil.copy(root+'\\'+file, dst_dir+folder+'\\')
    

def main():
    #with open('diff-files.txt', 'r') as in_file:
    #    for line in in_file:
    #        new_files.append(line.strip('\n'))

    loc = os.path.abspath(input('Unpacked files location >'))
    while True:
        menu(loc)

if __name__ == '__main__':
    main()
