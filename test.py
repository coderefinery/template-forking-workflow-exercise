"""
This will loop through all files *.md and check that they contain the string
'taco' (case-insensitive).
"""

from __future__ import print_function
import os
import sys

for filename in os.listdir("."):
    if filename.endswith(".md"):
        with open(filename, 'r') as f:
            recipe = f.read().lower()
            if not 'taco' in recipe:
                print("file {0} contains no string 'taco'".format(filename), file=sys.stderr)
                sys.exit(1)

print("all *.md files contain the string 'taco'")
