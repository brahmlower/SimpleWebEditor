vendor_dir = SimpleWebEditor/static/vendor
node_dir = "node_modules"

build_static:
	# Make the static directories
	mkdir -p ${vendor_dir}

	# Copy to bootstrap
	cp ${node_dir}/bootstrap3/dist/css/bootstrap.min.css ${vendor_dir}
	cp ${node_dir}/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff2 ${vendor_dir}
	cp ${node_dir}/bootstrap3/dist/fonts/glyphicons-halflings-regular.woff ${vendor_dir}
	cp ${node_dir}/bootstrap3/dist/fonts/glyphicons-halflings-regular.ttf ${vendor_dir}

	# Copy ace
	cp ${node_dir}/ace-builds/src-min/ace.js ${vendor_dir}

	# Copy to jquery
	cp ${node_dir}/jquery/dist/jquery.min.js ${vendor_dir}

	# Copy to bootstrap-treeview
	cp ${node_dir}/bootstrap-treeview/dist/bootstrap-treeview.min.css ${vendor_dir}
	cp ${node_dir}/bootstrap-treeview/dist/bootstrap-treeview.min.js ${vendor_dir}

npm_install:
	mkdir -p ${node_dir}
	npm install

install: npm_install build_static
	pip install .

uninstall:
	pip uninstall -y SimpleWebEditor

reinstall: uninstall install

clean:
	rm -rf ${node_dir}
	rm -rf ${vendor_dir}
	rm -rf SimpleWebEditor/*.pyc
