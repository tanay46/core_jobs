$(function() {
    $("#subnav-well").height($(window).height() - 180);
    $(window).resize(function(){
        $("#subnav-well").height($(window).height() - 180);
    });

    //Tagcloud functionality
    $("div.tags a").click(function() {
        $.get('/jobs/tag/', {
            q: $(this).text()
        }, function(data) {
            $(".posts:first").after(data).animate({
                height: 'toggle',
                opacity: 'toggle'
            }, "slow", function() {
                $(".posts:first").remove();
            });
        });
        return false;
    });
});