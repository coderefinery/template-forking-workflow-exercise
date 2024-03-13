import glob
from pathlib import Path
import re
import sys

ingredients_re = re.compile('^#.*ingredients',  re.IGNORECASE|re.MULTILINE)
instructions_re = re.compile('^#.*instructions',  re.IGNORECASE|re.MULTILINE)

base = Path('.')
print(f"Checking recipes in {str(base.absolute())}:")

errors = 0
for path in base.glob('*/*.md'):
    if not ingredients_re.search(path.read_text()):
        print(f'::error file={str(path)},title=Ingredients missing::File is missing an ingredients section: "# Ingredients"')
        errors += 1
    if not instructions_re.search(path.read_text()):
        print(f'::error file={str(path)},title=Instructions missing::File is missing an instructions section: "# Instructions"')
        errors += 1
print(f"{errors} errors")
if errors:
    sys.exit(1)
