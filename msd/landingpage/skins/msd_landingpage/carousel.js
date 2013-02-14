(function (jq) {
    jq('.carousel').hover(
        jq('.carousel-pager-button-prev').toggle();
        jq('.carousel-pager-button-next').toggle();
    );
});

var carousel_interval;
if (jq('#carousel')) {
    var carousel_rotate = function() {
        features = jq('.carousel-banner');
        if (features.length < 2)
            return;
        jq('.carousel-banner:visible').fadeOut(300);
        jq('.carousel-button.selected').removeClass('selected');
        jq('.selected').removeClass('selected');
        next = jq('.carousel-banner:visible').next('.carousel-banner');
        if (next.length) {
            next.fadeIn(300);
            jq('#carousel-button-' + next.attr('id').substr(16)).addClass('selected');
            jq('#carousel-body-' + next.attr('id').substr(16)).addClass('selected');
        } else {
            jq('#carousel-banner-0').fadeIn(300);
            jq('.carousel-button:first').addClass('selected');
            jq('.carousel-body:first').addClass('selected');
        }
    };
    jq(function() {
        carousel_interval = setInterval(carousel_rotate, 8000);
        setTimeout(function() {
            jq('#carousel .link-https, #carousel .link-external').each( function() {
                jq(this).replaceWith(jq(this).html());
            })
        }, 1000);
        jq('#carousel').hover(
            function() { clearInterval(carousel_interval); },
            function() { carousel_interval = setInterval(carousel_rotate, 8000)
        });
    });
}
