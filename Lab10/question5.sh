#!/bin/bash

echo -n "Enter a score:"
read n

if [ "$n" -ge 90 ];then
	echo "A"
	
elif [ "$n" -ge 80 ];then
	echo "B" 
      
elif [ "$n" -ge 70 ];then
	echo "C"
else 
	echo "Fail"
fi


