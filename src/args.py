import argparse, os, json
import logging


'''
Deal with app settings.
Loads previously saved and put commandline arguments over.
'''
class Args():
	appName = 'TemplatePySide'
	settingsFile = os.path.join(os.path.expanduser('~'), ".%s/%s.ini" % (appName,appName))

	args= None



	'''
	_reuseOld tells to load saved settings.
	If set, 'dst' is not required.
	'''
	def __init__(self, _reuseOld=True):
		if _reuseOld:
			self.args = self.load()

		if not self.args:
			self.args = {}


		cArgs = self.parseCmdline()

		if cArgs:
			for cArg in cArgs:
				if cArgs[cArg] != None:
					self.args[cArg] = cArgs[cArg]
		



	'''
	Save current settings to application related file.
	'''
	def save(self):
		settings = json.dumps(self.args, sort_keys=True, indent=4)

		try:
			if not os.path.exists(os.path.dirname(self.settingsFile)):
				os.makedirs(os.path.dirname(self.settingsFile))

			f = open(self.settingsFile, 'w')
			f.write(settings)
		except:
			logging.warning('Settings could not be saved.')
			return


		f.close()



	#private

	def load(self):
		try:
			f = open(self.settingsFile, 'r')
		except:
			logging.warning('No stored settings found.')
			return


		try:
			settingsStr = f.read()
		except:
			logging.warning('Setting file couldn\'t be read')
			return

		f.close()


		try:
			return json.loads(settingsStr)
		except:
			logging.warning('Setting file corrupt')
			return





# -todo 1 (clean, args) +0: make reliable args priority: defaults > .ini > cmdline
	def parseCmdline(self, _softDefs):
		cParser = argparse.ArgumentParser(description= 'PySide Template')

		cParser.add_argument('-tool', default=False, action='store_true', help='no caption borderless')
		cParser.add_argument('inStr', type=str, default='pwned', nargs=(None if 0 else '?'), help='Mandatory string input')
#		cParser.add_argument('-num', type=int, choices=[1,2], help='number setting', help=argparse.SUPPRESS)

		
		cArgs = cParser.parse_args()
	
		if cArgs:
			return vars(cArgs)


			