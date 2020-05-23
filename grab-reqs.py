from pathlib import Path
from os import walk
from shutil import copy


unpack_path = Path(r'')
output_dir = Path('./req-output')
reqs = []


if __name__ == '__main__':
    reqs = list(set(Path('reqs.txt').read_text().strip().split('\n')))
    output_dir.mkdir(parents=True, exist_ok=True)

    for root, _, files in walk(unpack_path):
        for file in files:
            for r in reqs:
                if file == r:
                    print(f'Found "{r}"')
                    copy(Path(root, file), output_dir)
                    reqs.remove(r)
