#!/bin/bash

read -ra numbers < nums.txt
echo "The numbers are:"

for i in "${numbers[@]}"
do
	echo $i
done

echo "Double numbers:"
for i in "${numbers[@]}"
do
	echo $((i*2))
done

