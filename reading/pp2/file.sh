#!/bin/bash

if [ -x $1 ] ; then
 echo wc -l $1
 echo $(wc -l $1)
else
 echo "nope"
fi
