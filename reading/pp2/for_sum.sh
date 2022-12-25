#!/bin/bash
for number in `seq 1 1 10`
do
    total=$(($total + $number))
done
echo $total
