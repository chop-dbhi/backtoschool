import editor.data.image as imageData


def convert():

    pixels = imageData.getPixels()
    bwPixels = []

    # The average method simply averages the values: (R + G + B) / 3.
    for (r,g,b) in pixels:
        r = g = b = (r+g+b)/3
        bwPixels.append((r,g,b))

    imageData.setPixels(bwPixels)
