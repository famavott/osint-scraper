'use strict'


$(document).ready(
    $('#search').on('click', loading_page)
    )

function loading_page(){
    $('.main_page').fadeOut('slow');
    $('.body').show();
    $('.progress').fadeIn('slow');
}

$('input[name=email]').keyup(function(){
    if (this.value.length > 0) {
        $('input[class="email-box"]').prop('disabled', false)
        $('input[class="all-box"]').prop('disabled', false)
    } else {
        $('input[class="email-box"]').prop('disabled', true)
        $('input[class="all-box"]').prop('disabled', true)
    }
})

$('input[name=handle]').keyup(function(){
    if (this.value.length > 0) {
        $('input[class="handle-box"]').prop('disabled', false)
        $('input[class="all-box"]').prop('disabled', false)
    } else {
        $('input[class="handle-box"]').prop('disabled', true)
        $('input[class="all-box"]').prop('disabled', false)
    }
})

$('input[name="select_all"]').change(function(){
    if(this.checked){
        $('input[name="selected_sites"]').prop('checked', true)
    } else {
        $('input[name="selected_sites"]').removeAttr('checked')
    }
})
