from PIL import Image
import os

def main(p):
    percent = p / 100
    source = 'source'
    store = 'store'
    os.mkdir(source)
    os.mkdir(store)
    dir = os.listdir(source)
    for i in dir:
        if i.endswith('.jpg'):
            dir = source + '\\' + i
            img = Image.open(dir)
            new_img = img.resize((int(img.size[0] * percent), int(img.size[1] * percent)))
            new_img.save(store + '\\' + i + '(' + str(int(img.size[0] * percent)) + ', ' +
                         str(int(img.size[1] * percent)) + ').png', 'png')

if __name__ == '__main__':
    main(15)
