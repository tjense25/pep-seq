#! usr/bin/env python
import sys

if len(sys.argv) == 2:
	InFile = open(sys.argv[1], 'rU')
	linenumber = 0
	joinedSeq = ''
	for line in InFile:
		if(linenumber == 0):
			linenumber += 1
			continue;
		else:
			columns = line.strip('\n').split(',')
			joinedSeq += columns[0]
	InFile.close()
	for aa in 'ACDEFGHIKLMNPQRSTVWY':
		count = joinedSeq.count(aa)
		print('%s: %d' % (aa, count))
