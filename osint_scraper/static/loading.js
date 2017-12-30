'use strict'


$(document).ready(
    $('#search').on('click', loading_page)
    )

function loading_page(){
    $(".main_page").fadeOut("slow");
    $(".body").show();
    $(".progress").fadeIn("slow");
}
