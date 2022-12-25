#!/usr/bin/env bash
# File       : exercise_1.sh
# Description: Example script for Git workflow
# Copyright 2022 Harvard University. All Rights Reserved.

printf 'File to add: '
if ! read f; then 
    printf '\nCanceled\n'
    exit 1
fi

if ! git add -- "$f"; then
    exit 1
fi
# the `--` specifies 'end of command options'.  It is a measure to prevent
# unexpected side effects because the user input stored in variable `$f` could
# potentially be something that looks exactly like an option for `git add` (see
# `git help add` for what options are possible). If that would be the case
# (again it is a corner case) then the code would fail because `git add [some
# option parsed in $f]` would still expect a list of files to be added.  This
# list was expected to be contained in `$f` but it has been falsely interpreted
# as an option to `git add`.  See also
# https://askubuntu.com/questions/813303/whats-the-difference-between-one-hyphen-and-two-hyphens-in-a-command/813309#813309

git status
printf 'Create commit? (y/n) '
read cont
if [ "$cont" = n ]; then 
    printf '\nExiting\n'
    exit 1
fi

printf 'Commit message:  '
if ! IFS= read mess; then
    printf '\Canceled\n'
    exit 1
fi
# IFS (internal field separator) specifies which delimiter to use to split an
# input stream.  Because here the user is expected to input a commit message, a
# specific delimiter does not make sense and we want to avoid that the input
# stream is split in an unexpected position (e.g. at a comma).  Hence the IFS is
# set to nothing `IFS=` and the variable `mess` will contain only one continuous
# string instead of possibly an array of strings if the input stream has been
# split (unexpectedly).  It is a measure to prevent the code from having
# unexpected side effects.

if ! git commit -m "$mess"; then
    exit 1
fi

git status

printf 'Push? (y/n) '
read cont
if [ "$cont" = n ]; then
    printf '\nExiting\n'
    exit 1
fi

git push
exit 0
