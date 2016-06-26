# SimpleWebEditor

This project is still underdevelopment. Some descriptions here will represent the project in its final state.

This provides a simple web interface for editing specified local files. After installing and starting the service, can open, edit and save files via your web browser of choice.
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

## Development installation
Prerequisites for the development installation are the following packages:
* pip
* nodejs (make sure 'node' points to 'nodejs' or running <code>npm install</code> will fail)

```
git clone https://github.com/bplower/SimpleWebEditor.git
cd SimpleWebEditor
pip install -r requirements.txt
npm install
./prepare-static.sh
python main.py
```