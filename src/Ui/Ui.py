from Args import *

from .AppWindow import *


class Ui():
	modulePath= path.abspath(path.dirname(__file__))


	qApp = None

	appWindow = None



	def __init__(self):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('fusion'))


		#init
		self.appWindow = AppWindow(Args.Cmdline.tool)
		self.appWindow.setStyle(f"{self.modulePath}/schemes/default.qss")
		self.appWindow.setContent(Args.Cmdline.msg)


		self.appWindow.show()
		self.qApp.exec_()


		logging.warning('Exiting')
