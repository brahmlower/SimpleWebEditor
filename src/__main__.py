import sys
import SimpleWebEditor

# Handle the provided options/arguments
filename = "."
if len(sys.argv) > 1:
    filename = sys.argv[1]

# Generate and set the filetree
treedict = SimpleWebEditor.get_directory_structure(filename)
# An individual file results in a treedict equal to an empty dictionary
if treedict != {}:
	try:
		SimpleWebEditor.filetree = SimpleWebEditor.convert_tree(treedict[filename])
	except KeyError:
		# the root key is the last directory name in the whole path. We need
		# to replace the key to make loading the file work properly
		treedict[filename] = treedict[filename.split("/")[-1]]
		del treedict[filename.split("/")[-1]]
		SimpleWebEditor.filetree = SimpleWebEditor.convert_tree(treedict[filename])
else:
	SimpleWebEditor.filetree = SimpleWebEditor.convert_tree({filename: None})
SimpleWebEditor.app.run()
