import os
import sys

from PIL import Image


def replace_improved(s):
    formats = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']
    for f in formats:
        s = s.replace(f, '')
    return s

def main(p=15, s=None):
    percent = int(p) / 100
    if s is not None:
        source = s
    else:
        source = 'source'
    store = 'store'
    os.makedirs(source, exist_ok=True)
    os.makedirs(store, exist_ok=True)
    directory = os.listdir(source)
    for i in directory:
        if i.endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif')):
            print('Resizing file', str(i))
            directory = source + '\\' + i
            img = Image.open(directory)
            new_img = img.resize((int(img.size[0] * percent), int(img.size[1] * percent)))
            name = replace_improved(i)
            new_img.save(
                store + '\\' + name + '_resized_to_(' + str(int(img.size[0] * percent)) + ', ' +
                str(int(img.size[1] * percent)) + ').png', 'png')
    print('All work done... press any key to exit.')
    input()


if __name__ == '__main__':
    default = 15
    source = 'source'

    print('Source folder for images?\n For default value (/source) just press Enter:')
    p_source = input()
    if p_source == '':
        p_source = source
    print('Percent value for images reduction?\n For default value (15%) just press Enter:')
    p_percent = input()
    if p_percent == '':
        p_percent = default

    if len(sys.argv) == 2:
        main(default, sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[2], sys.argv[1])
    else:
        main(p_percent, p_source)
