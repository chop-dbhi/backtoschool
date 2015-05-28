# -*- mode: python -*-
# This is a PyInstaller script to for packaging the code into a standalone application for  Windows

a = Analysis(['runapp.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [('bw.py','editor\\processing\\bw.py','DATA')]
a.datas += [('custom.py','editor\\processing\\custom.py','DATA')]
a.datas += [('hello.py','editor\\processing\\hello.py','DATA')]
a.datas += [('sepia.py','editor\\processing\\sepia.py','DATA')]
a.datas += [('xray.py','editor\\processing\\xray.py','DATA')]

# to address the warning "file already exists but should not: C:\Users\<username>\AppData\Local\Temp\_MEI<...>\Include\pyconfig.h":

for d in a.datas:
    if 'pyconfig' in d[0]: 
        a.datas.remove(d)
        break


"""
msvc*.dll files listed below and the manifest file can be re-distributed under the license terms for Microsoft Visual C++ 2008 Express edition. They are required by Python because it was compiled using Visual C++ 2008. All other Microsoft dlls that PyInstaller tries to include will be removed.

Microsoft.VC90.CRT.manifest
msvcm90.dll
msvcp90.dll
msvcr90.dll

"""

microsoftInclude = TOC([('Microsoft.VC90.CRT.manifest', 'C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT\\Microsoft.VC90.CRT.manifest', 'BINARY'),
('msvcm90.dll', 'C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT\\msvcm90.dll', 'BINARY'),
('msvcp90.dll', 'C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT\\msvcp90.dll', 'BINARY'),
('msvcr90.dll', 'C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT\\msvcr90.dll', 'BINARY')])

microsoftExclude = ['Microsoft.VC90.CRT.manifest', 'msvcm90.dll', 'msvcp90.dll', 'msvcr90.dll', 'Microsoft.VC90.MFC.manifest', 'mfc90.dll', 'mfc90u.dll', 'mfcm90.dll', 'mfcm90u.dll', 'kernel32']

a.binaries = [b for b in a.binaries if (not b[0] in microsoftExclude)]


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('img', prefix='img'),
          a.zipfiles,
          a.datas,
          microsoftInclude,
          name='ImageEditor.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icon.ico')