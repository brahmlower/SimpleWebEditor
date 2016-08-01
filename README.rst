SimpleWebEditor
===============

This provides a simple web interface for editing files on the server it's run from. After starting the server, you can open, edit and save files via your web browser of choice. This can be useful if you would like a graphical editor on a remote server where latency makes ssh xforwarding impractical.

::

  pip install -y SimpleWebEditor
  python -m SimpleWebEditor

Running the module with no arguments will recursively list all files from the directory you ran it from. You may provide arguments to specify other directories, or even just individual files:

::

  python -m SimpleWebEditor ~/shopping_list.txt
  python -m SimpleWebEditor /etc

By default, only connections from the localhost to port 5000 are allowed. We can change this by providing the host and port value.

::

  python -m SimpleWebEditor . 127.0.0.1 8000
  python -m SimpleWebEditor . 0.0.0.0 9000
  python -m SimpleWebEditor /etc 0.0.0.0 80

Dependencies
------------
- `Flask`_
- `Bootstrap Treeview`_
- `Quill`_

.. _Flask: http://flask.pocoo.org/
.. _Bootstrap Treeview: http://jonmiles.github.io/bootstrap-treeview/
.. _Quill: http://quilljs.com/

Installation from source
------------------------

Prerequisites for the development installation are the following packages:

- pip
- nodejs

:: 

  git clone https://github.com/bplower/SimpleWebEditor.git
  cd SimpleWebEditor
  make install
  source venv/bin/activate
  python -m SimpleWebEditor
