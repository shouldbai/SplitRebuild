#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii
import os
import os.path

#filepath
#n is the length of the index eg.00000235 ,n = 8,start with 0
def rebuildFile(filepath, n):
	files = os.listdir(filepath)
	files.sort()
	for index in range(len(files)):
		files[index] = (files[index].split('_'))[1]
	return files

def rebuild(outFileName):
	outHexStr = ''.join(rebuildFile('output', 8))
	#output to a new file
	outputBinData = binascii.a2b_hex(outHexStr)
	ofile = open(outFileName,'wb')
	ofile.write(outputBinData)

rebuild('newFile.docx')