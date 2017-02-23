build_static:
	# Make the static directories
	mkdir -p SimpleWebEditor/static/vendor

	# Copy to bootstrap
	cp node_modules/bootstrap3/dist/css/bootstrap.css SimpleWebEditor/static/vendor/.
	cp node_modules/bootstrap3/dist/js/bootstrap.js SimpleWebEditor/static/vendor/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff2 SimpleWebEditor/static/vendor/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff SimpleWebEditor/static/vendor/.
	cp node_modules/bootstrap3/dist/fonts/glyphicons-halflings-regular.ttf SimpleWebEditor/static/vendor/.

	# Copy to jquery
	cp node_modules/jquery/dist/jquery.min.js SimpleWebEditor/static/vendor/.

	# Copy to quill
	cp node_modules/quill/dist/quill.snow.css SimpleWebEditor/static/vendor/.
	cp node_modules/quill/dist/quill.js SimpleWebEditor/static/vendor/.

	# Copy to bootstrap-treeview
	cp node_modules/bootstrap-treeview/dist/bootstrap-treeview.min.css SimpleWebEditor/static/vendor/.
	cp node_modules/bootstrap-treeview/dist/bootstrap-treeview.min.js SimpleWebEditor/static/vendor/.

npm_install:
	mkdir -p node_modules
	npm install

install: npm_install build_static
	pip install .

uninstall:
	pip uninstall -y SimpleWebEditor

reinstall: uninstall install

clean:
	rm -rf node_modules
	rm -rf SimpleWebEditor/*.pyc
	rm -rf SimpleWebEditor/static/vendor
