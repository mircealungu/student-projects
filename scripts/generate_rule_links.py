#!/usr/bin/env python3

import glob

for filepath in sorted(glob.iglob('writing_rules/*.md'), key=lambda x:x.split("/")[1]):
    filename = filepath.split("/")[1]
    title = filename.replace("_"," ").replace(".md","")

    print(f"[{title}]({filepath})")
