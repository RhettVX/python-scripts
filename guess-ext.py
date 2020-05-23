import sys
import os
import shutil
from pathlib import Path


def main(path: Path):
    data = path.read_bytes()

    # WARNING: PROTECTIVE GOGGLES REQUIRED BEYOND THIS POINT
    if not path.stat().st_size > 0:
        return
    try:
        path = str(path)
        if data[:3] == b'DDS':
            print("Found DDS")
            os.rename(path, path + '.dds')
        elif data[:12] == b'*TEXTUREPART':
            print("Found ECO")
            os.rename(path, path + '.eco')
        elif data[:4] == b'DMAT':
            print("Found DMA")
            os.rename(path, path + '.dma')
        # elif data[:5] == b'\x00\x00\x03\x01\x07':
        #     print("Found XRSB")
        #     os.rename(path, path + '.xrsb')
        # elif data[:5] == b'\x00\x00\x03\x01\x71':
        #     print("Found PRSB")
        #     os.rename(path, path + '.prsb')
        elif data[:4] == b'FSB5':
            print("Found FSB")
            os.rename(path, path + '.fsb')
        elif data[:4] == b'\x00\x00\x02\x00':
            print("Found TGA")
            os.rename(path, path + '.tga')
        elif data[:4] == b'ZONE':
            print("Found ZONE")
            os.rename(path, path + '.zone')
        elif data[:5] == b'<?xml':
            print("Found XML")
            os.rename(path, path + '.xml')
        elif data[:4] == b'DMOD':
            print("Found DME")
            os.rename(path, path + '.dme')
        elif data[1:4] == b'PNG':
            print("Found PNG")
            os.rename(path, path + '.png')
        elif data[:2] == b'\xFF\xD8':
            print("Found JPG")
            os.rename(path, path + '.jpg')
        elif data[:2] == b'BM':
            print("Found BMP")
            os.rename(path, path + '.bmp')
        elif data[0] == b'#':
            print("Found Text Map")
            os.rename(path, path + '.txt')
        elif data[:14] == b'<ActorRuntime>':
            print("Found ADR")
            os.rename(path, path + '.adr')
        elif data[:10] == b'<ActorSet>':
            print('Found AGR')
            os.rename(path, path + '.agr')
        elif data[:4] == b'CNK0':
            print("Found CNK0")
            os.rename(path, path + '.cnk0')
        elif data[:4] == b'CNK1':
            print("Found CNK1")
            os.rename(path, path + '.cnk1')
        elif data[:4] == b'CNK2':
            print("Found CNK2")
            os.rename(path, path + '.cnk2')
        elif data[:4] == b'CNK3':
            print("Found CNK3")
            os.rename(path, path + '.cnk3')
        elif data[:4] == b'CNK4':
            print("Found CNK4")
            os.rename(path, path + '.cnk4')
        elif data[:4] == b'CNK5':
            print("Found CNK5")
            os.rename(path, path + '.cnk5')
        elif data[:4] == b'CNK6':
            print("Found CNK6")
            os.rename(path, path + '.cnk6')
        elif data[:4] == b'CDTA':
            print("Found CDT")
            os.rename(path, path + '.cdt')
        elif data[:3] == b'CFX':
            print("Found CFX")  # ?
            os.rename(path, path + '.gfx')
        elif data[:4] == b'VNFO':
            print("Found VNFO")
            os.rename(path, path + '.vnfo')
    except FileExistsError:
        print('File Error')
        return


if __name__ == '__main__':

    for arg in sys.argv[1:]:
        # arg = r''
        path = Path(arg)
        if not path.is_dir():
            print('Not dir')
            continue

        for root, _, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.bin':
                    main(Path(root) / file)

    print("Done")
    input("Press enter")
