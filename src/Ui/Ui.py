from Args import *

from .AppWindow import *


class Ui():
	modulePath= path.abspath(path.dirname(__file__))

	resUi = path.join(modulePath,'AppWindow.ui')
	resIcon = path.join(modulePath,'icons/icon-app.svg')
	resStyle = path.join(modulePath,'styles/default.qss')


	qApp = None

	trayIcon = None



	def initApp(self, _appName):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('fusion'))
		self.qApp.setWindowIcon(QIcon(self.resIcon))
		if _appName:
			self.qApp.setApplicationName(_appName)



	def initTray(self):
		self.trayIcon = QSystemTrayIcon(QIcon(self.resIcon))

		self.trayIcon.show()



	def windowStart(self):
		cPos = Args.Application.wPos and QPoint(*Args.Application.wPos)
		cPos = cPos or QPoint(0,0)

		cSize = Args.Application.wSize and QSize(*Args.Application.wSize)
		cSize = cSize or QApplication.primaryScreen().size()


		appWindow = AppWindow(
			self.resUi,
			resStyle=self.resStyle,
			isTool=Args.Cmdline.tool,
			isTray=Args.Cmdline.tray,
			isDnd=Args.Cmdline.dnd
		)
		appWindow.windowGeometry(cSize, cPos, Args.Application.wMaxi)


		return appWindow



	def windowSave(self, _window):
		wSize = _window.windowGeometry()
		Args.Application.wSize = (wSize[0].width(), wSize[0].height())
		Args.Application.wPos = (wSize[1].x(), wSize[1].y())
		Args.Application.wMaxi = wSize[2]



	def __init__(self, appName=None):
		self.initApp(appName)


		appWin = self.windowStart()
		if Args.Cmdline.tray:
			self.initTray()

			self.trayIcon.activated.connect(appWin.miniTray)


		appWin.setContent(Args.Cmdline.msg)

		appWin.show()

		self.qApp.exec_()

		self.windowSave(appWin)


		logging.warning('Exiting')
