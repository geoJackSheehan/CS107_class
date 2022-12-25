#!/usr/bin/env bash
# File       : exercise_1.sh
# Description: Scripted version of the steps in exercise 1
# Copyright 2022 Harvard University. All Rights Reserved.
markup()
{
    # wrapper function to highlight commands
    echo -e "\033[0;33m###### ${*}\033[0m"
    ${*}
}

dst='exercise_1'
rm -rf ${dst}
mkdir -p ${dst}
cd ${dst}
git init
git branch -M main
cat <<EOF >README.md
# CS107 / AC207 Private Class Repository

Fall 2022
EOF
git add README.md
git commit -m 'Initial commit'

markup git switch main
markup git switch -c feature_branch
markup git branch
markup git status
cat <<'EOF' >>README.md

# Content

* `homework`: My homework directory
* `lab`:      Pair-programming sessions
* `lecture`:  Lecture slides and supplementary lecture material
EOF
markup git status
echo -e "\033[0;33m###### git commit -am 'Add Content subsection to README'\033[0m"
git commit -am 'Add Content subsection to README'

markup git switch main
markup git diff HEAD..feature_branch
markup git merge feature_branch
markup git status
markup git diff HEAD~..
markup git branch -d feature_branch
echo -e "\033[0;33mOmit git push\033[0m"
echo -e "\033[0;33mREMOVE THE AUTOMATICALLY CREATED '${dst}' DIRECTORY AGAIN WHEN DONE.\033[0m"
