from os import path

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *


class Object():
	None



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
	qApp = None

	layout = Object()
	layout.main = None
	layout.drag = None
	layout.content = None

	modulePath= path.abspath(path.dirname(__file__))



	def __init__(self, _isTool=False):
		self.qApp = QApplication()
		self.qApp.setStyle(QStyleFactory.create('plastique'))

		uiFile = path.join(self.modulePath,'AppWindow.ui')
		cMain = self.layout.main = QUiLoader().load(uiFile)


		#capture widgets
		self.layout.drag= cMain.findChild(QWidget, "outerFrame")

		self.layout.content= cMain.findChild(QWidget, "labContent")

		

		#update widgets state
		if _isTool:
			cMain.setWindowFlags(Qt.FramelessWindowHint)

			self.layout.drag.installEventFilter( QWinFilter(cMain) )





	'''
	Display UI and enter QT app loop
	'''
	def exec(self):
		self.layout.main.show()


		self.qApp.exec_()


	def setContent(self, _content):
		self.layout.content.setText(_content)

