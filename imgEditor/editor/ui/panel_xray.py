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
import editor.ui.panel_image as panel_image
import editor.processing.xray as xray


class Panel(panel_image.Panel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        if IS_WIN:
            self.SetDoubleBuffered(True)

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        codePanel = panel_code.Panel(self, 'xray.py')
        self.codePanel = weakref.ref(codePanel)
        sizer.Add(codePanel, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)

        imgSizer = wx.BoxSizer(wx.VERTICAL)

        toolbar = self.makeToolbar()
        imgSizer.Add(toolbar, flag=wx.EXPAND, proportion=0)

        w,h = wx.DisplaySize()
        self.imageData = image.ImageData(size=(0.3*w,0.6*h), imgFileName='oblique.png',
                                         imgDir = os.path.join(os.path.join(BASEDIR,'img'),'xrays'))

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


    def makeToolbar(self):

        sizerV = wx.BoxSizer(wx.VERTICAL)

        sizer = super(Panel,self).makeToolbar(applyLabel="Process X-ray")

        sizerV.Add(sizer, flag=wx.EXPAND)

        applyBmp = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR, (25,25))


        button = GB.GradientButton(self, -1, applyBmp, label="Publish to Website")
        self.Bind(wx.EVT_BUTTON, self.onPublish, button)
        sizerV.Add(button, flag=wx.ALL, border=3)

        return sizerV


    def onApply(self, event):
        self.codePanel().saveCode()
        self.codePanel().clearOutput()
        self.applyFilter(xray)


    def onPublish(self, event):
        self.imageData.saveImage(os.path.join(PUBLISH_DIR, self.imageData.getImgFileName()))


    def grabOutput(self):
        self.codePanel().grabOutput()


