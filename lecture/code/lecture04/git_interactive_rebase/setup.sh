#!/usr/bin/env bash
rm -rf git
mkdir -p git/repo
mkdir -p git/remote

# initialize remote
(cd git/remote && git init --bare)

# initialize repository
cd git/repo
git init
git config user.name 'Dev Eloper'
git config user.email 'dev@eloper.org'
git remote add origin ../remote
git branch -M main

# create content
echo 'Initial' >file
git add file
git commit -m 'Initial'
git push -u origin main

# create modifications
for (( i = 1; i < 11; i++ )); do
    echo "Modification ${i}" >>file

    # create commit
    git add file
    git commit -m "Modification ${i}"
done
