#!/bin/bash

if [ -e "$listoffiles" ]; then
	echo "File exist"
else
	echo "File does not exist"
fi
if [ -s "$listoffiles" ]; then
	echo "File is not empty"
else
	echo "File is empty"
fi
if [ -f "$listoffiles" ]; then
	echo "It is a file"
else
	echo "It is not a file"
fi

# -e checks whether the file exist or not
# -s checks whether the file is empty or not
# -f checks whether the file is regular or not
