import Ui
from Args import *


AppPrefs = {
	'Application': {
		'wSize': [None],
		'wPos': [None],
		'wMaxi': [False],
	},
	'Cmdline': {
		'tool': [0],
		'tray': [0],
		'dnd': [0],
		'hold': [0],
		'msg': ['pwned'],
	}
}

if __name__ == '__main__':
	Args(AppPrefs, 'TemplatePySide', 'Cmdline')

	Ui.Ui('TemplatePySide')
