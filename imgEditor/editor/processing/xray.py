def applyFilter(pixels):

    newPixels = []

    for pixel in pixels:

        (r,g,b)  = pixel

        if r>250 and g>250 and b>250:
            g=0
            b=0

        newPixel = (r,g,b)
        newPixels.append(newPixel)

    return newPixels