import sys
import os


def main():
    for root, dirs, files in os.walk(r''):
        for file in files:
            if file.endswith(''):
                with open(root+'\\'+file, 'w') as file:
                    file.write("")


if __name__ == '__main__':
    main()
