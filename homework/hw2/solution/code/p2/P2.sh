#!/usr/bin/env bash
# File       : P2.sh
# Description: Problem 2 Git remotes replay script (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
rm -rf git
mkdir git
cd git

# a.) instead of moving out of an already existent Git repository, you can also
# add the directory created by this script to your .gitignore file.  Do not add
# nested Git repositories to your history (the .gitignore will avoid this).
mkdir 'bare' 'local' 'sandbox'
(cd bare && git init --bare && ls)
(cd local && git init && git branch -M main && ls .git)
(cd sandbox && git init && git branch -M main && touch file && git add file &&
    git commit -m 'Initial' && git switch -c hw1p5) # emulated sandbox repository
diff bare/config local/.git/config

# b.)
cd 'local'
cat <<EOF >LICENSE
Copyright © 2022 ${USER}

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
EOF

cat <<EOF >README.md
# Homework 2, Problem 2: Git Remotes

Playing around with Git remotes
EOF

git status
git add LICENSE README.md
git commit -m 'Add LICENSE and project README'
git log
git remote add origin ../bare
git push -u origin main
cd ..

# c.)
cd sandbox # this is emulated here, should be your real fork
git remote add bare ../bare
git remote -v # only one remote for this example see above ^^^
git fetch bare
git merge --allow-unrelated-histories bare/main
