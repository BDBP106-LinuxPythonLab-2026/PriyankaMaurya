#!/bin/bash

sort -t "," -k2,2n "SOCR-HeightWeight_data.csv" > "Height_sorted.txt" 

tail -n2 "SOCR-HeightWeight_data.csv"
