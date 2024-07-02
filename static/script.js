// Assuming jQuery is available
$(function () {
    $('.datepicker').datepicker({
        format: 'dd-mm-yyyy',
        autoclose: true,
        todayHighlight: true
    });

    $('input[name="query"]').on('keypress', function (e) {
        if (e.which === 13) {
            $(this).closest('form').submit();
        }
    });

    $('.toggle-theme').on('click', function() {
        $('body').toggleClass('dark-mode');
        $(this).toggleClass('dark-mode');
    });
});
