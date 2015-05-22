def applyFilter(pixels):
    '''
    Formula:

    outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
    outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
    outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)

    (source: http://www.techrepublic.com/blog/how-do-i/how-do-i-convert-images-to-grayscale-and-sepia-tone-using-c/)

    The resulting values need to be capped at 255
    '''

    sepiaPixels = []

    for pixel in pixels:

        (inputRed, inputGreen, inputBlue)  = pixel

        outputRed = min(255, int(inputRed*0.393 + inputGreen*0.769 + inputBlue*0.181))
        outputGreen = min(255, int(inputRed*0.349 + inputGreen*0.686 + inputBlue*0.168))
        outputBlue = min(255, int(inputRed*0.272 + inputGreen*0.534 + inputBlue*0.131))

        newPixel = (outputRed, outputGreen, outputBlue)
        sepiaPixels.append(newPixel)

    return sepiaPixels