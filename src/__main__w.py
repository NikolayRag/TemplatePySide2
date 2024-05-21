from os import path

import Ui
from Ui.myLittleWin import *

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
		'loglevel': [10,[0,50],int,"Logging level"],
		'tool': [0],
		'tray': [0],
		'dnd': [0],
		'hold': [0],
		'style': ['fusion'],
		'msg': ['pwned'],
	}
}


modulePath= path.abspath(path.dirname(__file__))
resUi = path.join(modulePath,'Resource/AppWindow.ui')
resIcon = path.join(modulePath,'Resource/icons/icon-app.svg')
resStyle = path.join(modulePath,'Resource/styles/default.qss')



if __name__ == '__main__':
	Args(AppPrefs, AppName, cmdlineBlock='Cmdline')
	logging.basicConfig(level=Args.Cmdline.loglevel)
	


	cUi = Ui.Ui(AppName, resIcon)

	appWindow = myLittleWin(
		resUi,
		fileStyle=resStyle,
		isTool=Args.Cmdline.tool,
		isTray=Args.Cmdline.tray,
		isDnd=Args.Cmdline.dnd
	)
	appWindow.setupWin(Args.Cmdline.msg)

	cUi.setupUi(appWindow)

	cUi.go()
