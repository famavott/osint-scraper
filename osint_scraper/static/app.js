'use strict'

$(document).ready(
    $('#search').on('click', loading_page)
    )

function loading_page(){
    $('.main_page').fadeOut('slow');
    $('.body').show();
    $('.progress').fadeIn('slow');
}

$('input[name="select_all"]').change(function(){
    if(this.checked){
        $('input[name="selected_sites"]').prop('checked', true)
    } else {
        $('input[name="selected_sites"]').removeAttr('checked')
    }
})

$('.form-control').keyup(function() {
    if ($('input[class="inputHandle"]').val() == '' || $('input[class="inputEmail"]').val() == '' ) {
        $('.form-btn').prop('disabled', true)
    } else {
        $('.form-btn').prop('disabled', false)
        $('.all-box').prop('disabled', false)
    }
});
