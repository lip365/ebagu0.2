$(function(){
	$(document).on('click', 'a.favIt', function(e){
        e.preventDefault();
		var itemId = $(this).attr('id').split("_")[1],
            csrf = $('[name=csrfmiddlewaretoken]').val();
        if (!csrf) console.log("You must add {% csrftoken %} somewhere in the template.");
        $.ajax({
            type: "POST",
            url: $(this).attr("data-action-url"),
            data: {'csrfmiddlewaretoken': csrf},
            dataType: "json",
            timeout: 2000,
            cache: false,
            beforeSend: function(XMLHttpRequest) {
                //$("#loader").fadeIn();
            },
            error: function(data, XMLHttpRequest, textStatus, errorThrown){
                $(this).html("Error connecting to the server.");
            },
            complete: function(XMLHttpRequest, textStatus) {
                //$("#loader").fadeOut();
            },
            success: function(data, textStatus, XMLHttpRequest){
                $('#FavIt_'+itemId).html(data.message);
                $('#FavCounter_'+itemId).html(data.counter);
            }
        });
	});
});
