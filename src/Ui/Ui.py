from Args import *

from .AppWindow import *


class Ui():
	qApp = None

	appWindow = None



	def __init__(self):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('fusion'))


		#init
		self.appWindow = AppWindow(Args.Cmdline.tool)
		self.appWindow.setContent(Args.Cmdline.msg)


		self.appWindow.show()
		self.qApp.exec_()


		logging.warning('Exiting')
