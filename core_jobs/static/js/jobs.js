$(function(){
    $("div.tags a").click(function(){
        $.get(
            '/jobs/tag/',
            {q: $(this).text()},
            function(data) {
                $(data).insertAfter(".posts:first")
                $(".posts:first").animate({ height: 'toggle', opacity: 'toggle' }, "slow", function(){
                    $(".posts:first").remove();
                });
            }
        );
    });
});