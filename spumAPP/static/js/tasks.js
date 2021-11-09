$('document').ready(function () {
    $('.task-entry').each(function(element) {
        $(this).click(function() {
            $(this).toggleClass('done');
            const noteDone = $(this).hasClass('done');
            const noteID = $(this).attr('id');
            $.ajax({
                type: 'POST',
                url: 'http://nakolesah.ru/',
                data: { 
                    'foo': 'bar', 
                    'ca$libri': 'no$libri' // <-- the $ sign in the parameter name seems unusual, I would avoid it
                },
                success: function(msg){
                    alert('wow' + msg);
                }
            });
        });
    });
});