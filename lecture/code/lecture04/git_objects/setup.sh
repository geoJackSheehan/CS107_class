#!/usr/bin/env bash
rm -rf repo
mkdir -p repo

# initialize repository
cd repo
git init
git config user.name 'Dev Eloper'
git config user.email 'dev@eloper.org'

# create content
echo 'Hello CS107/AC207!' >hello.txt

# create commit
git add hello.txt
git commit -m 'Initial'
