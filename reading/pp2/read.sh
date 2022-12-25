#!/usr/bin/env bash

read -p "please enter a message ;" continue_msg

printf '%s\n' "$continue_msg"

# What if 
#printf "$continue_msg"

if [[ "$continue_msg" = "N" ]]; then
	exit 1
else
	printf "success\n"
fi
