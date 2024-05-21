import Ui

from PySide2.QtWidgets import *



'''
Example App window
'''
class myLittleWin(Ui.AppWindow):
	wContent = None



	def __init__(self, fileUi, fileStyle=None, isTray=False, isTool=False, isDnd=False):
		Ui.AppWindow.__init__(self, fileUi, fileStyle, isTray, isTool, isDnd)

		self.wContent= self.wMain.findChild(QWidget, "labContent")



	def setupWin(self, _content):
		self.wContent.setText(_content)
