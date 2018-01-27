#!/usr/bin/python
import sys

def convertToArffRegex(regex):
	regex_list = list(regex.strip())
	arff_regex = ','.join(regex_list)
	return arff_regex

def main():
	for line in sys.stdin:
		print(convertToArffRegex(line))

if __name__ == "__main__":
	main()
