#!/usr/bin/env bash
# File       : exercise_2.sh
# Description: Check for executable files in current directory
# Copyright 2022 Harvard University. All Rights Reserved.

for f in $(ls); do
    if [ -x "$f" ]; then
        echo "'$f' is executable"
    fi
done
