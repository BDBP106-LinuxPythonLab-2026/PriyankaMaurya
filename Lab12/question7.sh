#!/bin/bash

check_directory() {
	local dir=$1
	if [ ! -d "$dir" ]; then
		mkdir "$dir"
		echo "Directory "$dir" did not exist"
	else
		echo "Directory "$dir" exist"
	fi
}
check_directory "Testdir"
