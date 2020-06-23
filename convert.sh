#!/bin/bash
set -x
echo "converting dot files"
for x in `ls ./`; do
  dot -Tpng -o$x.png $x
done
