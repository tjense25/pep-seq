#!/bin/bash

MOTIFS=$(awk '/^[^#]/ {print $1}' $1 | ./convertToArffRegex.py)

echo "motif		toxic	neutral	anti"

totaltox=$(grep ',tox' $2 | wc -l)
totalneu=$(grep ',neu' $2 | wc -l)
totalanti=$(grep ',anti' $2 | wc -l)

for m in $MOTIFS
do
	grep "^$m" $2 > temp.txt
	tox=$(grep ',tox' temp.txt | wc -l)
	neu=$(grep ',neu' temp.txt | wc -l)
	anti=$(grep ',anti' temp.txt | wc -l)
	echo "$m	$tox	$neu	$anti"
done
