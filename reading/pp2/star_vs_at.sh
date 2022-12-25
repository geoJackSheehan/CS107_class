#!/bin/bash
echo "----0"
for i in $@; do echo "\$i=["$i"]"; done
echo "----1"
for i in $*; do echo "\$i=["$i"]"; done
echo "----2"

for i in "$@"; do echo "\$i=["$i"]"; done
echo "----3"
for i in "$*"; do echo "\$i=["$i"]"; done
echo "----4"
