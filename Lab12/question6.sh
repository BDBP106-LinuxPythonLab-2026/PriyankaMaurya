#!/bin/bash

Maximum () {
	local num1=$1
	local num2=$2
	if [ $num1 -ge $num2 ]; then
		echo "$num1"
	else
		echo "$num2"
	fi
}
Maximum_value=$(Maximum 55 30)
echo "Maximum value is $Maximum_value"

