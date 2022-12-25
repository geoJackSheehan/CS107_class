#!/usr/bin/env bash
grep -c [0-9] apollo13.txt > out.txt
grep --help | grep '\--count'
ls *.py | wc -l
find . -type f ! -path "*/.*" ! -perm -o=rw | wc -l
find . -maxdepth 1 -name "[!.]*" \( -type f -or -type d \) ! -perm -o=rw | wc -l
