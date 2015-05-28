import weakref
import wx

from editor.constants import *
import editor.ui.panel_hello_world as panel_hello_world
import editor.ui.panel_image as panel_image
import editor.ui.panel_xray as panel_xray


class Frame(wx.Frame):

    def __init__(self, parent, title='Editor'):

        wx.Frame.__init__(self, parent, title=title)

        if IS_WIN: self.SetDoubleBuffered(True)

        self.addMenu()
        self.addHotKeys()

        w,h = wx.DisplaySize()
        self.SetSize((0.9*w,0.9*h))

        self.addNotebook()

        self.Show()


    def addNotebook(self):

        notebook = wx.Notebook(self, style=wx.BK_TOP)
        self.notebook = weakref.ref(notebook)

        panel = panel_hello_world.Panel(notebook)
        notebook.AddPage(panel, 'Hello, world!')

        panel = panel_image.Panel(notebook)
        notebook.AddPage(panel, 'Image editing')

        panel = panel_xray.Panel(notebook)
        notebook.AddPage(panel, 'X-ray editing')

        self.helloPageID = 0
        self.imagePageID = 1
        self.xrayPageID = 2

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onPageChanged, notebook)
        # Note: this
        # notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onPageChanged)
        # doesn't work correctly because one of the pages in the notebook itself has a notebook,
        # and with the notebook.Bind setup the event intended to inner notebook actually goes to both.
        # For an explanation of the differences please read:
        # http://wiki.wxpython.org/self.Bind_vs._self.button.Bind

        self.notebook().GetPage(0).grabOutput()


    def onPageChanged(self, event):

        selection = event.GetSelection()
        self.notebook().GetPage(selection).grabOutput()

        event.Skip() # make sure to propagate the event to upstream handlers


    def addMenu(self):

        # The menu bar needs to be created before any content is added to the pages,
        # otherwise there are sizing issues on windows.

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        # on Mac OS both Exit and About menus will end up in the application menu
        # instead of where we've put them.

        menuExit = fileMenu.Append(wx.ID_EXIT,'E&xit\tCtrl+X', 'Quit ' + APP_NAME)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)

        # on Mac File menu would end up empty, so don't add it.
        if not IS_MAC:
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
