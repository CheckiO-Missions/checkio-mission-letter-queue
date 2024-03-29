requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            animation: function($expl, data){
                var checkioInput = data.in[0];
                if (!checkioInput) return;

                var queue = [];
                var $table = $expl.find("table");
                for (var i = 0; i < checkioInput.length; i++) {
                    var $tr = $("<tr></tr>");
                    var c = checkioInput[i];
                    if (c.lastIndexOf("PUSH", 0) === 0) {
                        var ch = c.split(" ")[1];
                        queue.push(ch);
                    }
                    else if (queue.length > 0) {
                        queue.shift();
                    }
                    $tr.append($("<td></td>").text(c));
                    $tr.append($("<td></td>").text(queue.join("")));
                    $table.append($tr);
                }
            },
        });
        io.start();
    }
);
