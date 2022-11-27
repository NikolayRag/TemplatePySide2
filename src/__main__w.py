from os import path

import Ui
from Args import *


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

	cUi = Ui.Ui(resUi, AppName, resIcon, resStyle)
	cUi.setup(Args.Cmdline.msg)
	cUi.go()
