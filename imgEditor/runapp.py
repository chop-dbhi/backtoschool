#!/usr/bin/env python

import os
import logging
import sys

import wx

import editor.ui.frame as frame
from editor.constants import APP_NAME, IS_LINUX


class App(wx.App):

    def __init__(self, title, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        self.title = title
        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)

    def OnInit(self):
        self.frame = frame.Frame(None, title=self.title)
        self.frame.Show()
        return True


    def MacReopenApp(self):
        '''
        when the dock icon is clicked:
        - if the app is minimized, raise it;
        - if the app is in a different desktop, switch to that desktop.
        '''
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        self.frame.Raise()


def main():
    sys.settrace

    # set current working directory to ./img
    #os.chdir(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'img'))

    '''
    Make sure Unity doesn't grab the application menu bar
    -- otherwise the application will have trouble calculating its own window size, and it also
    won't have the permission to kill the menu on exit.
    '''
    if IS_LINUX:
        os.putenv("UBUNTU_MENUPROXY","0")

    app = App(title=APP_NAME)
    app.MainLoop()

if __name__ == '__main__':
    try:
        main()
    except Exception, ex:
        logging.debug("main: " + `ex`)




