#!/bin/bash

echo "Enter a file name"
read filename

if [ -f "$filename" ]; then
	if [ -x "$filename" ]; then
		echo "File exists & executable"
	else
		echo "File exists & not executable"
	fi
	echo "File exists"
	exit 200
	echo $?

else
	echo "File does not exist"
	exit 201
	echo $?
fi

echo "Outside the if-block"
exit 0
echo $?


	
