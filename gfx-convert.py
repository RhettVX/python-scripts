from pathlib import Path
from sys import argv


if __name__ == '__main__':
    # for x in Path('.').glob('*.gfx'):
    #     x.rename(x.stem+'.swf')
    
    for x in Path(argv[1]).glob('*.gfx'):
        print(x)
        data = bytearray(x.read_bytes())

        if data[:3] == b'CFX':
            print('CFX')
            data[:3] = b'CWS'

        elif data[:3] == b'GFX':
            print('GFX')
            data[:3] = b'FWS'
            
        (x.parent / f'{x.stem}.swf').write_bytes(data)

        
