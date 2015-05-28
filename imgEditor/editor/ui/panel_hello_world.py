try:
    from agw import gradientbutton as GB
except ImportError:
    import wx.lib.agw.gradientbutton as GB

import weakref
import wx.lib.scrolledpanel as scrolled
import wx

from editor.constants import IS_FROZEN
import editor.ui.code_editor as code_editor

if IS_FROZEN:
    import hello
else:
    import editor.processing.hello as hello


class Panel(scrolled.ScrolledPanel):

    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        sizer = wx.BoxSizer(wx.VERTICAL)

        button = GB.GradientButton(self, -1, wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR, (25,25)), "Run code")
        self.Bind(wx.EVT_BUTTON, self.onApply, button)
        sizer.Add(button, flag=wx.ALL, border=5)

        codeEditor = code_editor.Panel(self, 'hello.py')
        self.codePanel = weakref.ref(codeEditor)
        sizer.Add(codeEditor, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        sizer.Fit(self)

        self.SetupScrolling()


    def onApply(self, event):
        self.codePanel().saveCode()
        self.codePanel().clearOutput()
        reload(hello)


    def grabOutput(self):
        self.codePanel().grabOutput()





