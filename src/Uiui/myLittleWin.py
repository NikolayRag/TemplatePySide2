import Uiui

from PySide2.QtWidgets import *



'''
Example App window
'''
class myLittleWin(Uiui.AppWindow):
	wContent = None



	def __init__(self, fileUi, fileStyle=None, isTray=False, isTool=False, isDnd=False):
		Uiui.AppWindow.__init__(self, fileUi, fileStyle, isTray, isTool, isDnd)

		self.wContent= self.wMain.findChild(QWidget, "labContent")



	def setupWin(self, _content):
		self.wContent.setText(_content)
