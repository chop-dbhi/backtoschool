import weakref
from wx.lib.wordwrap import wordwrap
import wx

from editor.constants import *
import editor.ui.panel as panel
import editor.data.image as imageInfo


class Frame(wx.Frame):  # top-level window.

    def __init__(self, parent, title='Editor'):

        wx.Frame.__init__(self, parent, title=title)

        if IS_WIN: self.SetDoubleBuffered(True)

        self.addMenu()
        self.addHotKeys()
        self.addToolbar()

        w,h = wx.DisplaySize()
        self.SetSize((0.7*w,0.7*h))
        imageInfo.setSize((0.5*w,0.5*h))

        mainPanel = panel.Panel(self)
        self.mainPanel = weakref.ref(mainPanel) # To avoid a double delete when the frame is destroyed,
                                                # only create a soft reference here,
                                                # because a hard reference will automatically get generated.

        self.Show()


    def addToolbar(self):

        tsize = (25,25)
        self.toolbar = self.CreateToolBar(wx.TB_FLAT|wx.TB_TEXT)

        openBmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        saveBmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, tsize)
        resetBmp = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, tsize)

        self.toolbar.SetToolBitmapSize(tsize)

        openIcon = self.toolbar.AddLabelTool(wx.ID_OPEN, "Open", openBmp, shortHelp="Open image file", longHelp="Open image file")
        self.Bind(wx.EVT_TOOL, self.onOpen, openIcon)

        saveIcon = self.toolbar.AddLabelTool(wx.ID_SAVE, "Save", saveBmp, shortHelp="Save image to file", longHelp="Save image to file")
        self.Bind(wx.EVT_TOOL, self.onSave, saveIcon)

        resetIcon = self.toolbar.AddLabelTool(wx.ID_RESET, "Reset", resetBmp, shortHelp="Reset image", longHelp="Reset image")
        self.Bind(wx.EVT_TOOL, self.onReset, resetIcon)

        self.toolbar.Realize()


    def addMenu(self):

        # The menu bar needs to be created before any content is added to the pages,
        # otherwise there are sizing issues on windows.

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        menuOpen = fileMenu.Append(wx.ID_OPEN, '&Open image', 'Open image file')
        self.Bind(wx.EVT_MENU, self.onOpen, menuOpen)

        menuSave = fileMenu.Append(wx.ID_SAVE, '&Save image', 'Save image to file')
        self.Bind(wx.EVT_MENU, self.onSave, menuSave)

        # on Mac OS both Exit and About menus will end up in the application menu
        # instead of where we've put them.

        menuExit = fileMenu.Append(wx.ID_EXIT,'E&xit\tCtrl+X', 'Quit ' + APP_NAME)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)

        menuAbout = fileMenu.Append(wx.ID_ABOUT, '&About', 'About ' + APP_NAME)
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)

        menuBar.Append(fileMenu, "File")
        self.SetMenuBar(menuBar)


    def addHotKeys(self):
        # exit on Ctrl+Q (or Cmd+Q on Mac OS)
        newId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onExit, id=newId)
        accelTbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('Q'), newId )])
        self.SetAcceleratorTable(accelTbl)


    def onExit(self, event):
        self.Close()


    def onOpen(self, event):

        dlg = wx.FileDialog(self,
            message = 'Choose image file to open',
            defaultDir = imageInfo.getImgDir(),  # tried using os.getcwd() (current working directory)
                                                 # but that didn't work correctly on mac
            defaultFile = '',
            wildcard = 'Image files (*.jpeg,*.jpg,*.png)|*.jpeg;*.jpg;*.png',
            style = wx.OPEN  # tried adding "|wx.CHANGE_DIR" to allow the dialog to change current working directory.
                             # but that didn't work correctly on mac
        )

        if dlg.ShowModal() == wx.ID_OK:
            imageInfo.setFile(dlg.GetPath())
            imageInfo.loadImage()
            self.mainPanel().displayImage()

        dlg.Destroy()


    def onSave(self, event):

        dlg = wx.FileDialog(
            self,
            message = 'Save image to file',
            defaultDir = imageInfo.getImgDir(),
            defaultFile = '',
            wildcard = 'Image files (*.png)|*.png',
            style = wx.SAVE | wx.OVERWRITE_PROMPT)

        if dlg.ShowModal() == wx.ID_OK:
            imageInfo.setFile(dlg.GetPath())
            imageInfo.saveImage()


    def onReset(self, event):
        imageInfo.loadImage()
        self.mainPanel().displayImage()


    def onAbout(self,event):

        info = wx.AboutDialogInfo()
        info.Name = APP_NAME
        info.Version = VERSION
        info.Copyright = COPYRIGHT
        info.Description = wordwrap(DESCRIPTION, 400, wx.ClientDC(self))
        info.WebSite = (COMPANY_URL, COMPANY_NAME)
        info.Developers = DEVELOPERS

        wx.AboutBox(info)


