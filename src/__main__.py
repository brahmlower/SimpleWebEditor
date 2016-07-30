import os
import sys
from SimpleWebEditor import SimpleWebEditor

# Handle the provided options/arguments
filename = "."
flask_host = '127.0.0.1'
flask_port = 5000
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    flask_host = sys.argv[2]
if len(sys.argv) > 3:
    flask_port = sys.argv[3]

# Translate user paths and convert it to an absolute path
filename = os.path.abspath(os.path.expanduser(filename))

swe = SimpleWebEditor(filename, __name__)
swe.run(host = flask_host, port = flask_port)
