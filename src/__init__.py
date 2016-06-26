import sys
import os
import json
from flask import Flask
from flask import request

app = Flask(__name__)
filetree = []

@app.route("/")
def index():
    """
    Serve the main page for editing everything
    """
    pkg_path = "/".join(sys.modules[__name__].__file__.split("/")[:-1]) + "/"
    return open(pkg_path + 'index.html', 'r').read()

@app.route("/loadtree/")
def loadtree():
    """
    Retrieves the directory tree structure
    """
    return json.dumps(filetree)

@app.route("/loadfile/", methods=['POST'])
def loadfile():
    """
    Loads data from the requested file. This will currently only work for
    files in the same directory.
    """
    return open(request.form['filename'], 'r').read()

@app.route("/savefile/", methods=['POST'])
def savefile():
    """
    This saves the data to the specified file.
    """
    filename = request.form['filename']
    data = request.form['data'][:-1]
    open(filename, 'w').write(data)
    return "{'status': 'success'}"

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir

def convert_tree(treedict):
    dirs = []
    files = []
    for i in treedict:
        if not treedict[i]:
            # This is a file
            files.append({
                'text': i
            })
        else:
            # This is a directory
            dirs.append({
                'text': i,
                'nodes': convert_tree(treedict[i])
            })
    return dirs + files

# if __name__ == "__main__":
#     filename = "."
#     if len(sys.argv) > 1:
#         filename = sys.argv[1]
#     treedict = get_directory_structure(filename)
#     filetree = convert_tree(treedict["."])
#     app.run()
