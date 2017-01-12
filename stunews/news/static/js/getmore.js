$(document).ready(function(){
    $.ajax({
            url: 'http://119.29.133.102:9999/scutnews/getnews/',
            // url: 'http://127.0.0.1:8000/scutnews/getnews/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({"page": 1}),
            success:function(data) {
                console.log(data);
            }
        });

});