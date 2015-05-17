import os
import wx

from editor.constants import BASEDIR

class ImageData:

    def __init__(self, size=(400,300), imgFileName='default.jpg', imgDir=''):

        self.imgFileName = imgFileName
        self.imgDir = imgDir
        if self.imgDir == '':
            self.imgDir = os.path.join(BASEDIR,'img')
        self.imgFullPath = os.path.join(self.imgDir, self.imgFileName)

        self.w, self.h = size

        self.loadImage()


    def getImgDir(self):
        return self.imgDir

    def getImgFileName(self):
        return self.imgFileName

    def getImgFullPath(self):
        return self.imgFullPath

    def getBitmap(self):
        return wx.BitmapFromImage(self.image)


    def getPixels(self):

        pixelData = self.image.GetData()  # string of characters in RGBRGBRGB... format
                                          # in the top-to-bottom, left-to-right order
        pixelData = map(lambda ch: ord(ch), pixelData)  # convert to array of integers
        return zip(*[iter(pixelData)]*3)  # split the array into [(R,G,B), (R,G,B),...]


    def setPixels(self, pixels):

        flattened = [value for pixel in pixels for value in pixel]  # we get an array of integers [(R,G,B), (R,G,B),...];
                                                                    # flatten it into [R,G,B,R,G,B,R,G,B,...] int array
        pixelData = map(lambda ii: chr(ii), flattened)  # convert integers into ascii
        pixelData = ''.join(pixelData)  # convert char array into a string
        self.image.SetData(pixelData)


    def saveImage(self, fullPath):

        self.setPath(fullPath)
        self.image.SaveFile(self.imgFullPath, wx.BITMAP_TYPE_PNG)


    def loadImage(self, fullPath=''):

        if fullPath!='':
            self.setPath(fullPath)

        self.image = wx.ImageFromStream(open(self.imgFullPath, "rb"))

        w,h = self.image.GetWidth(), self.image.GetHeight()
        scale = min(self.w/w, self.h/h)
        self.image = self.image.Scale(w*scale, h*scale, wx.IMAGE_QUALITY_HIGH)


    def setPath(self, fullPath):

        self.imgFullPath = fullPath
        self.imgDir, self.imgFileName = os.path.split(fullPath)


