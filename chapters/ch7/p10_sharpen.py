import images

img = images.Image('bonesBox.gif')


def detectEdges(image, thresh, degree):
    def average(triple):
        (r, g, b) = triple
        return (r + g + b) // 3

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new = image.clone()
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)

            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - leftLum) > thresh or abs(oldLum - bottomLum) > thresh:
                r, g, b = new.getPixel(x, y)
                r, g, b = darken(r, g, b, degree)
                new.setPixel(x, y, (r, g, b))
    return new


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

bclr = int(input('how dark do you want the edges: '))
ratio = int(input('what is the  threshold: '))
nimg = detectEdges(img, ratio, bclr)

nimg.draw()
