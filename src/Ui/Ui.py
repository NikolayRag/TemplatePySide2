from Args import *

from .AppWindow import *


class Ui():
	modulePath= path.abspath(path.dirname(__file__))


	qApp = None

	appWindow = None



	def __init__(self):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('fusion'))


		#read geo
		cPos = Args.Application.wPos and QPoint(*Args.Application.wPos)
		cPos = cPos or QPoint(0,0)

		cSize = Args.Application.wSize and QSize(*Args.Application.wSize)
		cSize = cSize or QApplication.primaryScreen().size()


		self.appWindow = AppWindow(Args.Cmdline.tool)
		self.appWindow.setStyle(f"{self.modulePath}/schemes/default.qss")
		self.appWindow.setContent(Args.Cmdline.msg)
		self.appWindow.windowGeometry(cSize, cPos, Args.Application.wMaxi)


		self.appWindow.show()
		self.qApp.exec_()


		#store geo
		wSize = self.appWindow.windowGeometry()
		Args.Application.wSize = (wSize[0].width(), wSize[0].height())
		Args.Application.wPos = (wSize[1].x(), wSize[1].y())
		Args.Application.wMaxi = wSize[2]


		logging.warning('Exiting')
