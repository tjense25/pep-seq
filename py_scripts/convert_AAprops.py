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
				residue = columns[1]
				properties = columns[8:]
				properties = map(float, properties)
				self.AAdict[residue] = properties
		InFile.close()

props  = AAproperties()

residues = 'RHKDESTNQCGPAVILFMYW'
if len(sys.argv) == 2 and sys.argv[1].endswith('.csv'):
	InFile = open(sys.argv[1], 'rU')
	outFileName = 'arff_files' + sys.argv[1].strip('raw_data').strip('.csv') + '.AAprops.arff'
	OutFile = open(outFileName, 'w')
	OutFile.write('@relation pep-seq\n')
	AA_properties = ["acidR", "basicR", "sulfur", "hydroxy", "aromatic", "cyclic", "polarity", "charge", "hydrpthy", "MW"];
	for i in range(1, 9):
		for p in AA_properties:
			OutFile.write('@attribute pos%d%s NUMERIC\n' % (i, p))
	OutFile.write('@attribute toxicity  {toxic, neutral, anti-toxic}\n')
	OutFile.write('@data\n')
	linenumber = 0
	for line in InFile:
		if(linenumber == 0):
			linenumber += 1
			continue
		else:
			columns = line.strip('\n').split(',')
			pepseq = columns[0];
			toxicity = columns[8];
			for r in pepseq:
				for v in props.AAdict[r]:
					OutFile.write(str(v) + ',')
			OutFile.write('%s\n' % toxicity)
	InFile.close();
	OutFile.close();
else:
	print("ERROR")
