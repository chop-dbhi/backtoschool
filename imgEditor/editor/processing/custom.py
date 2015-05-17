def applyFilter(pixels):

    newPixels = []

    for pixel in pixels:

        (inputRed, inputGreen, inputBlue)  = pixel

        outputRed = inputRed
        outputGreen = inputGreen
        outputBlue = 0

        newPixel = (outputRed, outputGreen, outputBlue)
        newPixels.append(newPixel)

    return newPixels