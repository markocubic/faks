jQuery($ => {
    $('#user').hover(function() {
        $(this).children('img').prop('src', function() {
            return $(this).data('over');
        });
    }, function() {
        $(this).children('img').prop('src', function() {
            return $(this).data('leave');
        });
    });
});