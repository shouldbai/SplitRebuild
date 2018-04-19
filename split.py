#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii

def avsplit1(s, n):
    fn = len(s)//n
    rn = len(s)%n
    ar = [fn+1]*rn+ [fn]*(n-rn)
    si = [i*(fn+1) if i<rn else (rn*(fn+1)+(i-rn)*fn) for i in range(n)]
    sr = [s[si[i]:si[i]+ar[i]] for i in range(n)]
    return sr

def splitFile(fileName):
	f = open(fileName, 'rb')
	bdata = f.read()
	hexdata = binascii.b2a_hex(bdata)
	strdata = (str(hexdata).split('\''))[1]
	sgroup = avsplit1(strdata, 240)

	#split into parts with the part of data as the name of files
	#prefix is the index of the part

	for index in range(len(sgroup)):
		oFileName = sgroup[index]
		prefix = str(index).zfill(8)
		of = open('output/' + prefix + "_" + oFileName, 'w')
		of.write('')


splitFile('test.docx')




