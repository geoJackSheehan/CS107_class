#!/usr/bin/env bash
test -e a.sh; echo $?
test -r a.sh; echo $?
test -w a.sh; echo $?
test -x a.sh; echo $?
