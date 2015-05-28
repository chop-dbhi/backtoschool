import os
import platform
import sys

APP_NAME = 'Biomedical Image Processing Tutorial'

# Is this execution from a PyInstaller bundle?
IS_FROZEN = getattr(sys, 'frozen', False)

if IS_FROZEN:
    # PyInstaller creates a temporary directory for all the files it needs.
    BASEDIR = sys._MEIPASS
    PROCESSING_DIR = BASEDIR
    # 'Publish' will be replaced by saving to desktop
    PUBLISH_DIR = os.path.join(os.path.expanduser('~'), 'Desktop')
else:
    BASEDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
    PROCESSING_DIR = os.path.join(os.path.join(BASEDIR, 'editor'), 'processing')
    PUBLISH_DIR = PUBLISH_DIR = os.path.join(os.path.join(BASEDIR, '..'),'img')

osName = platform.system().lower()
IS_MAC = (osName == 'darwin')
IS_WIN = (osName == 'windows')
IS_LINUX = (not IS_MAC) and (not IS_WIN)

