#!/usr/bin/env bash
# File       : P5.sh
# Description: Replay Git journey in homework 1 (you need access to
#              https://code.harvard.edu/CS107)
# Copyright 2022 Harvard University. All Rights Reserved.

# Note that there are no SSH keys configured in the class Docker container for
# security reasons.  You could play this file through on your host instead (e.g.
# WSL).

rm -rf git
mkdir git
cd git

# a.)
# Using the SSH link which assumes you have installed your SSH key in your
# profile.  Ideally, you should prefer the SSH protocol whenever possible.
git clone git@code.harvard.edu:CS107/sandbox.git

# Note: you will not have sufficient permissions to contribute to this sandbox
# repository.  You can still contribute by creating a fork and then a pull
# request to merge your contribution into the upstream repository you do not
# have permission to push directly.  Hence, your pull request will first undergo
# a review by one of the developers for the upstream repository.  The developer
# might request changes from you before the pull request is merged, all these
# changes will happen in your open pull request.  For your homework, the
# teaching staff is in the role of the reviewer and you are the contributor.
# This is a typical workflow on platforms like Github or Gitlab.
#
# Instead you will create a fork in your profile on code.harvard.edu where you
# do have the necessary right for pushing work.

################################################################################
## NOTE: in the homework you are asked to perform the following steps to finish
## part a.):
#rm -rf sandbox # remove the CS107/sandbox clone

## Clone your fork (note that you must replace faw093 with your own NetID for
## this to work)
#git clone git@code.harvard.edu:faw093/sandbox.git

## Because there are already commits pushed on these forks, we will just use the
## CS107/sandbox repository here without pushing to it.
################################################################################

# b.)

# i.)
cd sandbox
git branch -a
git switch test
git diff master..HEAD

# ii.)
git switch master
git branch hw1p5
git switch hw1p5
git switch -c hw1p5_tmp

# iii.)
cd homework/hw1/sandbox
echo 'Jane Smith' >>README.md
git status
git add README.md # add the changes to the index (a.k.a staging changes)
git commit # -m 'Adding Jane Smith to README.md'  # not adding -m option will open GIT_EDITOR
git status # check again
# see `git help add` to read more about the --patch option for staging changes.

# iv.)  (we will not do these steps because we are not working on a fresh fork!)
#git push  # will fail
#git push origin hw1p5_tmp  # will work on your fork (will not work here because we use the CS107/sandbox clone)
##git push -u origin hw1p5_tmp  # add the -u/--set-upstream option to let Git remember the association between origin and hw1p5_tmp
git branch -vv

# v.) merge conflict
git switch hw1p5
git diff hw1p5_tmp..
echo 'John Doe' >>README.md
git commit -am 'Adding John Doe to README.md'  # -a: add; -m: commit message
git merge hw1p5_tmp  # this command will cause a conflict in the README.md file
git status
vim README.md # resolve the conflict manually using vim (any text editor can do)
git add README.md  # stage the conflict resolution
git commit  # commit (Git will automatically enter a merge commit message, you can accept it or further modify)
git branch -d hw1p5_tmp
#git push origin --delete hw1p5_tmp # we are not doing this because we have not pushed in iv.) above (the branch does not exist on the remote)!

# vi.) revert a commit
echo 'One more addition to README.md' >>README.md
git commit -am 'One more change to README.md (to be reverted)'
#git push -u origin hw1p5  # again, we omit this step here (you should do it in the HW)

# The push above inserts the commit in the remote history.  If it is shared with
# other developers, the only way to undo it is to use git revert (will see more
# about this in next HW).
git log --oneline  # to inspect history
git revert HEAD  # just use the HEAD pointer for simplicity in this case (since the revert is trivial)
git log --oneline  # reversion commit added on top

# c.) adding additional remotes
# We will not do this step here.  You can always add more remotes that point to
# different servers (e.g. one on github.com, one on code.harvard.edu yeat
# another on gitlab.com for example) this is very common.  For the forked
# repository in the homework, it makes sense to add the upstream repository (the
# one at CS107/sandbox for which you can only pull) because this will be your
# target for the pull request.  You can add new remotes with `git remote add
# <local name> <URL>`.  We are not doing this here.  There is only one remote in
# this reply scenario (i.e. CS107/sandbox):
git remote -v
