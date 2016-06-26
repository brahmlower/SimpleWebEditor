# SimpleWebEditor

This provides a simple web interface for editing files on the server it's run from. After starting the server, you can open, edit and save files via your web browser of choice. This can be useful if you would like a graphical editor on a remote server where latency makes ssh xforwarding impractical.
```
pip install -y SimpleWebEditor
python -m SimpleWebEditor
```
Running the module with no arguments will recursively list all files from the directory you ran it from. You may provide arguments to specify other directories, or even just individual files:
```
python -m SimpleWebEditor ~/shopping_list.txt
python -m SimpleWebEditor /etc
```
## Dependencies
### Backend
* Flask http://flask.pocoo.org/

### Frontend
* Bootstrap Treeview http://jonmiles.github.io/bootstrap-treeview/
* Quill http://quilljs.com/

## Installation from source
Prerequisites for the development installation are the following packages:
* pip
* nodejs (make sure 'node' points to 'nodejs' or running <code>npm install</code> will fail)

```
git clone https://github.com/bplower/SimpleWebEditor.git
cd SimpleWebEditor
virtualenv venv
source venv/bin/activate
npm install
./prepare-static.sh
python setup.py install
python -m SimpleWebEditor
```
