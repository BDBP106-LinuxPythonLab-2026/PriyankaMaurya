#!/bin/bash

#Multiplication table using until

echo "Enter a number:"
read number

i=1
until [ $i -gt 15 ]
do
	echo "$number*$i = $((number*i))"
	i=$((i+1))
done


