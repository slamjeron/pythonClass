import images
import sys


def chBright(im, clr):
    h = im.getHeight()
    w = im.getWidth()
    for x in range(w):
        for y in range(h):
            r, g, b = im.getPixel(x, y)
            r, g, b = darken(r, g, b, clr)
            if r <= 255 and g <= 255 and b <= 255:
                im.setPixel(x, y, (r, g, b))

    im.draw()


def darken(r, g, b, chan):
    if chan > 0:
        if (r + chan < 255):
            r = r + chan
        else:
            r = 255
        if (g + chan < 255):
            g = g + chan
        else:
            g = 255
        if (b + chan < 254):
            b = b + chan
        else:
            b = 255
    else:
        if (r + chan > 0):
            r = r + chan
        else:
            r = 0
        if (g + chan > 0):
            g = g + chan
        else:
            g = 0
        if (b + chan > 0):
            b = b + chan
        else:
            b = 0
    return r, g, b


while True:
    while True:
        try:
            bright = int(input('input the brightness of the image using a number between -255 and 255: '))
        except ValueError:
            print('the value you entered is incorrect')
            continue
        else:
            break;

    img = images.Image('bonesBox.gif')
    chBright(img, bright)
    inp = input('would you like to try again type y if you do anything else will end the program: ')
    if (inp == 'y'):
        continue
    else:
        sys.exit()

