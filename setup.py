from setuptools import setup

setup(
    # Application name:
    name = "SimpleWebEditor",

    # Version number:
    version = "0.0.2",

    # Application author details:
    author = "Brahm Lower",
    author_email = "bplower@gmail.com",

    # License
    license = "GPL-3.0",

    # Packages:
    packages = ["SimpleWebEditor"],

    package_dir = {'SimpleWebEditor': 'src'},

    package_data = {
        "SimpleWebEditor": [
            "index.html",
            "static/js/jquery.min.js",
            "static/css/bootstrap.css",
            "static/js/bootstrap.js",
            "static/fonts/glyphicons-halflings-regular.ttf",
            "static/fonts/glyphicons-halflings-regular.woff",
            "static/fonts/glyphicons-halflings-regular.woff2",
            "static/css/bootstrap-treeview.min.css",
            "static/js/bootstrap-treeview.min.js",
            "static/css/quill.snow.css",
            "static/js/quill.js",
            "static/css/simplewebeditor.css",
            "static/js/simplewebeditor.js"
        ]
    },

    # Details:
    url = "http://github.com/bplower/SimpleWebEditor/",
    bugtrack_url = "https://github.com/bplower/SimpleWebEditor/issues",
    download_url = 'https://github.com/bplower/SimpleWebEditor/tarball/' + version,

    # Description:
    description = "A simple server allowing you to edit files in a browser.",
    long_description = open("README.md").read(),

    # Dependant packages:
    install_requires = ["flask"],

    zip_safe = False,
)
