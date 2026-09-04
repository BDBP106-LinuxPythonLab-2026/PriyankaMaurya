#!/bin/bash

while IFS=read -r a b c d 
do
	if (( a % 2 == 0 && b % 2 == 0 && c % 2 == 0 && d % 2 ))
	then
		echo "$a $b $c $d"
	fi
done < "SOCR-HeightWeight_data.csv"
