import sys
import SimpleWebEditor

# Handle the provided options/arguments
filename = "."
if len(sys.argv) > 1:
    filename = sys.argv[1]

# Generate and set the filetree
treedict = SimpleWebEditor.get_directory_structure(filename)
SimpleWebEditor.filetree = SimpleWebEditor.convert_tree(treedict["."])
SimpleWebEditor.app.run()