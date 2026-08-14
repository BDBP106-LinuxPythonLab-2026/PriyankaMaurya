#!/bin/bash


echo "Input a number:"
read n

if [ "$n" -gt 100 ]; then #Here the double bracket error is fixed and closed the bracket with square bracket only.
	echo "The number is greater than 100."
elif [ "$n" -le 100 ]; then #Here else condition is an error to fix it we have used elif condition to rectify it.
	echo "The number is not greater than 100."
elif [ "$n" -gt 100 ]; then #Here if condition rectify with elif condition, double bracket is an error and closing of bracket is only with square bracket only and semicolon is used after the square bracket.
	echo "The number is greater than 100."
fi
