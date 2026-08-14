#!/bin/bash

echo "Enter file name:"
read file

if [ -f "$file" ]; then
	echo "File exist"
	
	if [ -x "$file" ]; then
	echo "File exist & is executable"

else
	echo "The file is not executable"
fi
else
	echo "The file does not exists"
fi	
