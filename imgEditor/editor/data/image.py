import os
import sys
import wx

_imgFileName = 'default.jpg'
_imgDir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'img')
_imgFullPath = os.path.join(_imgDir, _imgFileName)

_w = 400
_h = 300

def setFile(path):
    global _imgFullPath
    global _imgFileName
    global _imgDir
    _imgFullPath = path
    _imgDir, _imgFileName = os.path.split(path)


def getImgDir():
    return _imgDir

def getImgFileName():
    return _imgFileName

def getImgFullPath():
    return _imgFullPath


def getBitmap():
    bitmap = wx.BitmapFromImage(_image)
    return bitmap


def getPixels():
    pixelData = _image.GetData()  # string of characters in RGBRGBRGB... format
                                  # in the top-to-bottom, left-to-right order
    pixelData = map(lambda ch: ord(ch), pixelData)  # convert to array of integers
    return zip(*[iter(pixelData)]*3)  # split the array into [(R,G,B), (R,G,B),...]

def setPixels(pixels):
    flattened = [value for pixel in pixels for value in pixel]  # we get an array of integers [(R,G,B), (R,G,B),...];
                                                                # flatten it into [R,G,B,R,G,B,R,G,B,...] int array
    pixelData = map(lambda ii: chr(ii), flattened)  # convert integers into ascii
    pixelData = ''.join(pixelData)  # convert char array into a string
    _image.SetData(pixelData)


def setSize(size):
    global _w,_h
    _w,_h = size

def saveImage():
    _image.SaveFile(_imgFullPath, wx.BITMAP_TYPE_PNG)


def loadImage():
    '''load image from the file specified by _imgFullPath'''

    global _image

    _image = wx.ImageFromStream(open(_imgFullPath, "rb"))

    w,h = _image.GetWidth(), _image.GetHeight()
    scale = min(_w/w, _h/h)
    _image = _image.Scale(w*scale, h*scale, wx.IMAGE_QUALITY_HIGH)




