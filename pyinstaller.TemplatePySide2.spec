# -*- mode: python -*-

block_cipher = None


a = Analysis(['src/__main__w.py'],
	pathex=[''],
	binaries=None,
	datas=[
		('src/Resource/AppWindow.ui', 'Resource'),
		('src/Resource/icons/icon-app.svg', 'Resource/icons'),
		('src/Resource/styles/default.qss', 'Resource/styles'),
#		('bin/bin.exe','src/bin/bin.exe','DATA'),
	],
	hiddenimports=['PySide2.QtXml'],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='TemplatePySide2',
          debug=False,
          strip=False,
          upx=True,
          console=False )
 