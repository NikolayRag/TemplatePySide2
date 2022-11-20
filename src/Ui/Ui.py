from Args import *

from .AppWindow import *


class Ui():
	args = None

	appWindow = None


	def __init__(self):

		#init
		self.appWindow = AppWindow(Args.Cmdline.tool)
		self.appWindow.setContent(Args.Cmdline.msg)


		self.appWindow.exec()

		logging.warning('Exiting')
		self.args.save()
