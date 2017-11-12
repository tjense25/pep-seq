#! usr/bin/env python
import sys

if len(sys.argv) == 3 and sys.argv[1].endswith('.csv'):
	InFile = open(sys.argv[1], 'rU')
	OutFile = open(sys.argv[2], 'w')
	OutFile.write("@relation toxic\n")
	res_nominal = '{R,H,D,S,N,C,G,V,I,L,F,Y}'
	for i in range(8):
		OutFile.write('@attribute pos%d %s\n' % (i, res_nominal))
	OutFile.write('@data\n')
	for line in InFile:
		columns = line.strip('\n').split(',')
		sequence = columns[0]
		toxicity = columns[8]
		if toxicity != 'toxic': continue
		data = []
		for r in sequence:
			data.append(r)
			data.append(',')
		data[len(data) - 1] = "\n"
		OutFile.write("".join(data))
	InFile.close()
	OutFile.close()
else:
	print("ERROR\nUSAGE: python py_scripts/getToxic.py Input_data.csv arff_files/Output_file.arff")
