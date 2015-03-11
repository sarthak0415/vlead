window.onload = function() {
    $("#files").on('change', function(evt){
        // creating FileReader
        var reader = new FileReader();

        // assigning handler
        reader.onloadend = function(evt) {      
            lines = evt.target.result.split(/[\r\n]+/g);

            lines.forEach(function (line) {
               console.log(line);
            }); 
        };

        // getting File instance
        var file = evt.target.files[0];

        // start reading
        reader.readAsText(file);
    }
}