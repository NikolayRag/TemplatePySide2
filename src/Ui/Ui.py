from .AppWindow import *


class Ui():
	args = None

	appWindow = None


	def __init__(self, _args):
		self.args = _args


		#init
		self.appWindow = AppWindow(_args.args['tool'])
		self.appWindow.setContent(_args.args['inStr'])


		self.appWindow.exec()

