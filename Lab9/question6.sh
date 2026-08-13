#!/bin/bash

echo "HOME directoty is"
echo "$HOME"

echo "Calculation : $bc_output
bc_output=$(bc << EOF
scale=5
23934/44343
EOF
)"

echo "Files starting with D:"
ls $HOME | grep " D "


echo "Username details from /etc/passwd. :"
grep "$USERNAME" /etc/passwd
