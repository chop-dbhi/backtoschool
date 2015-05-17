def applyFilter(pixels):
    '''
    Formula:
    outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
    outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
    outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)

    The resulting values need to be capped at 255
    '''

    sepiaPixels = []

    for pixel in pixels:

        (inputRed, inputGreen, inputBlue)  = pixel

        outputRed = min(255, int((inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)))
        outputGreen = min(255, int((inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)))
        outputBlue = min(255, int((inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)))

        newPixel = (outputRed,outputGreen,outputBlue)
        sepiaPixels.append(newPixel)

    return sepiaPixels