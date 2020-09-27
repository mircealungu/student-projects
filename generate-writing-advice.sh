#!/bin/bash

python3 scripts/generate_writing_advice.py > writing-advice.tmp
cp writing-advice.tmp writing-advice.md
rm -f writing-advice.tmp

echo "*** Contents of writing-advice.md is now: "
cat writing-advice.md