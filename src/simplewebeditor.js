function onNodeSelect(event, node) {
    if (node.nodes) {
        // If the nodes attribute is defined, then the selected node
        // is a directory, and not a file to be displayed. In this case,
        // we do nothing and return.
        return;
    }
    current_file = node.text;
    parentNode = $('#tree').treeview('getNode', node.parentId);
    while (typeof parentNode.text == 'string') {
        current_file = parentNode.text + "/" + current_file
        parentNode = $('#tree').treeview('getNode', parentNode.parentId);
    }
    loadFile();
};

function loadTree() {
    // Some logic to retrieve, or generate tree structure
    $.getJSON(
        '/loadtree/',
        {},
        function (data) {
            var treeview_data = {
                expandIcon: 'glyphicon glyphicon-triangle-right',
                collapseIcon: 'glyphicon glyphicon-triangle-bottom',
                levels: 1,
                onNodeSelected: onNodeSelect,
                //onNodeUnselected: function (event, node) { loadFile(node.text) },
                data: data
            }
            $('#tree').treeview(treeview_data);
        }
    );
};

function saveFile() {
    // Disable the save button to prevent multiple save operations at once
    $('#save_button').prop("disabled", true);
    // Now start the save operation
    $.post(
        '/savefile/',
        {
            filename: current_file,
            data: basicEditor.getText()
        },
        function (raw_data) {
            data = JSON.parse(raw_data)
            $('#save_button').prop("disabled", false);
            $('#save_message').text(data.message);
        }
    );
};

function loadFile() {
    $.post(
        '/loadfile/',
        { filename: current_file },
        function (raw_data) {
            data = JSON.parse(raw_data)
            if (data.success) {
                basicEditor.setText(data.message);
            }
        },
        "text"
    );
};

var editorConfig = {styles: {'.ql-editor': {'font-family': "monospace"}}}
var current_file = '';
var basicEditor = new Quill('#editor', editorConfig);
basicEditor.addModule('toolbar', {container: '#toolbar'});
loadTree();