import os
import sys
import json
import flask
from flask import current_app
from docopt import docopt

__version__ = "0.0.7"

class SimpleWebEditorServer(flask.Flask):
    def __init__(self, filepath, *args, **kwargs):
        super(SimpleWebEditorServer, self).__init__(*args, **kwargs)
        self.path_is_dir = None
        self.file_tree_root = self.get_file_tree_root(filepath)
        self.file_tree = self.build_file_tree(filepath)

        # Now register the routes
        self.route("/")(self.index)
        self.route("/loadtree/")(self.loadtree)
        self.route("/loadfile/", methods=['POST'])(self.loadfile)
        self.route("/savefile/", methods=['POST'])(self.savefile)

    def get_file_tree_root(self, filepath):
        if not os.path.exists(filepath):
            raise ValueError
        self.path_is_dir = os.path.isdir(filepath)
        if self.path_is_dir:
            return filepath + "/"
        else:
            return "/".join(filepath.split("/")[:-1]) + "/"

    def build_file_tree(self, file_path):
        raw_tree_dict = {}
        if not self.path_is_dir:
            file_name = file_path.split("/")[-1]
            raw_tree_dict[file_name] = None
        else:
            temp_tree_dict = get_dir_tree(file_path)
            raw_tree_dict_root_key = file_path.split("/")[-1]
            raw_tree_dict = temp_tree_dict[raw_tree_dict_root_key]
        return convert_tree(raw_tree_dict)

    def index(self):
        """
        Serve the main page for editing everything
        """
        return current_app.send_static_file('index.html')

    def loadtree(self):
        """
        Retrieves the directory tree structure
        """
        return json.dumps(self.file_tree)

    def loadfile(self):
        """
        Loads data from the requested file.
        """
        file_path = self.file_tree_root + flask.request.form['filename']
        status_dict = {}
        if not os.path.isfile(file_path):
            status_dict['success'] = False
            status_dict['message'] = "Specified path '%s' is not a file." % flask.request.form['filename']
            print status_dict['message']
        else:
            status_dict['success'] = True
            status_dict['message'] = open(file_path, 'r').read()
        return json.dumps(status_dict)

    def savefile(self):
        """
        This saves the data to the specified file.
        """
        file_path = self.file_tree_root + flask.request.form['filename']
        file_data = flask.request.form['data']
        status_dict = {}
        try:
            open(file_path, 'w').write(file_data)
            status_dict['success'] = True
            status_dict['message'] = 'Success'
        except Exception as error:
            status_dict['success'] = False
            status_dict['message'] = str(error)
        return json.dumps(status_dict)

def get_dir_tree(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir_tree = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir_tree)
        parent[folders[-1]] = subdir
    return dir_tree

def convert_tree(treedict):
    dirs = []
    files = []
    for i in treedict:
        if not treedict[i]:
            # This is a file
            files.append({'text': i})
        else:
            # This is a directory
            dirs.append({'text': i, 'nodes': convert_tree(treedict[i])})
    return dirs + files

def main(raw_input_list):
    """simplewebeditor

    Usage:
        simplewebeditor [options] [<file>]

    Options:
        -h, --help          Displays this message
        -H, --host <host>   The address to serve on [default: 127.0.0.1]
        -p, --port <port>   The port to serve on [default: 5000]
    """
    # Handle the provided arguments
    arguments = docopt(main.__doc__, argv=raw_input_list)
    if arguments["<file>"] is None:
        arguments["<file>"] = "."

    # Translate user paths and convert it to an absolute path
    filename = os.path.abspath(os.path.expanduser(arguments['<file>']))

    server = SimpleWebEditorServer(filename, __name__)
    server.run(host=arguments['--host'], port=arguments['--port'])
