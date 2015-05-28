try:
    from agw import gradientbutton as GB
except ImportError:
    import wx.lib.agw.gradientbutton as GB

import weakref
import wx.lib.scrolledpanel as scrolled
import wx

from editor.constants import *
import editor.data.image as image
import editor.ui.code_editor as panel_code

if IS_FROZEN:
    import bw
    import custom
    import sepia
else:
    import editor.processing.bw as bw
    import editor.processing.custom as custom
    import editor.processing.sepia as sepia


class Panel(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        if IS_WIN:
            self.SetDoubleBuffered(True)

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        codeNotebook = self.makeCodeNotebook()
        self.codeNotebook = weakref.ref(codeNotebook)
        sizer.Add(codeNotebook, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)

        imgSizer = wx.BoxSizer(wx.VERTICAL)

        toolbar = self.makeToolbar()
        imgSizer.Add(toolbar, flag=wx.EXPAND, proportion=0)

        w,h = wx.DisplaySize()
        self.imageData = image.ImageData(size=(0.3*w,0.6*h))

        bmp = wx.StaticBitmap(self, wx.ID_ANY, self.imageData.getBitmap())
        self.bmp = weakref.ref(bmp)

        imgSizer.Add((0,30), proportion=0)  # spacer
        imgSizer.Add(bmp, flag=wx.ALIGN_CENTER)
        imgSizer.Add((0,0), proportion=1)

        sizer.Add(imgSizer, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        sizer.Fit(self)

        self.SetupScrolling()


    def makeCodeNotebook(self):

        codeNotebook = wx.Notebook(self, id=wx.ID_ANY, style=wx.BK_TOP)

        codePanel = panel_code.Panel(codeNotebook, 'bw.py')
        codeNotebook.AddPage(codePanel, 'B&&W')

        codePanel = panel_code.Panel(codeNotebook, 'sepia.py')
        codeNotebook.AddPage(codePanel, 'Sepia')

        codePanel = panel_code.Panel(codeNotebook, 'custom.py')
        codeNotebook.AddPage(codePanel, 'Custom Filter')

        self.currentFilter = 0
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onFilterChanged, codeNotebook)

        # Note: this
        # codeNotebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onFilterChanged)
        # doesn't work correctly because the event intended to this inner notebook actually also goes to
        # the outer notebook on the main frame
        # For an explanation of the differences please read:
        # http://wiki.wxpython.org/self.Bind_vs._self.button.Bind

        return codeNotebook


    def makeToolbar(self, applyLabel="Apply Filter"):

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        tsize = (25,25)

        openBmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        saveBmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, tsize)
        applyBmp = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR, tsize)
        resetBmp = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, tsize)

        # This works on mac but not on raspberry pi
        # because wx.Button with bitmap+text aren't available in wx.Python 2.8 (this was introduced in 2.9)
        # => using gradient buttons instead. 
        # button = wx.Button(self, label="Open")
        # button.SetBitmap(openBmp, wx.LEFT)

        button = GB.GradientButton(self, -1, openBmp, label="Open")
        self.Bind(wx.EVT_BUTTON, self.onOpen, button)
        sizer.Add(button, flag=wx.ALL, border=3)

        button = GB.GradientButton(self, -1, saveBmp, label="Save")
        self.Bind(wx.EVT_BUTTON, self.onSave, button)
        sizer.Add(button, flag=wx.ALL, border=3)

        sizer.Add((0,0), proportion=1)  # spacer

        button = GB.GradientButton(self, -1, applyBmp, label=applyLabel)
        self.Bind(wx.EVT_BUTTON, self.onApply, button)
        sizer.Add(button, flag=wx.ALL, border=3)

        button = GB.GradientButton(self, -1, resetBmp, label="Reset")
        self.Bind(wx.EVT_BUTTON, self.onReset, button)
        sizer.Add(button, flag=wx.ALL, border=3)

        return sizer


    def displayImage(self):
        self.bmp().SetBitmap(self.imageData.getBitmap())
        self.Layout()


    def applyFilter(self, filter):

        reload(filter)
        pixels = filter.applyFilter(self.imageData.getPixels())
        self.imageData.setPixels(pixels)
        self.displayImage()


    def onFilterChanged(self, event):

        self.currentFilter = event.GetSelection()
        self.codeNotebook().GetPage(self.currentFilter).grabOutput()

        event.Skip() # make sure to propagate the event to upstream handlers


    def onOpen(self, event):

        if IS_FROZEN:
            dir = PUBLISH_DIR
        else: dir = self.imageData.getImgDir()

        dlg = wx.FileDialog(self,
                            message = 'Choose image file to open',
                            defaultDir = dir,  # tried using os.getcwd() (current working directory)
                                               # but that didn't work correctly on mac
                            defaultFile = '',
                            wildcard = 'Image files (*.jpeg,*.jpg,*.png)|*.jpeg;*.jpg;*.png',
                            style = wx.OPEN  # tried adding "|wx.CHANGE_DIR" to allow the dialog to change current working directory.
                                             # but that didn't work correctly on mac
        )

        if dlg.ShowModal() == wx.ID_OK:
            self.imageData.loadImage(dlg.GetPath())
            self.displayImage()

        dlg.Destroy()


    def onSave(self, event):

        if IS_FROZEN:
            dir = PUBLISH_DIR
        else: dir = self.imageData.getImgDir()

        dlg = wx.FileDialog(
            self,
            message = 'Save image to file',
            defaultDir = dir,
            defaultFile = '',
            wildcard = 'Image files (*.png)|*.png',
            style = wx.SAVE | wx.OVERWRITE_PROMPT)

        if dlg.ShowModal() == wx.ID_OK:
            self.imageData.saveImage(dlg.GetPath())

        dlg.Destroy()


    def onApply(self, event):

        # on Raspberry pi image processing will take a while, so use a busy cursor
        wx.BeginBusyCursor()
        try:
            page = self.codeNotebook().CurrentPage
            page.saveCode()
            page.clearOutput()
            filter = (bw, sepia, custom)[self.currentFilter]
            self.applyFilter(filter)
        finally:
            wx.EndBusyCursor()


    def onReset(self, event):

        wx.BeginBusyCursor()
        try:
            self.imageData.loadImage()
            self.displayImage()
        finally:
            wx.EndBusyCursor()


    def grabOutput(self):
        self.codeNotebook().CurrentPage.grabOutput()


