#!/usr/bin/env bash
# File       : file_check.sh
# Description: Test type of file passed as argument to the script
# Copyright 2022 Harvard University. All Rights Reserved.

if [ $# -ne 1 ]; then
    cat <<EOF
USAGE: $0 <path/to/file>

    More documentation here.  The form used here is called a here-document.
    They are very useful to write longer strings and expanding variables like
    \$0 above.  See https://tldp.org/LDP/abs/html/here-docs.html
EOF
    exit 1 # exit with failure code
fi

if [ -f $1 ]; then
    echo "File $1 exists and is a regular file"
elif [ -d $1 ]; then
    echo "File $1 exists and is a directory"
elif [ -e $1 ]; then
    # any other file type (character, block or symbolic link)
    echo "File $1 exists and is an unknown file"
fi
