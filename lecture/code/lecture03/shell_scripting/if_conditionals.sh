#!/usr/bin/env bash
# File       : int_comparison.sh
# Description: Some string comparison examples
# Copyright 2022 Harvard University. All Rights Reserved.

if [ 'abc' == 'abc' ]; then
    echo "'abc' == 'abc'"
fi

str='' # empty string
if [ -z $str ]; then
    echo 'str is empty'
fi

if [ ! -z $str ]; then # negation
    echo 'str is not empty'
else
    echo 'str is empty'
fi

str='abc'
if [ -n $str ]; then # alternative: check if string is non-empty
    echo 'str is not empty'
fi
