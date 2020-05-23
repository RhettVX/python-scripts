from pathlib import Path
from argparse import ArgumentParser
from os import makedirs, walk
from re import fullmatch, IGNORECASE
from shutil import copy


type_regex = [
    ('models', r'.*\.dme$'),
    ('textures', r'^(?!img).*(?<!LOD\d)\.(dds|tga)$'),
    ('materials', r'.*\.dma$'),
    ('zones', r'.*(\.(zone|cnk\d?|tome|vnfo|ctg_pc|cel)|areas\.xml)$'),
    ('maps', r'.*_Tile.*(LOD\d|\d_\d)*.*\.(dds|txt)$'),
	('actordefs', r'.*\.adr$'),
	('data', r'.*\.(xml|txt)'),
	('nameless', r'.*\.bin$'),
	('images', r'.*\.(png|jpe?g|bmp)$'),
	('ui', r'img.*\.dds$'),
    ('scripts', r'.*(\.lua|scripts.txt)$'),
    ('audio', r'.*\.(fsb|ogg)$'),
    ('gfx', r'.*\.gfx$'),
    ('everything', '.*')
]


def main(path: Path):
    for i, pair in enumerate(type_regex):
        print(f'[{i}]: {pair[0]}')

    chosen_type = type_regex[int(input('Enter a number >'))]
    output_path = Path(f'copied-{chosen_type[0]}')

    makedirs(output_path, exist_ok=True)
    for root, _, files in walk(path):
        for file in files:
            if fullmatch(chosen_type[1], file, IGNORECASE):
                print(f'Found "{file}"')
                copy(Path(root, file), output_path)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('src', help='directory containing unpacked files')
    args = parser.parse_args()

    while True:
        try:
            main(Path(args.src))
        except ValueError:
            break
