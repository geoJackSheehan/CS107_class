#!/usr/bin/env bash
for f in $(find . -maxdepth 1 -type f); do
    echo "${f##*/} $(cat $f | sed -r '/^\s*$/d' | wc -l)"
done
