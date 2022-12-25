#!/usr/bin/env bash
# File       : int_comparison.sh
# Description: Integer comparison based on number of arguments given to the
#              script
# Copyright 2022 Harvard University. All Rights Reserved.

if [ $# -gt 2 ]; then
    echo "Number of arguments $# is larger than two"
else
    echo "Number of arguments $# is less than or equal to two"
fi
