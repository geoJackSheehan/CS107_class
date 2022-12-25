#!/usr/bin/env bash
rm -rf local remote
mkdir -p local
mkdir -p remote

# initialize remote
(cd remote && git init --bare)

# initialize repository
cd local
git init
git config user.name 'CS107/AC207 Developer'
git config user.email 'dev@harvard.edu'
git remote add origin ../remote
git branch -M main

# create content
echo 'Initial HW4 P2' >file
git add file
git commit -m 'Initial'
git push -u origin main

# create modifications
echo "Some changes added to file" >>file
git add file
git commit -m "Some more changes added to file"

echo "Forgot to add this line" >>file
git add file
git commit -m "Forgot to add some code (will fixup later)"

echo "Groundbreaking changes that will change how we see the world today!" >>file
git add file
git commit -m "Minor (bad commit message will reword later)"

echo "This code adds a new feature" >>file
git add file
git commit -m "Adding new feature to code"

echo "Adding component A to new feature" >>file
git add file
git commit -m "Extending new feature with component A"

echo "Adding component B to new feature" >>file
git add file
git commit -m "Extending new feature with component B"
