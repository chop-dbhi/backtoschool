def applyFilter(pixels):

    # This is an array where we'll store pixels for the new image. In the beginning, it's empty.
    newPixels = []

    # Let's go through the entire image one pixel at a time
    for pixel in pixels:
        
        # Let's get the Red, Green and Blue values for the current pixel
        inputRed  = pixel[0]
        inputGreen = pixel[1]
        inputBlue = pixel[2]

        # create a new pixel
        newPixel = [0,0,0]

        # Calculate new Red, Green and Blue values for this pixel.
        # Look at the code below: right now all we are doing is keeping the old values. 
        # How can we change these values to make the pin more visible? 
        # Remember, the pin was very dense, so the pixels corresponding to it 
        # will be very bright in the X-ray image. 
        # The maximum value for each color is 255, so the brightest possible pixel has 
        # Red = Green = Blue = 255.
        # A pixel that is almost as bright but a little dimmer will have Red = Green = Blue = 254;
        # an even dimmer one will have Red = Green = Blue = 253, and so on. 
        # Try to guess the color values for the brightest pixels in this X-Ray image, and you will find the pin!
        # When you find the brightest pixels, change their color to red, so that we can see the pin in the X-ray. 

        newPixel[0] = inputRed
        newPixel[1] = inputGreen
        newPixel[2] = inputBlue

        newPixels.append(newPixel)

    return newPixels