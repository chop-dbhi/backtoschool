import logging
import os
import subprocess
import weakref
import wx.lib.scrolledpanel as scrolled
import wx

from editor.constants import *
import editor.data.image as imageData
import editor.processing.bw as bw
import editor.processing.sepia as sepia


class Panel(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        if IS_WIN:
            self.SetDoubleBuffered(True)

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sb = wx.StaticBox(self, label='')
        imgSizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        imageData.loadImage()
        bmp = wx.StaticBitmap(self, wx.ID_ANY, imageData.getBitmap())
        self.bmp = weakref.ref(bmp)

        imgSizer.Add((0,0), proportion=1)  # spacer
        imgSizer.Add(bmp, flag=wx.ALIGN_CENTER)
        imgSizer.Add((0,0), proportion=1)

        sizer.Add(imgSizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)

        sb = wx.StaticBox(self, label='')
        buttonSizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        buttonGridSizer = wx.GridBagSizer(10,5)

        self.addButtons(buttonGridSizer, 'Black && White\n', self.doBW, self.doBwImplement, self.doBwReload, 0)
        self.addButtons(buttonGridSizer, 'Sepia\n', self.doSepia, self.doSepiaImplement, self.doSepiaReload, 1)

        buttonSizer.Add(buttonGridSizer)
        buttonSizer.Add((0,0), proportion=1)  # spacer to fill any remaining space
        sizer.Add(buttonSizer, proportion=0, flag=wx.TOP|wx.BOTTOM|wx.RIGHT|wx.EXPAND, border=10)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        sizer.Fit(self)

        self.SetupScrolling()


    def addButtons (self, gridSizer, title, callback, callbackOpen, callbackReload, rowNum):

        button = wx.Button(self, label=title)
        self.Bind(wx.EVT_BUTTON, callback, button)
        gridSizer.Add(button, pos=(rowNum,0), flag=wx.ALIGN_RIGHT)

        button = wx.Button(self, label="Open\ncode")
        self.Bind(wx.EVT_BUTTON, callbackOpen, button)
        gridSizer.Add(button, pos=(rowNum,1), flag=wx.ALIGN_RIGHT)

        button = wx.Button(self, label="Reload\ncode")
        self.Bind(wx.EVT_BUTTON, callbackReload, button)
        gridSizer.Add(button, pos=(rowNum,2), flag=wx.ALIGN_RIGHT)


    def displayImage(self):
        try:
            self.bmp().SetBitmap(imageData.getBitmap())
            self.Layout()
        except Exception, ex:
            logging.debug("panel.displayImage: " + `ex`)


    def doBW(self, event):
        bw.convert()
        self.displayImage()

    def doSepia(self, event):
        sepia.convert()
        self.displayImage()


    def doBwImplement(self, event):
        openFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../processing/bw.py'))

    def doSepiaImplement(self, event):
        openFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../processing/sepia.py'))


    def doBwReload(self, event):
        reload(bw)

    def doSepiaReload(self, event):
        reload(sepia)


def openFile(path):

    if IS_WIN:
        os.startfile(path)
        return

    if IS_MAC:
        os.system("open %s" % path)
        return

    devnull = open(os.devnull, 'w') # /dev/null for redirecting IO
    subprocess.Popen(['xdg-open', path], stderr=subprocess.PIPE, stdin=devnull, stdout=devnull)



