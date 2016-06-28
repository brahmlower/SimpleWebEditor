import os
import sys
from SimpleWebEditor import SimpleWebEditor

# Handle the provided options/arguments
filename = "."
if len(sys.argv) > 1:
    filename = sys.argv[1]

# Translate user paths and convert it to an absolute path
filename = os.path.abspath(os.path.expanduser(filename))

swe = SimpleWebEditor(filename, __name__)
swe.run()
