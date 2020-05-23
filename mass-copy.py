import os
import sys
import shutil
import re


dst_path = r''

search_term = r'^Amerish.*$'


def main():

    # path = sys.argv[1]
    path = r''

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    
    for root, dirs, files in os.walk(path):
        for file in files:
            matchObj = re.match(search_term, file, re.I)
            
            if matchObj:
                print(f'Copying {file}')
                shutil.copy(root+'\\'+file, dst_path)


if __name__ == '__main__':
    main()
