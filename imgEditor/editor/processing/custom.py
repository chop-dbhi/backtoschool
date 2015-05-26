def applyFilter(pixels):

    # This is an array where we'll store pixels for the new image. In the beginning, it's empty.
    newPixels = []

    # Let's go through the entire image, one pixel at a time
    for pixel in pixels:

        # Let's get the Red, Green and Blue values for the current pixel
        inputRed  = pixel[0]
        inputGreen = pixel[1]
        inputBlue = pixel[2]

        # Let's calculate Red, Green, and Blue values for the new pixel.
        # For example, remove all the blue out of this picture:
        outputRed = inputRed
        outputGreen = inputGreen
        outputBlue = 0

        # Now that we know the color values for the new pixel, let's create this pixel. 
        newPixel = [0,0,0]

        # Let's set the Red, Green, and Blue values for this new pixel
        newPixel[0] = outputRed 
        newPixel[1] = outputGreen
        newPixel[2] = outputBlue

	# add the new pixel to the resulting image
        newPixels.append(newPixel)

    return newPixels