#! usr/bin/env python
import sys

def getAllPossibleKmers(k, kmer, kmers, residues):
	if k == 0:
		kmers.append(kmer)
		return kmers;
	for r in residues:
		kmers = getAllPossibleKmers(k - 1, r + kmer, kmers, residues);
	return kmers;

if len(sys.argv) == 3 and sys.argv[2].endswith('.csv'):
	k = int(sys.argv[1]);
	InFile = open(sys.argv[2], 'rU')
	outFileName = sys.argv[2].strip('.csv') + ('.%dmerprofile.arff'%k);
	OutFile = open(outFileName, 'w')
	OutFile.write('@relation pep-seq\n')
	kmers = []
	residues = ['R','H','D','S','N','C','G','V','I','L','F','Y']
	residue_attr = '{R, H, D, S, N, C, G, V, I, L, F, Y}'
	kmers = getAllPossibleKmers(k, '', kmers, residues)
	for i in range(8):
		OutFile.write('@attribute pos%d %s\n' % (i, residue_attr))
	for kmer in kmers:
		OutFile.write('@attribute %s NUMERIC\n'%kmer)
	OutFile.write('@attribute toxicity {anti-toxic, neutral, toxic}\n')
	OutFile.write('@data\n')
	for line in InFile:
		columns = line.strip('\n').split(',')
		sequence = columns[0]
		toxicity = columns[8]
		for i in range(len(sequence)):
			OutFile.write('%s,' % sequence[i])
		for kmer in kmers:
			OutFile.write('%d,' % sequence.count(kmer))	
		OutFile.write('%s\n' % toxicity)
	InFile.close()
	OutFile.close()

else:
	print('ERROR!\nUSAGE: python createKmerProfile.py [k] [InFile name]');
	
