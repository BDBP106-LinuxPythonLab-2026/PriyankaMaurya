#!/bin/bash

echo -n "Enter a number:"
read number

if [ "$number" -ge 1 ]; then
	echo "Positive"
elif [ "$number" -lt 1 ]; then
		echo "negative"
	else
		echo "zero"
		
		fi
