venv: venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv venv
	touch venv/bin/activate

build_static:
	# Make the static directories
	mkdir -p src/static/{css,js,fonts}

	# Copy to bootstrap
	cp node_modules/bootstrap3/dist/css/bootstrap.css src/static/css/.
	cp node_modules/bootstrap3/dist/js/bootstrap.js src/static/js/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff2 src/static/fonts/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff src/static/fonts/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.ttf src/static/fonts/.

	# Copy to jquery
	cp node_modules/jquery/dist/jquery.min.js src/static/js/.

	# Copy to quill
	cp node_modules/quill/dist/quill.snow.css src/static/css/.
	cp node_modules/quill/dist/quill.js src/static/js/.

	# Copy to bootstrap-treeview
	cp node_modules/bootstrap-treeview/dist/bootstrap-treeview.min.css src/static/css/.
	cp node_modules/bootstrap-treeview/dist/bootstrap-treeview.min.js src/static/js/.

	# Copy the SimpleWebEditor static files
	cp src/simplewebeditor.css src/static/css/.
	cp src/simplewebeditor.js src/static/js/.

npm_install:
	test -d node_modules || mkdir node_modules
	npm install

install: npm_install build_static venv
	venv/bin/python setup.py install

clean:
	rm -r build
	rm -r node_modules
	rm -r venv
	rm -r SimpleWebEditor.egg-info

clean_all: clean
	rm -r dist