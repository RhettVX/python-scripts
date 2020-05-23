import sys
import os
import re
import shutil

test_args = [
    None,
    r'',
    r''
    ]

re_term = r'\[(~)\] (.*\.\w*):'
dst_dir = 'NewFiles'
new_files = []

def main():

    #if not os.path.exists(dst_dir):
    #    os.makedirs(dst_dir)
    
    with open(sys.argv[1], 'r') as in_file:
        for line in in_file:
            mo = re.search(re_term, line)
            if mo:
                #print(f'Found {mo.group(2)}')
                new_files.append(mo.group(2))

    with open('diff-files.txt', 'w') as out_file:
        for f in new_files:
            out_file.write(f+'\n')

    #for root, dirs, files in os.walk(test_args[2]):
    #    for file in files:
    #        if file in new_files:
    #            shutil.copy(root+'\\'+file, '.\\NewFiles\\')

if __name__ == '__main__':
    main()
