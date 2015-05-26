def applyFilter(pixels):
    '''
    Formula for the Sepia filter:

    outputRed = inputRed * 0.393 + inputGreen * 0.769 + inputBlue * 0.189
    outputGreen = inputRed * 0.349 + inputGreen * 0.686 + inputBlue * 0.168
    outputBlue = inputRed * 0.272 + inputGreen * 0.534 + inputBlue * 0.131

    (source: http://www.techrepublic.com/blog/how-do-i/how-do-i-convert-images-to-grayscale-and-sepia-tone-using-c/)

    Note: The resulting color values need to be capped at 255
    '''

    # This is an array where we'll store pixels for the new image. In the beginning, it's empty.
    newPixels = []

    # Let's go through the entire image, one pixel at a time
    for pixel in pixels:

        # Let's get the Red, Green and Blue values for the current pixel
        inputRed  = pixel[0]
        inputGreen = pixel[1]
        inputBlue = pixel[2]

        # Let's calculate Red, Green, and Blue values for the new pixel
        outputRed = min(255, int(inputRed*0.393 + inputGreen*0.769 + inputBlue*0.181))
        outputGreen = min(255, int(inputRed*0.349 + inputGreen*0.686 + inputBlue*0.168))
        outputBlue = min(255, int(inputRed*0.272 + inputGreen*0.534 + inputBlue*0.131))

        # Now that we know the color values for the new pixel, let's create this pixel. 
        newPixel = [0,0,0]

        # Let's set the Red, Green, and Blue values for this new pixel
        newPixel[0] = outputRed 
        newPixel[1] = outputGreen
        newPixel[2] = outputBlue

        # add the new pixel to the resulting image
        newPixels.append(newPixel)

    return newPixels