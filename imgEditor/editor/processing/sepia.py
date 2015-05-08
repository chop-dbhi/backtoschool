import editor.data.image as imageData


def convert():

    pixels = imageData.getPixels()
    sepiaPixels = []

    # outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
    # outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
    # outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)

    # The resulting values need to be capped at 255

    for (inputRed, inputGreen , inputBlue) in pixels:

        outputRed = min(255, int((inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)))
        outputGreen = min(255, int((inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)))
        outputBlue = min(255, int((inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)))

        sepiaPixels.append((outputRed,outputGreen,outputBlue))

    imageData.setPixels(sepiaPixels)
