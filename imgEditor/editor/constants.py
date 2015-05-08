import platform

osName = platform.system().lower()
IS_MAC = (osName == 'darwin')
IS_WIN = (osName == 'windows')
IS_LINUX = (not IS_MAC) and (not IS_WIN)

APP_NAME = 'Image Editor'
COMPANY_NAME = "The Children's Hospital of Philadelphia"
COMPANY_URL = 'http://www.chop.edu'
COPYRIGHT = '(C) 2015 ' + COMPANY_NAME
DESCRIPTION = 'Simple image processing application'
DEVELOPERS = ''
VERSION = '0.1'