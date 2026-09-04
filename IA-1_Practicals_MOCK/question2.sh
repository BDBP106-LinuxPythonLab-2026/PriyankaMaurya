#!/bin/bash

sort -t"," -k1,1 'pig_weights.csv' > column1.txt
sort -t"," -k2,2 'pig_weights.csv' > column2.txt
sort -t"," -k3,3 'pig_weights.csv' > column3.txt
sort -t"," -k4,4 'pig_weights.csv' > column4.txt
