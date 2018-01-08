
#! usr/bin/env python
import sys
import random

residues = 'RHKDESTNQCGPAVILFMYW'
if len(sys.argv) == 2 and sys.argv[1].endswith('.csv'):
	InFile = open(sys.argv[1], 'rU')
	outFileName = sys.argv[1].strip('.csv') + '.no_neutral.csv'
	OutFile = open(outFileName, 'w')
	linenumber = 0
	neutral_lines = []
	for line in InFile:
		if(linenumber == 0):
			linenumber += 1
			continue
		else:
			columns = line.strip('\n').split(',')
			toxicity = columns[8];
			if toxicity == 'neutral':
				neutral_lines.append(line)
			else:
				OutFile.write(line)
	#for i in random.sample(range(0, len(neutral_lines)), 5458):
		#OutFile.write(neutral_lines[i])
	InFile.close();
	OutFile.close();
else:
	print("ERROR")
