import os
import sys

from pathlib import Path
from PIL import Image
from pprint import pprint

# Flip finished
# Auto find correct size

offset = 4096
path = Path(sys.argv[1])

with path.open() as in_file:
    data = []
    images = []

    total_w = 0
    total_h = 0
    
    for line in in_file:
        data.append(line.strip().split('\t'))

for grp in data:
    print(grp[0])
    images.append(grp[0])
    total_w += int(grp[6])
    total_h += int(grp[7])

output_img = Image.new('RGB', (4096*2, 4096*2))
for i, x in enumerate(images):
    im = Image.open(path.parent / x)
    output_img.paste(im, (int(float(data[i][3]))+offset, int(float(data[i][1])+offset)))
    #print(output_img.size)
    im.close()

output_img = output_img.transpose(method=Image.FLIP_TOP_BOTTOM)
output_img.save('output_image.png')
