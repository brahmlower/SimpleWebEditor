function onNodeSelect(event, node) {
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
    $.post(
        '/savefile/',
        {
            filename: current_file,
            data: basicEditor.getText()
        },
        function (data) { console.log(data) }
    );
};

function loadFile() {
    $.post(
        '/loadfile/',
        { filename: current_file },
        function (data) { basicEditor.setText(data) },
        "text"
    );
};

var editorConfig = {styles: {'.ql-editor': {'font-family': "monospace"}}}
var current_file = '';
var basicEditor = new Quill('#editor', editorConfig);
basicEditor.addModule('toolbar', {container: '#toolbar'});
loadTree();