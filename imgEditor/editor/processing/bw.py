def applyFilter(pixels):

    # This is an array where we'll store pixels for the new image. In the beginning, it's empty.
    newPixels = []

    # Let's go through the entire image, one pixel at a time
    for pixel in pixels:

        # Let's get the Red, Green and Blue values for the current pixel
        inputRed  = pixel[0]
        inputGreen = pixel[1]
        inputBlue = pixel[2]

       # in a Black&White image, each pixel has the same value for Red, Green, and Blue.
       # But what is that value?  
       # Red = Green = Blue = ?
       # The easiest method of calculating the new value is to average the old values: 
       # newRed = newGreen = newBlue = (oldRed + oldGreen + oldBlue) / 3

	average = (inputRed + inputGreen + inputBlue) / 3

        outputRed = average
        outputGreen = average
        outputBlue = average

        # Now that we know the color values for the new pixel, let's create this pixel. 
        newPixel = [0,0,0]

        # Let's set the Red, Green, and Blue values for this new pixel
        newPixel[0] = outputRed 
        newPixel[1] = outputGreen
        newPixel[2] = outputBlue

        # Optional exercise: 
        # Now that you know how to convert an image to B&W, try something new!
        # Try changing the output values. For example, If you increase the outputRed value, 
        # you can make the image red-and-white instead of black-and-white!
        # But remember that each color value cannot be bigger than 255.
        # To make sure that a number is not bigger than 255, you can use the min function, for example:
        # newNumber = min(number, 255)

	# add the new pixel to the resulting image
        newPixels.append(newPixel)

    return newPixels