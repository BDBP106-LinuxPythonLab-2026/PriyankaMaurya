#!/bin/bash


mass=1
energy=3
speed=3*10^8
Energy=$(bc << EOF
$mass*$speed*$speed
EOF
)

echo "Calculating energy-mass equivalence :$Energy J"
 
