#! /usr/bin/env python2
__name__ = "Text-File-Clear-Special-Symbols"
__author__ = "VegaS"
__date__ = "2019-11-13"
__version__ = "0.0.1"

import sys
import string
import os.path

if len(sys.argv) != 2:
	print("Drag the file that you want to fix to batch file.")
	sys.exit(0)


class ClearSpecialSymbols:
	SUFFIX_NAME = "_fixed"

	def __init__(self, fileName):
		fileNameSplit = os.path.splitext(fileName)
		self.fileName = fileName
		self.fileNameFixed = fileNameSplit[0] + self.SUFFIX_NAME + fileNameSplit[1]
		self.fileStringsAllowed = set(string.printable)

	def run(self):
		if os.path.getsize(self.fileName) == 0:
			print('File "{}" is empty.'.format(self.fileName))
			return

		file_data = []
		with open(self.fileName, 'r') as file:
			for line in file.readlines():
				if sys.version_info[0] < 3:
					file_data.append(filter(lambda x: x in self.fileStringsAllowed, line))
				else:
					file_data.append(''.join(list(filter(lambda x: x in self.fileStringsAllowed, line))))
			file.close()

		new_file = open(self.fileNameFixed, 'w')
		new_file.write(''.join(file_data))
		new_file.close()

		print('File: "{}" successfully saved!'.format(self.fileNameFixed))


cls = ClearSpecialSymbols(sys.argv[1])
cls.run()