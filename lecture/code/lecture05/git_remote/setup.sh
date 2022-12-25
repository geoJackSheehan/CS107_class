#!/usr/bin/env bash
# File       : setup.sh
# Description: Setup example Git repositories with a remote
# Copyright 2022 Harvard University. All Rights Reserved.
rm -rf git
mkdir -p git/remote

# initialize remote (bare repository)
(cd git/remote && git init --bare)

# initialize A
mkdir -p git/A
cd git/A
git init
git config user.name 'Developer A'
git config user.email 'A@domain.org'
git branch -M main

# setup the remote and create content
git remote add origin ../remote # no URL this time
echo 'Initial' >file
git add file
git commit -m 'Initial'
git push -u origin main

# B clones
cd .. # inside `git` directory
git clone remote B
cd B # inside repository B
git config user.name 'Developer B'
git config user.email 'B@domain.org'
git config branch.main.rebase 'false'
# default branch name already defined by A
