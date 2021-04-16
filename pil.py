from PIL import Image
import os

def main(p):
    percent = p / 100
    source = 'source'
    store = 'store'
    os.makedirs(source, exist_ok=True)
    os.makedirs(store, exist_ok=True)
    dir = os.listdir(source)
    for i in dir:
        print('Resizing file ' + str(i))
        if i.endswith('.jpg'):
            dir = source + '\\' + i
            img = Image.open(dir)
            new_img = img.resize((int(img.size[0] * percent), int(img.size[1] * percent)))
            new_img.save(store + '\\' + i.replace('.jpg', '') + '_resized_to_(' + str(int(img.size[0] * percent)) + ', ' +
                         str(int(img.size[1] * percent)) + ').png', 'png')
    print('All work done... press any key to exit.')
    input()

if __name__ == '__main__':
    main(15)
