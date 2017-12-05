#! usr/bin/env python
import sys
import random
import re

def main():
	OutFile = open('arff_files/simulated_data/simulated_data_2.arff', 'w')
	OutFile.write('@relation pep-seq\n')
	residues = ['R','H','D','S','N','C','G','V','I','L','F','Y']

	for i in range(8):
		OutFile.write('@attribute pos%d {' % i)
		for r in residues:
			if r == 'R':
				OutFile.write('R')
				continue
			OutFile.write(',%s' % r)
		OutFile.write('}\n')

	OutFile.write('@attribute toxicity {antitoxic, neutral, toxic}\n')
	OutFile.write('@data\n')

	toxic = set()
	neutral = set()
	antitoxic = set()

	#generate random data that matches the motif C**VY**F and call these peptides toxic
	for i in range(750):
		toxic_peptide = []
		toxic_peptide.append('C')
		toxic_peptide.extend(random.sample(residues, 2))
		toxic_peptide.append('V')
		toxic_peptide.append('Y')
		toxic_peptide.extend(random.sample(residues, 2))
		toxic_peptide.append('F')
		toxic.add(''.join(toxic_peptide))

	#generate random data that matches **IL*D*S
	for i in range(750):
		toxic_pep = []
		toxic_pep.extend(random.sample(residues, 2))
		toxic_pep.extend(['I', 'L'])
		toxic_pep.append(random.choice(residues))
		toxic_pep.append('D')
		toxic_pep.append(random.choice(residues))
		toxic_pep.append('S')
		toxic.add(''.join(toxic_pep))

	#generate toxic data that partially matches an antitoxic motif
	#match motif HV***NF*
	for i in range(750):
		toxic_pep = []
		toxic_pep.extend(['H', 'V'])
		toxic_pep.extend(random.sample(residues, 3))
		toxic_pep.extend(['N', 'F'])
		toxic_pep.extend(random.choice(residues))
		toxic.add(''.join(toxic_pep))

	#generates random data that matches the simulated antitoxic motif HVV***G*
	for i in range(1000):
		antitoxic_peptide = []
		antitoxic_peptide.append('H')
		antitoxic_peptide.append('V')
		antitoxic_peptide.append('V')
		antitoxic_peptide.extend(random.sample(residues, 3))
		antitoxic_peptide.append('G')
		antitoxic_peptide.append(random.choice(residues))
		antitoxic.add(''.join(antitoxic_peptide))

	#generates random antitoxic peps matching motif **RRVR**
	for i in range(1000):
		antitoxic_pep = []
		antitoxic_pep.extend(random.sample(residues, 3))
		antitoxic_pep.extend(['R', 'R', 'V', 'R'])
		antitoxic_pep.extend(random.sample(residues, 2))
		antitoxic.add(''.join(antitoxic_pep))
		

	#generate partial mathces for the toxic sequences
	for i in range(500):
		neutral_peptide = []
		neutral_peptide.append('C')
		neutral_peptide.extend(random.sample(residues, 2))
		neutral_peptide.append('V')
		neutral_peptide.extend(random.sample(residues, 3))
		neutral_peptide.append('F')
		neutral_peptide = ''.join(neutral_peptide)
		if re.search(r'C\w\wVY\w\wF', neutral_peptide):
			continue
		else:
			neutral.add(neutral_peptide)
	
	#generate partial matches for antitoxic sequence
	for i in range(500):
		neutral_peptide = []
		neutral_peptide.append('H')
		neutral_peptide.extend(random.choice(residues))
		neutral_peptide.append('V')
		neutral_peptide.extend(random.sample(residues, 3))
		neutral_peptide.append('G')
		neutral_peptide.append(random.choice(residues))
		neutral_peptide = ''.join(neutral_peptide)
		if re.search(r'HVV\w\w\wG\w', neutral_peptide):
			continue
		else:
			neutral.add(neutral_peptide)


	#generate random peptides that do not match either motif, call them neutral
	for i in range(2000):
		neutral_peptide = []
		neutral_peptide.extend(random.sample(residues, 8))
		neutral_peptide = ''.join(neutral_peptide)
		if re.search(r'C\w\wVY\w\wF', neutral_peptide):
			continue
		elif re.search(r'\w\wIL\wD\wS', neutral_peptide):
			continue
		elif re.search(r'HV\w\w\wNF\w', neutral_peptide):
			continue
		elif re.search(r'HVV\w\w\wG\w', neutral_peptide):
			continue
		elif re.search(r'\w\wRRVR\w\w', neutral_peptide):
			continue
		else:
			neutral.add(neutral_peptide)

	for tox_pep in toxic:
		for i in range(8):
			OutFile.write('%s,' % tox_pep[i])
		OutFile.write('toxic\n')
	for neu_pep in neutral:
		for i in range(8):
			OutFile.write('%s,' % neu_pep[i])
		OutFile.write('neutral\n')
	for antitox_pep in  antitoxic:
		for i in range(8):
			OutFile.write('%s,' % antitox_pep[i])
		OutFile.write('antitoxic\n')
	OutFile.close()

	
if __name__ == '__main__':
	main()
