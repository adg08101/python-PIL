from PIL import Image
import os
import sys


def main(p, s=None):
    percent = p / 100
    if s is not None:
        source = s
        print(s)
    else:
        source = 'source'
    store = 'store'
    os.makedirs(source, exist_ok=True)
    os.makedirs(store, exist_ok=True)
    dir = os.listdir(source)
    for i in dir:
        print('Resizing file ' + str(i))
        if i.endswith('.jpg') or i.endswith('.JPG'):
            dir = source + '\\' + i
            img = Image.open(dir)
            new_img = img.resize((int(img.size[0] * percent), int(img.size[1] * percent)))
            new_img.save(
                store + '\\' + i.replace('.jpg', '') + '_resized_to_(' + str(int(img.size[0] * percent)) + ', ' +
                str(int(img.size[1] * percent)) + ').png', 'png')
    print('All work done... press any key to exit.')
    input()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(15, sys.argv[1])
    else:
        main(15)
