#!/bin/bash

#Q1)
var1="Testing"
var2="testing"

#Q2)
if [ "$var1" > "$var2" ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

#Q3)
var1="Testing"
var2="testing"

if [ "$var1" \> "$var2" ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

#Q4)
echo "Testing" > teststringfile
echo "testing" >> teststringfile


