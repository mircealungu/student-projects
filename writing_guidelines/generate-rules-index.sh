#!/bin/bash

python3 scripts/generate_writing_advice.py > README.tmp
cp README.tmp README.md
rm -f README.tmp

echo "*** Contents of writing-advice.md is now: "
cat README.md