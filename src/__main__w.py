from os import path

import Ui

from Args import *



class AppWindowLocal(Ui.AppWindow):
	def __init__(self, fileUi, fileStyle=None, isTray=False, isTool=False, isDnd=False):
		Ui.AppWindow.__init__(self, fileUi, fileStyle, isTray, isTool, isDnd)



AppName = 'TemplatePySide2'


AppPrefs = {
	'Application': { #window state holder
		'wFactor': [.8], #fraction of app over screen at first run
		'wSize': [None],
		'wPos': [None],
		'wMaxi': [False],
	},
	'Cmdline': {
		'tool': [0],
		'tray': [0],
		'dnd': [0],
		'hold': [0],
		'style': ['fusion'],
		'msg': ['pwned'],
	}
}


modulePath= path.abspath(path.dirname(__file__))
resUi = path.join(modulePath,'Ui/AppWindow.ui')
resIcon = path.join(modulePath,'Ui/icons/icon-app.svg')
resStyle = path.join(modulePath,'Ui/styles/default.qss')



if __name__ == '__main__':
	Args(AppPrefs, AppName, cmdlineBlock='Cmdline')

	cUi = Ui.Ui(AppName, resIcon)

	appWindow = AppWindowLocal(
		resUi,
		fileStyle=resStyle,
		isTool=Args.Cmdline.tool,
		isTray=Args.Cmdline.tray,
		isDnd=Args.Cmdline.dnd
	)
	cUi.setupWin(appWindow)(Args.Cmdline.msg)

	cUi.go()
