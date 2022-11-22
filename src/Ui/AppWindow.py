from os import path
import logging


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




class AppWindow(QObject):
	modulePath= path.abspath(path.dirname(__file__))


	#support for window size/pos while maximized issue
	rtSize = [None, None]
	rtPos = [None, None]


	wMain = None
	wCaption = None
	wContent = None



	def ynBox(self, _txt, _txtQ, btnYes, btnNo, yesno=False):
		msgBox = QMessageBox()
		msgBox.setText(_txt)
		msgBox.setInformativeText(_txtQ)
		msgBox.setStandardButtons(btnYes | btnNo)
		msgBox.setDefaultButton(btnNo)
		if msgBox.exec() == (btnYes if yesno else btnNo):
			return True



########## -support



#specific logic relying on QT events order
# for (re)storing "true" window size/pos while maximized
	def moved(self, _e):
		if self.rtPos[1] != None:
			self.rtPos[0] = self.rtPos[1]
			self.rtPos[1] = self.wMain.pos()
		else:
			self.rtPos[1] = self.rtPos[0]



	def resized(self, _e):
		if self.rtSize[1] != None:
			self.rtSize[0] = self.rtSize[1]
			self.rtSize[1] = self.wMain.size()
		else:
			self.rtSize[1] = self.rtSize[0]


	def maximized(self, _e):
		if self.wMain.isMaximized():
			self.rtSize[1] = self.rtSize[0]
			self.rtPos[1] = self.rtPos[0]



	def tryExit(self, event):
		if self.ynBox("Out", "Maybe not?", QMessageBox.Ok, QMessageBox.Cancel):
			event.ignore()

		if event.isAccepted():
			logging.warning('left')
		else:
			logging.warning('stay')


		return True



	def dropped(self, _e):
		logging.warning(_e.mimeData().urls())



#########



	def __init__(self, _isTool=False, _isDnd=False):
		QObject.__init__(self)


		uiFile = path.join(self.modulePath,'AppWindow.ui')
		cMain = self.wMain = QUiLoader().load(uiFile)


		BindFilter({
				QEvent.Close: self.tryExit,
				QEvent.Move: self.moved,
				QEvent.Resize: self.resized,
				QEvent.WindowStateChange: self.maximized,
		 	},
		 	cMain
		 )


		#capture widgets
		self.wCaption= cMain.findChild(QWidget, "outerFrame")

		self.wContent= cMain.findChild(QWidget, "labContent")

		

		#update widgets state
		if _isTool:
			cMain.setWindowFlags(Qt.FramelessWindowHint)

			self.wCaption.installEventFilter( QWinFilter(cMain) )


		if _isDnd:
			logging.warning('Dnd on')

			BindFilter({
					QEvent.DragEnter: lambda e: e.acceptProposedAction(),
					QEvent.Drop: self.dropped,
			 	},
			 	cMain
		 	)



	def show(self):
		self.wMain.show()



	def setStyle(self, _styleFile):
		with open(_styleFile) as fQss:
			self.wMain.setStyleSheet(fQss.read())



	def setContent(self, _content):
		self.wContent.setText(_content)



	def windowGeometry(self, _size=None, _pos=None, maximize=None):
		if _size!=None and _pos!=None:
			self.wMain.resize( _size )

			self.wMain.move( _pos )

			if maximize:
				self.wMain.showMaximized()

			#marker values to pass to following events
			self.rtSize = [_size,None]
			self.rtPos = [_pos,None]


		return [self.rtSize[1], self.rtPos[1], self.wMain.isMaximized()]
