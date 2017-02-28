SimpleWebEditor
===============

This provides a simple web interface for editing files on the server it's run from. After starting the server, you can open, edit and save files via your web browser of choice. This can be useful if you would like a graphical editor on a remote server where latency makes ssh xforwarding impractical.

Installing the package will provide the script 'simplewebeditor' which simply wraps the libraries main function

::

  $ simplewebeditor
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

You can also run the web editor by invoking the module via python

::

  $ python -m SimpleWebEditor
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Or you can call the modules main function from within the python interpreter

::

  $ python
  >>> import SimpleWebEditor
  >>> SimpleWebEditor.main([])
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Running the module with no arguments will recursively list all files from the directory you ran it from. You may provide arguments to specify other directories

::

  $ simplewebeditor /etc

or even just individual files

::

  $ simplewebeditor ~/shopping_list.txt

By default, only connections from localhost at port 5000 are allowed. This functionality can be changed by providing the port or host options:

Hosting my user directory locally at port 1234:

::

  $ simplewebeditor --port 1234 ~/
   * Running on http://127.0.0.1:1234/ (Press CTRL+C to quit)

Hosting /etc/passwd at 0.0.0.0:

::

  $ simplewebeditor --host 0.0.0.0 /etc/passwd
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Dependencies
------------
- `Flask`_
- `Docopt`_
- `jQuery`_
- `Bootstrap`_
- `Bootstrap Treeview`_
- `Ace`_

.. _Flask: http://flask.pocoo.org/
.. _Docopt: http://docopt.org/
.. _jQuery: https://jquery.com/
.. _Bootstrap: http://getbootstrap.com/
.. _Bootstrap Treeview: http://jonmiles.github.io/bootstrap-treeview/
.. _Ace: https://ace.c9.io/

Installation
------------

SimpleWebEditor is available on pypa:

::

  $ pip install -y SimpleWebEditor

Installation from source
------------------------

Prerequisites for the development installation are the following packages:

- pip
- nodejs

:: 

  $ git clone https://github.com/bplower/SimpleWebEditor.git
  $ cd SimpleWebEditor
  $ virtualenv venv
  $ source venv/bin/activate
  $ make install
