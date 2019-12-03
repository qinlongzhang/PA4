import numpy as np
from collections import OrderedDict
class readfile:
	def __init__(self):
		self.allCharacterDict = OrderedDict()
		self.allCharacterDict ["!!!!"] = ""
		self.allCharacterDict["\n"] = ""
		self.noteList = []
		self.noteList.append("!!!!")
		self.noteList.append("\n")



	def readTheFile(self,filename):
		f = open(filename)
		for line in f:
			if line == "<start>\n":
				self.allCharacterDict["~~"] = ""
				self.noteList.append("~~")
			elif line == "<end>\n":
				self.allCharacterDict["~~~"] = ""
				self.noteList.append("~~~")
			else:
				for char in line:
					if char not in self.allCharacterDict:
						self.allCharacterDict[char] = ""
						self.noteList.append(char)

	def oneHotDotConverter(self):
		entryLength = len(self.allCharacterDict)
		for idx,eachItem in enumerate(self.allCharacterDict):
			oneHotDot = np.zeros(entryLength).astype("float32")
			oneHotDot[idx] = 1
			self.allCharacterDict[eachItem] = oneHotDot



	def returnTheDict(self,filename):
		self.readTheFile(filename)
		self.oneHotDotConverter()
		return self.allCharacterDict

	def getKeyIndex(self,value):
		return np.argmax(value)




