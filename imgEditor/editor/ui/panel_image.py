import weakref
import wx.lib.scrolledpanel as scrolled
import wx

from editor.constants import *
import editor.processing.bw as bw
import editor.processing.custom as custom
import editor.data.image as image
import editor.ui.code_editor as panel_code
import editor.processing.sepia as sepia


class Panel(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        if IS_WIN:
            self.SetDoubleBuffered(True)

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        codeNotebook = self.makeCodeNotebook()
        self.codeNotebook = weakref.ref(codeNotebook)
        sizer.Add(codeNotebook, proportion=1, flag=wx.EXPAND)

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

        button = wx.Button(self, label="Open")
        button.SetBitmap(openBmp, wx.LEFT)
        self.Bind(wx.EVT_BUTTON, self.onOpen, button)
        sizer.Add(button)

        button = wx.Button(self, label="Save")
        button.SetBitmap(saveBmp, wx.LEFT)
        self.Bind(wx.EVT_BUTTON, self.onSave, button)
        sizer.Add(button)

        sizer.Add((0,0), proportion=1)  # spacer

        button = wx.Button(self, label=applyLabel)
        button.SetBitmap(applyBmp, wx.LEFT)
        self.Bind(wx.EVT_BUTTON, self.onApply, button)
        sizer.Add(button)

        button = wx.Button(self, label="Reset")
        button.SetBitmap(resetBmp, wx.LEFT)
        self.Bind(wx.EVT_BUTTON, self.onReset, button)
        sizer.Add(button)

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

        dlg = wx.FileDialog(self,
                            message = 'Choose image file to open',
                            defaultDir = self.imageData.getImgDir(),  # tried using os.getcwd() (current working directory)
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

        dlg = wx.FileDialog(
            self,
            message = 'Save image to file',
            defaultDir = self.imageData.getImgDir(),
            defaultFile = '',
            wildcard = 'Image files (*.png)|*.png',
            style = wx.SAVE | wx.OVERWRITE_PROMPT)

        if dlg.ShowModal() == wx.ID_OK:
            self.imageData.saveImage(dlg.GetPath())


    def onApply(self, event):
        page = self.codeNotebook().CurrentPage
        page.saveCode()
        page.clearOutput()
        filter = (bw, sepia, custom)[self.currentFilter]
        self.applyFilter(filter)


    def onReset(self, event):
        self.imageData.loadImage()
        self.displayImage()


    def grabOutput(self):
        self.codeNotebook().CurrentPage.grabOutput()


