def applyFilter(pixels):

    '''The simplest method of converting to B&W is to simply average the values: R = G = B = (R + G + B) / 3'''

    bwPixels = []

    for pixel in pixels:

        (inputRed, inputGreen, inputBlue)  = pixel

        outputRed = outputGreen = outputBlue = (inputRed + inputGreen + inputBlue) / 3

        #outputRed = min(outputRed+50, 255)  # uncomment to increase the red levels and make the image
                                                                        # red-and-white instead of b&w. The new value needs to be capped at 255.
        #outputGreen = min(outputGreen*2, 255)  # green-and-white
        #outputBlue = min(outputBlue*2, 255)  # blue-and-white

        newPixel = (outputRed, outputGreen, outputBlue)
        bwPixels.append(newPixel)

    return bwPixels