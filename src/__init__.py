import sys
import os
import json
import flask

class SimpleWebEditor(flask.Flask):
    def __init__(self, filepath, *args, **kwargs):
        super(SimpleWebEditor, self).__init__(*args, **kwargs)
        self.package_root = self.get_package_root()
        self.register_routes()
        self.path_is_dir = None
        self.file_tree_root = None
        self.sanitize_filepath(filepath)
        self.file_tree = self.build_file_tree(filepath)

    def register_routes(self):
        # Now register the routes
        self.route("/")(self.index)
        self.route("/loadtree/")(self.loadtree)
        self.route("/loadfile/", methods=['POST'])(self.loadfile)
        self.route("/savefile/", methods=['POST'])(self.savefile)

    def sanitize_filepath(self, filepath):
        if not os.path.exists(filepath):
            raise ValueError
        self.path_is_dir = os.path.isdir(filepath)
        if self.path_is_dir:
            self.file_tree_root = filepath + "/"
        else:
            self.file_tree_root = "/".join(filepath.split("/")[:-1]) + "/"

    def get_package_root(self):
        return "/".join(sys.modules[__name__].__file__.split("/")[:-1]) + "/"

    def build_file_tree(self, file_path):
        if not self.path_is_dir:
            file_name = file_path.split("/")[-1]
            return convert_tree({file_name: None})

        raw_tree_dict = get_dir_tree(file_path)
        raw_tree_dict_root_key = file_path.split("/")[-1]
        raw_tree_dict = raw_tree_dict[raw_tree_dict_root_key]
        return convert_tree(raw_tree_dict)

    def index(self):
        """
        Serve the main page for editing everything
        """
        return open(self.package_root + 'index.html', 'r').read()

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
        file_data = flask.request.form['data'][:-1]
        status_dict = {}
        try:
            open(file_path, 'w').write(file_data)
            status_dict['success'] = True
            status_dict['message'] = 'Success'
        except Exception as e:
            status_dict['success'] = False
            status_dict['message'] = str(e)
        return json.dumps(status_dict)

def get_dir_tree(rootdir):
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