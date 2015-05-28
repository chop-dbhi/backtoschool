# -*- mode: python -*-
a = Analysis(['runapp.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [('bw.py','editor/processing/bw.py','DATA')]
a.datas += [('custom.py','editor/processing/custom.py','DATA')]
a.datas += [('hello.py','editor/processing/hello.py','DATA')]
a.datas += [('sepia.py','editor/processing/sepia.py','DATA')]
a.datas += [('xray.py','editor/processing/xray.py','DATA')]


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('img', prefix='img'),
          a.zipfiles,
          a.datas,
          name='ImageEditor',
          debug=False,
          strip=True,
          upx=True,
          console=False , icon='icon.icns')
app = BUNDLE(exe,
             name='ImageEditor.app',
             icon='icon.icns')
