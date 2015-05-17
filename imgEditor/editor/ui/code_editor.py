import wx.richtext
import weakref
import wx

from editor.constants import *


class Panel(wx.Panel):

    def __init__(self, parent, fileName):
        wx.Panel.__init__(self, parent, -1)

        self.fileName = os.path.join(os.path.join(os.path.join(BASEDIR,'editor'),'processing'),fileName)
        self.outFileName = os.path.join(BASEDIR,'out.txt')

        sizer = wx.BoxSizer(wx.VERTICAL)

        codeEditor = wx.richtext.RichTextCtrl(self, style=wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER)
        self.codeEditor = weakref.ref(codeEditor)
        codeEditor.LoadFile(self.fileName, type=wx.richtext.RICHTEXT_TYPE_TEXT)
        sizer.Add(codeEditor, proportion=2, flag=wx.EXPAND)
        sizer.Add((0,10), proportion=0)  # spacer

        stdOut = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.TE_READONLY)
        self.stdOut = weakref.ref(stdOut)
        sizer.Add(stdOut, proportion=1, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        sizer.Fit(self)


    def saveCode(self):
        self.codeEditor().SaveFile(self.fileName, type=wx.richtext.RICHTEXT_TYPE_TEXT)


    def runStandaloneCode(self):
        os.system("python %(code)s > %(out)s" % {"code": self.fileName, "out": self.outFileName})


    def reloadOutput(self):
        self.stdOut().LoadFile(self.outFileName)


    def clearOutput(self):
        self.stdOut().Clear()


    def grabOutput(self):
        sys.stdout = self.stdOut()
        sys.stderr = self.stdOut()
