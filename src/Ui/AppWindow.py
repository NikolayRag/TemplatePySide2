from os import path

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

from .BindFilter import *



'''
Draggable support example
'''
class QWinFilter(QObject):
	mouseOffset= None

	def __init__(self, _base):
		super().__init__(_base)


	def eventFilter(self, obj, event):
		if event.type() == QEvent.MouseButtonPress:
			self.mouseOffset= event.globalPos()-obj.window().pos()
			return True

		if event.type() == QEvent.MouseButtonRelease:
			self.mouseOffset= False
			return True

		if event.type() == QEvent.MouseMove and self.mouseOffset:
			obj.window().move(event.globalPos()-self.mouseOffset)
			return True
			
		return False




class AppWindow():
	modulePath= path.abspath(path.dirname(__file__))


	qApp = None


	wMain = None
	wCaption = None
	wContent = None



	def __init__(self, _isTool=False):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('plastique'))

		uiFile = path.join(self.modulePath,'AppWindow.ui')
		cMain = self.wMain = QUiLoader().load(uiFile)


		#capture widgets
		self.wCaption= cMain.findChild(QWidget, "outerFrame")

		self.wContent= cMain.findChild(QWidget, "labContent")

		

		#update widgets state
		if _isTool:
			cMain.setWindowFlags(Qt.FramelessWindowHint)

			self.wCaption.installEventFilter( QWinFilter(cMain) )





	'''
	Display UI and enter QT app loop
	'''
	def exec(self):
		self.wMain.show()


		self.qApp.exec_()


	def setContent(self, _content):
		self.wContent.setText(_content)

