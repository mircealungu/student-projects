#!/usr/bin/env python3

import glob

def generate_rule_links():
	for filepath in sorted(glob.iglob('./*.md'), key=lambda x:x.split("/")[1]):		
		if "README.md" in filepath:
			continue
			
		filename = filepath.split("/")[1]
		title = filename.replace("_"," ").replace(".md","")
		filepath = filepath[2:]

		print(f"https://github.com/mircealungu/student-projects/blob/master/writing_guidelines/{filepath}")



generate_rule_links()