'use strict'


console.log('hello world')

$(document).ready(
    $('#submit_button').on('click', loading_page)
    )

function loading_page(){
    $(".main_page").fadeOut("slow");
    $(".body").show();
    $(".progress").fadeIn("slow");
}
