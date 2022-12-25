#!/usr/bin/env bash
# File       : redirections.sh
# Description: Some redirection examples for stdout and stderr
# Copyright 2022 Harvard University. All Rights Reserved.

echo 'The `echo` command outputs to stdout:'
echo 'Hello CS107/AC207'
echo 'Hello CS107/AC207' >/dev/null # no output to stdout here

echo 'The `cp` command takes at least two arguments:'

cp >out1 # this will fail and print an error message on your screen.  The stdout
         # stream will be empty and so is the file out1

cp 2>/dev/null  # this will redirect the stderr stream into /dev/null.  You will
                # not see the error message on your screen

cp >out2 2>&1  # this will redirect both stdout and stderr to the file out2.
               # There will be no output on the screen
