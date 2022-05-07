var no_accent_list = []


var accent_list = []

var wordorder = []

function generate_no_accent(word, correct){
    console.log("hello")
    if(correct=="True"){
        $('#appendnoaccent').append("<div class = 'wordlist green'>"+word+"</div>");
    }
    if(correct=="False"){
        $('#appendnoaccent').append("<div class = 'wordlist red'>"+word+"</div>");
    }

}

function generate_yes_accent(word, correct){
    console.log("hello")
    if(correct=="True"){
        $('#appendaccent').append("<div class = 'wordlist green'>"+word+"</div>");
    }
    if(correct=="False"){
        $('#appendaccent').append("<div class = 'wordlist red'>"+word+"</div>");
    }  
}


$(document).ready(function(){
    ans = "correct"
    count = 0
    $( "#next_button" ).prop('disabled', true)

    $('.wordlist').draggable(
    {
    revert: 'invalid',
    cursor: 'move',
    });

    $(".needs_accent_box").droppable({
        accept: ".wordlist",
        activeClass: "dragging_color",
        hoverClass: "over_color",

        drop: function( event, ui ) {
            count = count+1
            if(count==5){
                $( "#next_button" ).prop('disabled', false)
            }
            ui.draggable[0].style.opacity = "0.0";
            ui.draggable.draggable({disabled: true});
            let word = ui.draggable[0].getAttribute("data-word")
            let correct = ui.draggable[0].getAttribute("data-yesaccent")
            //let hi = ui.draggable[0].getAttribute("data-hi")
            console.log(word)
            console.log(correct)
            if(correct=="False"){
                ans="incorrect"
            }

            accent_list.push(word);
            
            console.log(accent_list)
            generate_yes_accent(word, correct)
        }
    });


    
    $(".no_accent_box").droppable({
        accept: ".wordlist",
        activeClass: "dragging_color",
        hoverClass: "over_color",

        drop: function( event, ui ) {
            count = count+1
            if(count==5){
                $( "#next_button" ).prop('disabled', false)
            }
            ui.draggable.draggable({disabled: true});
            ui.draggable[0].style.opacity = "0.0";

            let word = ui.draggable[0].getAttribute("data-word")
            let correct = ui.draggable[0].getAttribute("data-noaccent")
            console.log(word)
            console.log(correct)
            if(correct=="False"){
                ans="incorrect"
            }

            no_accent_list.push(word);
            generate_no_accent(word, correct)
          }
    });

    $( "#next_button" ).click(function() {
        let data_to_save = {"ans": ans}
        console.log(data_to_save)

        $.ajax({
            type: "POST",
            url: "../keepscore",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function(result){
                console.log(result)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    })
})