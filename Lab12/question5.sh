#!/bin/bash

# Function divide

divide()
{
	local num1=$1
	local num2=$2
	

if [ $num2 -eq 0 ]; then
	echo "Cannot divide by zero"
fi

local q=$(echo "scale=2 ; $1 / $2" | bc)
local r=$(echo "scale=1 ; $1 / $2" | bc)
echo "Quotient is: $q"
echo "Remainder is: $r"
}
result=$( divide 10 3 )
echo "$result"

