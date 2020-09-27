#!/usr/bin/env python3

import glob

def generate_rule_links():
	for filepath in sorted(glob.iglob('writing_rules/*.md'), key=lambda x:x.split("/")[1]):
	    filename = filepath.split("/")[1]
	    title = filename.replace("_"," ").replace(".md","")

	    print(f"* [{title}]({filepath})")


preamble = True
after_the_rules = False

with open('writing-advice.md') as f:
	
	for l in f.read().splitlines():

		is_rule_line = l.strip().startswith("*")

		if is_rule_line:
			if preamble:
				preamble = False
				generate_rule_links()
				after_the_rules = True

			continue


		print(l)


