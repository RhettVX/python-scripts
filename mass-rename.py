import os


dir_path = r''
old_term = ''
new_term = ''


file_exts = ['.zone', '.vnfo', '.tome', '.cnk0',
             '.cnk1', '.cnk2', '.cnk2', '.cnk3',
             '.cnk4', '.cnk5', '.txt', '.xml'
             ]


def main():
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            
            if ext in file_exts:
                new_name = file.replace(old_term, new_term)
                os.rename(root+'\\'+file, root+'\\'+new_name)


if __name__ == '__main__':
    main()
