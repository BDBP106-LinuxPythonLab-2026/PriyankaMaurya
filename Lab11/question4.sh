#!/bin/bash

var1="Priyanka"
var2="maurya"

if [ "$var1" > "$var2" ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

var1="Priyanka"
var2="maurya"

if [ "$var1" \> "$var2" ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

