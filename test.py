import os
import sys
import os
from pathlib import Path
from readfile import readfile
if __name__ == "__main__":
	rf = readfile()
	dictTrain = rf.returnTheDict("C:/Users/26400/OneDrive/Desktop/PA4/train.txt")
	print(len(dictTrain))

	for item in dictTrain:
		print("key is ",item)
		print("value is ",dictTrain[item])

	"""
	path = sys.path[0]
	path = path + "aug.txt"
	f = open(path,"r")
	for line in f:
		print(line)
"""