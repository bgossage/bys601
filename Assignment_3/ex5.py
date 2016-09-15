#!/usr/bin/python

from numpy import *

def conversion(x,y,z):
	X = array([ [x],[y],[z] ] )
	M = array([ [0.012938,0.000000,0.000000],[0.000000,0.012938,0.000000],[0.000000,0.000000,0.026878] ])
	NewX = dot(M,X)
	return NewX
	
InFile = open("/Users/joeng/Desktop/BYS601/5kxk.pdb","r")
OutFile = open("/Users/joeng/Desktop/BYS601/new_5kxk.pdb","w")

for line in InFile:
	if line.startswith("ATOM") or line.startswith("HETATM"):
		ATOM = line[0:6]
		AtomNumber = int(line[6:11] )
		AtomName = line[12:16]
		AminoAcid = line[16:17]
		AA = line[17:22]
		Chain = line[21:22]
		ResNumber = int(line[22:26])
		CodeInsert = line[26:27]
		x = float(line[30:38])
		y = float(line[38:46])
		z = float(line[46:54])
		O = float(line[54:60])
		Tm = float(line[60:66])
		element = line[76:78]
		
		A = conversion(x,y,z)  # Conversion to fractional coordinates
		
		x = A[0,0]
		y = A[1,0]
		z = A[2,0]
		
		Output = "%-6s%5d %4s%1s%3s %1s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f"\
%(ATOM, AtomNumber, AtomName, AminoAcid, AA, Chain, ResNumber, CodeInsert, x,y,z,\
O,Tm,element,charge)
		print Output
		OutFile.write(Output)
	
	else:
		print line
		OutFile.write(line)
InFile.close()
OutFile.close()

		