"use strict";
(function() {
    // 1. Data Width
    let getDivs = document.querySelectorAll(".skill-bar");

    getDivs.forEach(function(skillbar) {
        let data = skillbar.getAttribute("data-width");
        skillbar.style.width = data;
    });

    // 2. Data Background Image
    $("[data-bg-image]").each(function() {
        const img = $(this).data("bg-image");
        $(this).css({
            backgroundImage: `url(${img})`,
        });
    });

    // 3. Mobile Burger Menu Bar
    $(".sidebarBtn").on("click", function(e) {
        e.preventDefault();
        $(".cc--slideNav").toggleClass("show");
    });

    // 4. Mobile Menu Dropdown
    const rtMobileMenu = $(".offscreen-navigation .menu");
    if (rtMobileMenu.length) {
        rtMobileMenu.children("li").addClass("menu-item-parent");
        rtMobileMenu.find(".menu-item-has-children > a").on("click", function(e) {
            e.preventDefault();
            $(this).toggleClass("opened");
            const rtMobileSubMenu = $(this).next(".sub-menu"),
                s = $(this).closest(".menu-item-parent").find(".sub-menu");
            rtMobileMenu
                .find(".sub-menu")
                .not(s)
                .slideUp(250)
                .prev("a")
                .removeClass("opened"),
                rtMobileSubMenu.slideToggle(250);
        });
        rtMobileMenu
            .find(".menu-item:not(.menu-item-has-children) > a")
            .on("click", function(e) {
                $(".cc--slideNav").slideUp();
                $("body").removeClass("slidemenuon");
            });
    }

    // 5. On Scroll Sticky
    $(window).on("scroll", function() {
        if ($(".header").hasClass("sticky-on")) {
            var stickyPlaceHolder = $("#sticky-placeholder"),
                menu = $("#navbar-wrap"),
                menuH = menu.outerHeight(),
                topbarH = $("#topbar-wrap").outerHeight() || 0,
                targrtScroll = topbarH,
                header = $(".header");
            if ($(window).scrollTop() > targrtScroll) {
                header.addClass("sticky");
                stickyPlaceHolder.height(menuH);
            } else {
                header.removeClass("sticky");
                stickyPlaceHolder.height(0);
            }
        }
    });

    // 6. rt-slider-style-3
    $(".cc-sliderStyle1").each(function(i) {
        let ccSliderStyle1 = $(this).get(0);
        let prev = $(this).parents(".cc-slide-wrap").find(".btn-prev").get(0);
        let next = $(this).parents(".cc-slide-wrap").find(".btn-next").get(0);

        new Swiper(ccSliderStyle1, {
            slidesPerView: 1,
            loop: true,
            spaceBetween: 16,
            slideToClickedSlide: true,
            autoplay: {
                delay: 5000,
            },
            navigation: {
                nextEl: next,
                prevEl: prev,
            },
            speed: 800,
            breakpoints: {
                0: {
                    slidesPerView: 1,
                },
                575: {
                    slidesPerView: 1,
                },
                768: {
                    slidesPerView: 2,
                },
                1200: {
                    slidesPerView: 3,
                },
            },
        });
    });

    // 7. Remove Active class When Another Block Hover
    // For Feature
    $(".featureBlock").hover(function() {
        $(".featureBlock").removeClass("featureBlock--active");
        $(this).addClass("featureBlock--active");
    });
    // For Portfolio
    $(".portfolioBlock").hover(function() {
        $(".portfolioBlock").removeClass("portfolioBlock--active");
        $(this).addClass("portfolioBlock--active");
    });

    // 8. rt-slider-style-3
    $(".featureActive").each(function(i) {
        let ccSliderStyle1 = $(this).get(0);
        let prev = $(this).parents(".cc-slide-wrap2").find(".btn-prev").get(0);
        let next = $(this).parents(".cc-slide-wrap2").find(".btn-next").get(0);

        new Swiper(ccSliderStyle1, {
            slidesPerView: 1,
            loop: true,
            spaceBetween: 9,
            slideToClickedSlide: true,
            autoplay: {
                delay: 5000,
            },
            navigation: {
                nextEl: next,
                prevEl: prev,
            },
            speed: 800,
            breakpoints: {
                0: {
                    slidesPerView: 1,
                },
                575: {
                    slidesPerView: 1,
                },
                768: {
                    slidesPerView: 2,
                },
                1200: {
                    slidesPerView: 4,
                },
            },
        });
    });

    // 9. Custom Options
    $("select").niceSelect();

    // 10. Bootstrap Custom Tooltip
    $(function() {
        $('[data-bs-toggle="tooltip"]').tooltip({
            offset: [0, 5],
        });
    });

    // 11. Mouse Custom Cursor
    function itCursor() {
        var myCursor = jQuery(".mouseCursor");
        if (myCursor.length) {
            if ($("body")) {
                const e = document.querySelector(".cursor-inner"),
                    t = document.querySelector(".cursor-outer");
                let n,
                    i = 0,
                    o = !1;
                (window.onmousemove = function(s) {
                    o ||
                        (t.style.transform =
                            "translate(" + s.clientX + "px, " + s.clientY + "px)"),
                        (e.style.transform =
                            "translate(" + s.clientX + "px, " + s.clientY + "px)"),
                        (n = s.clientY),
                        (i = s.clientX);
                }),
                $("body").on("mouseenter", "button, a, .cursor-pointer", function() {
                        e.classList.add("cursor-hover"), t.classList.add("cursor-hover");
                    }),
                    $("body").on("mouseleave", "button, a, .cursor-pointer", function() {
                        ($(this).is("a", "button") &&
                            $(this).closest(".cursor-pointer").length) ||
                        (e.classList.remove("cursor-hover"),
                            t.classList.remove("cursor-hover"));
                    }),
                    (e.style.visibility = "visible"),
                    (t.style.visibility = "visible");
            }
        }
    }
    itCursor();

    // 12. Preloader
    $(window).on("load", function() {
        "use strict";
        // Page Preloader
        let preloader = $("#preloader");
        preloader &&
            $("#preloader").fadeOut("slow", function() {
                $(this).remove();
            });
    });

    // 13. Bottom To Top
    if ($(".progress-wrap").length) {
        var progressPath = document.querySelector(".progress-wrap path");
        var pathLength = progressPath.getTotalLength();
        progressPath.style.transition = progressPath.style.WebkitTransition =
            "none";
        progressPath.style.strokeDasharray = pathLength + " " + pathLength;
        progressPath.style.strokeDashoffset = pathLength;
        progressPath.getBoundingClientRect();
        progressPath.style.transition = progressPath.style.WebkitTransition =
            "stroke-dashoffset 10ms linear";
        var updateProgress = function() {
            var scroll = $(window).scrollTop();
            var height = $(document).height() - $(window).height();
            var progress = pathLength - (scroll * pathLength) / height;
            progressPath.style.strokeDashoffset = progress;
        };
        updateProgress();
        $(window).scroll(updateProgress);
        var offset = 50;
        var duration = 550;
        jQuery(window).on("scroll", function() {
            if (jQuery(this).scrollTop() > offset) {
                jQuery(".progress-wrap").addClass("active-progress");
            } else {
                jQuery(".progress-wrap").removeClass("active-progress");
            }
        });
        jQuery(".progress-wrap").on("click", function(event) {
            event.preventDefault();
            jQuery("html, body").animate({
                    scrollTop: 0,
                },
                duration
            );
            return false;
        });
    }

    // 14. Custom Search
    let target = $("#template-search");
    $('a[href="#template-search"]').on("click", function(event) {
        event.preventDefault();
        target.addClass("open");
        setTimeout(function() {
            target.find("input").focus();
        }, 700);
        return false;
    });
    $("#template-search .close").on("click", function() {
        target.removeClass("open");
    });

    // 15. Testimonial Slider Style1
    $(".testi-slider-active1").each(function(i) {
        let ccSliderStyle1 = $(this).get(0);
        let prev = $(this).parents(".cc-slide-wrap3").find(".btn-prev").get(0);
        let next = $(this).parents(".cc-slide-wrap3").find(".btn-next").get(0);

        new Swiper(ccSliderStyle1, {
            slidesPerView: 1,
            loop: true,
            spaceBetween: 9,
            slideToClickedSlide: true,
            autoplay: {
                delay: 5000,
            },
            navigation: {
                nextEl: next,
                prevEl: prev,
            },
            speed: 800,
            breakpoints: {
                0: {
                    slidesPerView: 1,
                },
                575: {
                    slidesPerView: 1,
                },
                768: {
                    slidesPerView: 1,
                },
                1200: {
                    slidesPerView: 1,
                },
            },
        });
    });

    // 16. Testimonial Slider Style2
    $(".testi-slider-active2").each(function(i) {
        let ccSliderStyle1 = $(this).get(0);
        let prev = $(this).parents(".cc-slide-wrap4").find(".btn-prev").get(0);
        let next = $(this).parents(".cc-slide-wrap4").find(".btn-next").get(0);

        new Swiper(ccSliderStyle1, {
            slidesPerView: 1,
            loop: true,
            spaceBetween: 0,
            slideToClickedSlide: true,
            autoplay: {
                delay: 5000,
            },
            pagination: {
                el: ".it-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: next,
                prevEl: prev,
            },
            speed: 800,
            breakpoints: {
                0: {
                    slidesPerView: 1,
                },
                575: {
                    slidesPerView: 1,
                },
                768: {
                    slidesPerView: 1,
                },
                1200: {
                    slidesPerView: 2,
                },
            },
        });
    });

    // 17. Input Increment Decrement Input Box
    $(document)
        .on("click", ".quantity-plus", function() {
            const $holder = $(this).parents(".number-spinner");
            const $target = $holder.find("input.quantity-input");
            let $quantity = parseInt($target.val(), 10) | 0;
            if ($.isNumeric($quantity)) {
                $quantity = $quantity + 1;
                $target.val($quantity);
            } else {
                $target.val($quantity);
            }
        })
        .on("click", ".quantity-minus", function() {
            const $holder = $(this).parents(".number-spinner");
            const $target = $holder.find("input.quantity-input");
            let $quantity = parseInt($target.val(), 10) | 0;
            if ($.isNumeric($quantity) && $quantity >= 2) {
                $quantity = $quantity - 1;
                $target.val($quantity);
            } else {
                $target.val(1);
            }
        });

    // 18. AJAX Contact Form
    const contactForm = $(".it-contact-form");
    if (contactForm.length) {
        contactForm.each(function() {
            const innerContactForm = $(this);
            innerContactForm.validator().on("submit", function(e) {
                const $this = $(this),
                    $target = innerContactForm.find(".form-response");
                if (e.isDefaultPrevented()) {
                    $target.html(
                        "<div class='alert alert-danger'><p>Please select all required field.</p></div>"
                    );
                } else {
                    $.ajax({
                        url: "php/mailer.php",
                        type: "POST",
                        data: innerContactForm.serialize(),
                        beforeSend: function() {
                            $target.html(
                                "<div class='alert alert-info'><p>Loading ...</p></div>"
                            );
                        },
                        success: function(response) {
                            if (response === "success") {
                                $this[0].reset();
                                $target.html(
                                    "<div class='alert alert-success'><p>Message has been sent successfully.</p></div>"
                                );
                            } else {
                                res = JSON.parse(response);
                                if (res.message.length) {
                                    const messages = null;
                                    res.message.forEach(function(message) {
                                        messages += "<p>" + message + "</p>";
                                    });
                                    $target.html(
                                        "<div class='alert alert-success'><p>" +
                                        messages +
                                        "</p></div>"
                                    );
                                }
                            }
                        },
                        error: function() {
                            $target.html(
                                "<div class='alert alert-success'><p>Error !!!</p></div>"
                            );
                        },
                    });
                    return false;
                }
            });
        });
    }

    // 19. Sponsor/Brand Slider Activation
    $(".sponsor-slider-active").each(function(i) {
        let ccSliderStyle1 = $(this).get(0);
        let prev = $(this).parents(".cc-slide-wrap4").find(".btn-prev").get(0);
        let next = $(this).parents(".cc-slide-wrap4").find(".btn-next").get(0);

        new Swiper(ccSliderStyle1, {
            slidesPerView: 1,
            loop: true,
            spaceBetween: 0,
            slideToClickedSlide: true,
            autoplay: {
                delay: 5000,
            },
            pagination: {
                el: ".it-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: next,
                prevEl: prev,
            },
            speed: 800,
            breakpoints: {
                0: {
                    slidesPerView: 1,
                },
                575: {
                    slidesPerView: 3,
                },
                768: {
                    slidesPerView: 5,
                },
                1200: {
                    slidesPerView: 6,
                },
            },
        });
    });

    // 20. Sponsor/Brand Slider Activation
    let wow = new WOW({
        boxClass: "wow",
        animateClass: "animate__animated ",
        offset: 0,
        mobile: false,
        live: true,
        scrollContainer: null,
    });
    wow.init();

    // End Activation
})();