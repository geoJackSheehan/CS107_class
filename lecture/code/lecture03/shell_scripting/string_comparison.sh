#!/usr/bin/env bash
# File       : string_comparison.sh
# Description: Example for comparing string argument
# Copyright 2022 Harvard University. All Rights Reserved.

if [ "$1" == 'Hello CS107/AC207!' ]; then
    echo 'Success!'
else
    echo 'Got unexpected string argument'
fi
