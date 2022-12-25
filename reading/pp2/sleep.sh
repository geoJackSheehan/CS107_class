#!/bin/bash
function f() {
    date
    sleep "$1"
    echo "$1"
    date
}
while [ -n "$1" ]
do
    f "$1" &
    shift
done
wait
