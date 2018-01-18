#! usr/bin/env python
import sys
import random
import re

#Function creates a set of motifs by randomly selecting
#4 out of 8 positions to put a random residue in
def createMotifs(num_to_create, residues):
	motifs = set()
	while len(motifs) < num_to_create:
		motif = []
		blank = random.sample(range(8), 4)
		for i in range(8):
			if i in blank:
				motif.append('*')
			else:
				motif.append(random.choice(residues))
		motifs.add(''.join(motif))
	return motifs

#Generates a randomly created peptide that matches a given motif
def getPepsMatchingMotif(num_to_create, motif, residues):
	peps = set()
	while len(peps) < num_to_create:
		pep = []
		for res in motif:
			if res == '*':
				pep.append(random.choice(residues))
			else:
				pep.append(res)
		peps.add(''.join(pep))
	return peps
			

def main():

	OutFile = open('arff_files/simulated_data/simulated_data_6.arff', 'w')

	toxic = set()
	neutral = set()
	antitoxic = set()
	
	residues = ['R','H','D','S','N','C','G','V','I','L','F','Y'] #Some residues not inluded because they're not present in original dataset

	motifs = createMotifs(300, residues)
	for i,motif in enumerate(motifs):
		if i < 100:
			toxic = toxic | getPepsMatchingMotif(10, motif, residues)
			toxicity = "toxic"
		elif i < 200:
			neutral = neutral | getPepsMatchingMotif(10, motif, residues)
			toxicity = "neutral"
		else:
			antitoxic = antitoxic | getPepsMatchingMotif(10, motif, residues)
			toxicity = "antitoxic"
		OutFile.write('%% %s: %s\n' % (motif, toxicity))

	OutFile.write('@relation pep-seq\n')

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
