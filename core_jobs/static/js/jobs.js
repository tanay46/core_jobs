$(function() {
    $("#subnav-well").height($(window).height() - 180);
    $(window).resize(function(){
        $("#subnav-well").height($(window).height() - 180);
    });

    //Tagcloud functionality
    $("div.tags a").click(function(event) {
        var $tagButton = $(this);
        if (!$tagButton.attr("disabled")) {
            $tagButton.attr("disabled", true);
            $.get('/jobs/tag/', {
                q: $(this).text()
            }, function(data) {
                $(".posts:first").after(data).animate({
                    height: 'toggle',
                    opacity: 'toggle'
                }, "slow", function() {
                    $(".posts:first").remove();
                    $tagButton.attr("disabled", false);
                });
            });
            return false;
        }});
});