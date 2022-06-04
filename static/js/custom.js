$(document).ready(function() {
    $('input[type=radio][name=language]').change(function() {
        $(".language-form").submit();
    });

    // function showAnim() {

    // }

    // $(".anim").fontSpy({
    //     onLoad: 'showAnim',
    // });
    // $(".anim").addClass("animated");

    // fontSpy('SolaimanLipi', {
    //     // glyphs: '\ue81a\ue82d\ue823',
    //     success: function() {
    //         console.log('loaded');
    //         $('html[lang="bn"] body').css("font-family", "'SolaimanLipi', sans-serif");
    //     },
    //     failure: function() {
    //       //alert("My Icons failed to load");
    //     }
    // });

    var scrolled = false;
    $(window).on('scroll', function() {
        if (!scrolled) {
            scrolled = true;
            // new WOW().init();
            new WOW(
                {
                    boxClass:     'wow',      // default
                    animateClass: 'animated', // default
                    offset:       0,          // default
                    mobile:       false,
                    live:         true        // default
                }
            ).init();
        }
    });

    // $("[data-ani-delay]").css("animation-delay", $(this).data("ani-delay"));
    $("[data-ani-delay]").each(function(){
        $(this).css("animation-delay", $(this).data("ani-delay"));
        console.log($(this).data("ani-delay"));
    });
    $("[data-ani-duration]").each(function(){
        $(this).css("animation-duration", $(this).data("ani-duration"));
        console.log($(this).data("ani-duration"));
    });

    // get browser width
    var windowWidth = $(window).innerWidth();
    $(window).resize(function(){
        windowWidth = $(window).innerWidth();
    });
    // console.log(windowWidth);

    if (windowWidth >= 991){
        $('ul.primary-nav li.dropdown').hover(function() {
            $(this).find('.dropdown-menu').stop(true, true).delay(100).slideDown(200);
        }, function() {
            $(this).find('.dropdown-menu').stop(true, true).delay(100).slideUp(200);
        });
    }


    if($('a[data-rel=lightcase]').length) {
        $('a[data-rel=lightcase]').lightcase();
    }

    if($('.tut-link').length) {
        $('.tut-link').on('click', function(e){
            e.preventDefault();
            $('.tut-link').removeClass('active');
            $(this).addClass('active');
            $('#embed iframe').attr('src', $(this).data('src'));
            console.log($(this).data('src'));
            if (windowWidth <= 1024){
                $('html, body').animate({
                    scrollTop: $("#embed").offset().top
                });
            }
        });
    }

});
