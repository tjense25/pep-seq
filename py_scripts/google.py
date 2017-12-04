#! usr/bin/env python
import sys

def getTuple(version):
	numbers = version.split('.');
	if len(numbers) == 1:
		return (int(numbers[0]), -1, -1)
	elif len(numbers) == 2:
		return (int(numbers[0]), int(numbers[1]), -1)
	elif len(numbers) == 3:
		return (int(numbers[0]), int(numbers[1]), int(numbers[2]))

def convertBack(tuple_list):
	version_list = [];
	for tup in tuple_list:
		version = ''
		version += str(tup[0])
		if tup[1] >= 0:
			version += ".%d" % tup[1]
		if tup[2] >= 0:
			version += ".%d" % tup[2]
		version_list.append(version)
	return version_list

def compare(tup1, tup2):
	if cmp(tup1[0], tup2[0]) == 0:
		if cmp(tup1[1], tup2[1]) == 0:
			return cmp(tup1[2], tup2[2])
		else:
			return cmp(tup1[1], tup2[1])
	else:
		return cmp(tup1[0], tup2[0])

def sort(tuple_list):
	for i in range(0, len(tuple_list) - 1):
		print(tuple_list)
		min = tuple_list[i]
		min_pos = i
		for j in range(i + 1, len(tuple_list)):
			if compare(tuple_list[j], min) < 0:
				min_pos = j
				min = tuple_list[j]
		temp = tuple_list[i]
		tuple_list[i] = min
		tuple_list[min_pos] = temp
	return tuple_list

def answer(l):
	tuple_list = []
	for version in l:
		tuple_list.append(getTuple(version))
	tuple_list = sort(tuple_list)
	version_list = convertBack(tuple_list)
	return version_list

l = ["3.4.1", "1", "2.1.2", "1.1", "0.0.3", "1.4"]
l = answer(l)
print(l)
		
