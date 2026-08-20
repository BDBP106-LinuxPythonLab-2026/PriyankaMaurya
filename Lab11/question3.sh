#!/bin/bash



if [ -n "$string" ]; then
	echo "The string is empty"
else
	echo "The string is not empty"
fi
if [ -z "$string" ]; then
	echo "The string is empty"
else
	echo "The string is not empty"
fi
