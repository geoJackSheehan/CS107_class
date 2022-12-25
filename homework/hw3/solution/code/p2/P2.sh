#!/usr/bin/env bash
# File       : P2.sh
# Description: Story bash script
# Copyright 2022 Harvard University. All Rights Reserved.

# Developer A and B change the same hunk in the file
devB_change_same_hunk='true'

# Developer A and B change a different hunk in the file
# devB_change_same_hunk='false'

part='reset' # part a.) by default
if [[ $# -gt 0 ]]; then
    part="$1"
fi

rm -rf git
mkdir git
cd git

mkdir remote devA devB
(cd remote && git init --bare)

# devA
cd devA
git init
cat <<EOF >>.git/config
[user]
    name = Developer A
    email = A@seas.harvard.edu
EOF
git remote add origin ../remote
cat <<EOF >func.py
def A(a):
    return a

def B(b):
    return b
EOF
git add func.py
git commit -m 'Initial'
sed -i 's/def A/def function/' func.py
git commit -am 'Change function name (devA)'
sed -i 's/function/CommonAncestor/' func.py
git commit -am 'Change function name again (devA)'
git push -u origin main
cd ..

# devB
cd devB
git clone ../remote .
cat <<EOF >>.git/config
[user]
    name = Developer B
    email = B@seas.harvard.edu
EOF
if [[ $devB_change_same_hunk == 'true' ]]; then
    # devB changes the same hunk as devA in file.  This will always result in a
    # merge conflict, regardless whether the history has diverged or not
    sed -i 's/CommonAncestor/devB/' func.py
else
    # devB changes a different hunk in file.  If the history is preserved (using
    # git revert), Git is smart enough to resolve this later on.  If the history
    # has diverged because of a git reset and forced push a merge conflict will
    # result anyway (in a different place in the file though).
    sed -i 's/def B/def devB/' func.py
fi
git commit -am 'Change function name (devB)'
cd .. # lunch time

if [[ $part == 'reset' ]]; then
    # a.) git reset (history diverges)
    # devA back at work (malpractice)
    cd devA
    git reset --soft HEAD^ # experiment with --soft
    git commit -m 'Changed my mind (devA)' # this commit is no longer the same! Local history has been rewritten at this point
    git reset HEAD~ # and --mixed (the default)
    # Note: "~" and "^" are not the same in general (git help rev-parse).  Here "~"
    # and "^" are the same as "~1" and "^1" which are equivalent.
    git commit -am 'Changed my mind again (devA)' # here the -a option is required (again a different commit)
    git reset --hard HEAD~2 # two commits!
    sed -i 's/def A/def devA/' func.py
    git commit -am 'Change function name (reset by devA)'
    git push --force # devastating move!  Avoid this when working with shared remotes!
    cd ..

    # devB back from lunch (happy)
    cd devB
    # git push origin main # pull first
    git pull --no-rebase # devB no longer happy
else
    # b.) git revert (history preserved)
    # devA back at work with revert
    cd devA
    git revert -n HEAD~2.. # adds a revert commit (note HEAD~2..HEAD is identical)
    # git commit -am 'Revert last two commits by A'
    # this commit is important to avoid merge conflicts
    sed -i 's/def A/def devA/' func.py
    git commit -am 'Change function name (revert by devA)'
    git push # revert is safe
    cd ..

    # devB back from lunch (happy)
    cd devB
    # git push origin main # pull first
    git pull --no-rebase # devB still happy
fi
