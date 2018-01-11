#! usr/bin/env python	
import sys

class AAproperties:
	
	def __init__(self):
		self.AAdict = {}
		InFile = open('/fslhome/tjense25/fsl_groups/fslg_genome/pep_seq/tanner/py_scripts/AAproperties.txt', 'rU');
		inTable = None
		for line in InFile:
			if line.startswith("Ala"):
				inTable = True
			if inTable:
				columns = line.strip('\n').split('\t')
				residue = columns[0]
				properties = columns[2:]
				self.AAdict[residue] = properties
		InFile.close()
		print(self.AAdict)



x = AAproperties()
