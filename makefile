build_static:
	# Make the static directories
	mkdir -p SimpleWebEditor/static/css
	mkdir -p SimpleWebEditor/static/js
	mkdir -p SimpleWebEditor/static/fonts

	# Copy to bootstrap
	cp node_modules/bootstrap3/dist/css/bootstrap.css SimpleWebEditor/static/css/.
	cp node_modules/bootstrap3/dist/js/bootstrap.js SimpleWebEditor/static/js/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff2 SimpleWebEditor/static/fonts/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff SimpleWebEditor/static/fonts/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.ttf SimpleWebEditor/static/fonts/.

	# Copy to jquery
	cp node_modules/jquery/dist/jquery.min.js SimpleWebEditor/static/js/.

	# Copy to quill
	cp node_modules/quill/dist/quill.snow.css SimpleWebEditor/static/css/.
	cp node_modules/quill/dist/quill.js SimpleWebEditor/static/js/.

	# Copy to bootstrap-treeview
	cp node_modules/bootstrap-treeview/dist/bootstrap-treeview.min.css SimpleWebEditor/static/css/.
	cp node_modules/bootstrap-treeview/dist/bootstrap-treeview.min.js SimpleWebEditor/static/js/.

	# Copy the SimpleWebEditor static files
	cp SimpleWebEditor/simplewebeditor.css SimpleWebEditor/static/css/.
	cp SimpleWebEditor/simplewebeditor.js SimpleWebEditor/static/js/.

npm_install:
	mkdir -p node_modules
	npm install

install: npm_install build_static
	pip install .

uninstall:
	pip uninstall -y SimpleWebEditor

reinstall: uninstall reinstall

clean:
	rm -rf node_modules
	rm -rf SimpleWebEditor/static
