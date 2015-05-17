import os
import platform
import sys

APP_NAME = 'Biomedical Image Processing Tutorial'
BASEDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
PUBLISH_DIR = BASEDIR

osName = platform.system().lower()
IS_MAC = (osName == 'darwin')
IS_WIN = (osName == 'windows')
IS_LINUX = (not IS_MAC) and (not IS_WIN)

