/*=============================================================
Template Name: Hotel Himara - Hotel HTML Template
Author:        Eagle-Themes (Jomin Muskaj)
Author URI:    http://eagle-themes.com
Version:       1.1.0
=============================================================*/

(function($) {
  "use strict";

  // =============================================
  // LOADER
  // =============================================
  $(window).on('load', function() {
    $(".loader").fadeOut(500);
  });

  /*Document is Ready */
  $(document).ready(function() {

    // =============================================
    // HEADER
    // =============================================
    $(window).on("scroll", function() {
      var header = $('header');
      var topmenu = $('.topbar');
      var windowheight = $(this).scrollTop();
      var menuheight = header.outerHeight();
      var firstlogo = $('.first-logo');
      var secondlogo = $('.second-logo');
      var topmenuheight = 0;

      if (topmenu.length) {
        var topmenuheight = topmenu.outerHeight();
      }
      var fixedheight = topmenuheight;
      if (header.length) {
        if ((windowheight > fixedheight) && header.hasClass("sticky-header")) {
          header.addClass('header-fixed-top').delay(200);
          if (!header.hasClass("transparent-header")) {
            header.next("*").css("margin-top", menuheight);
          }
          if (header.hasClass("sticky-header")) {
            header.addClass("scroll-header");
          }
          // CHANGE LOGO ON SCROLL
          firstlogo.css("display", "none");
          secondlogo.css("display", "block");

        } else {
          header.removeClass("header-fixed-top");
          if (!header.hasClass("transparent-header")) {
            header.next("*").css("margin-top", "0");
          }
          if (header.hasClass("sticky-header")) {
            header.removeClass("scroll-header");
          }
          // CHANGE LOGO ON REVERSE SCROLL
          if (!header.hasClass('mobile-header')) {
            firstlogo.css("display", "block");
            secondlogo.css("display", "none");
          }
        }
      }
    });

    // =============================================
    // MENU
    // =============================================
    function mmenuInit() {
      var screenwidth = $(window).width();
      var header = $('header');
      var main_menu = $('#main-menu');
      var mobile_menu = $('#mobile-menu');
      var menu_toggler = $("#toggle-menu-button");
      var menubreakpoint = $('header').data("menutoggle");
      var dropdown = $('.dropdown');
      var biglogo = $('.big-logo');
      var mobilelogo = $('.mobile-logo');
      var menuside = 'right';

      // MOBILE
      if (screenwidth <= menubreakpoint) {

        // CLONE MAIN MENU
        $("#main-menu ul").clone().addClass("mmenu-init").prependTo(mobile_menu).removeAttr('id').removeClass('navbar-nav mx-auto').find('a').siblings('ul.dropdown-menu').removeAttr('class');

        header.addClass('mobile-header');
        header.removeClass('vertical-header , open-header');
        main_menu.css({
          "display": "none"
        });
        biglogo.css({
          "display": "none"
        });
        mobilelogo.css({
          "display": "block"
        });

        mobile_menu.mmenu({
          extensions: [
            'position-' + menuside,
            "fx-menu-slide",
          ],
        }, {

          offCanvas: {
            pageSelector: ".wrapper"
          },

          classNames: {
            fixedElements: {
              fixed: [
                'topbar',
                'header',
              ]
              //elemInsertsMethod: "insertBefore",
              //elemInsertSelector: ".wrapper"
            }
          }

        });

        var menu_API = mobile_menu.data("mmenu");
        menu_toggler.on("click", function() {
          menu_API.open();
          menu_API.close();
        });

        header.on("click", function() {
          menu_API.close();
        });

        menu_API.bind("open:finish", function() {
          setTimeout(function() {
            menu_toggler.addClass("open");
          });
        });

        menu_API.bind("close:finish", function() {
          setTimeout(function() {
            menu_toggler.removeClass("open");
          });
        });

      // DESKTOP
      } else {

        //DESKTOP HORIZONTAL MENU
        header.removeClass('mobile-header');
        main_menu.css({
          "display": "block"
        });

        biglogo.css({
          "display": "block"
        });
        mobilelogo.css({
          "display": "none"
        });

        // DESKTOP VERTICAL MENU
        if (header.hasClass('vertical-header')) {
          $('header').insertBefore('.wrapper');
          $('header > div').removeClass('container');
          if (header.hasClass('open-header')) {
            $('body').addClass('has-vertical-header-open');
            menu_toggler.css({
              "display": "none"
            });
          } else {
            $('body').addClass('has-vertical-header');
          }
          menu_toggler.on("click", function() {
            header.toggleClass('open-header');
            menu_toggler.toggleClass('open');
            $('body').toggleClass('has-vertical-header-open');
          });
        }

        // Open Drop Down Menu on hover for horizontal & vertical header
        dropdown.on({
          mouseenter: function() {
            $(this).addClass("open");
          },
          mouseleave: function() {
            $(this).removeClass('open');
            $('.submenu').removeClass('submenu-left');
          }
        });

      }
      header.addClass("loaded-header");
    }

    mmenuInit();

    $(window).resize(function() {
      mmenuInit();
    });

    // =============================================
    // ADD TO CART BUTTON
    // =============================================
    $(".add-to-cart").on({
      mouseenter: function() {
        $(this).parent().addClass("active");
      },
      mouseleave: function() {
        $(this).parent().removeClass("active");
      }
    });

    // =============================================
    // PRODUCT QUANTITY
    // =============================================
    $(function() {
      var spinner = $('.spinner');
      var spinnerplus = $('.spinner .btn:first-of-type')
      var spinnerminus = $('.spinner .btn:last-of-type');
      $(spinnerplus).on('click', function() {
        var btn = $(this);
        var input = btn.closest(spinner).find('input');
        if (input.attr('max') == undefined || parseInt(input.val()) < parseInt(input.attr('max'))) {
          input.val(parseInt(input.val(), 10) + 1, 10);
        } else {
          btn.next("disabled", true);
        }
      });
      $(spinnerminus).on('click', function() {
        var btn = $(this);
        var input = btn.closest(spinner).find('input');
        if (input.attr('min') == undefined || parseInt(input.val()) > parseInt(input.attr('min'))) {
          input.val(parseInt(input.val(), 10) - 1, 10);
        } else {
          btn.prev("disabled", true);
        }
      });
    })

    // =============================================
    // PRODUCT RATING
    // =============================================
    $('.user-rating input').on('change', function() {
      var radio = $(this);
      $('.user-rating .selected').removeClass('selected');
      radio.closest('label').addClass('selected');
    });

    // =============================================
    // POPUP BOOKING FORM
    // =============================================
    var roundedbookingform = $('.popup-booking-form')
    var roundedbookingformtoggle = $('.booking-form-toggle')
    roundedbookingformtoggle.on('click', function() {
      roundedbookingform.toggleClass('open');
      $(this).toggleClass('open');
    });

    // =============================================
    // DATEPICKER
    // =============================================
    var disabledDates = function(date) {
      var formatted = date.format('DD/MM/YYYY');
      return ["20/04/2018", "24/04/2018"].indexOf(formatted) > -1; // SET DISABLED DATES
    }

    $('.datepicker').daterangepicker({
      locale: {
        format: 'DD-MM-YYYY',
      },
      "startDate": moment(),
      "endDate": moment().add(5, 'day'),
      "minDate": moment(),
      isInvalidDate: disabledDates
    }, function(start, end, label) {});

    $(".calendar.left .daterangepicker_input").before("<div class='calendar-title'>Arrival Date</div>");
    $(".calendar.right .daterangepicker_input").before("<div class='calendar-title'>Departure Date</div>");

    // =============================================
    // GUESTS SELECT
    // =============================================
    $('.panel-dropdown .guestspicker').on('click', function(event) {
      $('.panel-dropdown').toggleClass('active');
      event.preventDefault();
    });
    $(window).click(function() {
      $('.panel-dropdown').removeClass('active');
    });
    $('.panel-dropdown').on('click', function(event) {
      event.stopPropagation();
    });

    function guestsSum() {
      var arr = $('.booking-guests');
      var guests = 0;
      for (var i = 0; i < arr.length; i++) {
        if (parseInt(arr[i].value, 10))
          guests += parseInt(arr[i].value, 10);
      }
      if (guests > 0) {
        var cardQty = document.querySelector(".gueststotal");
        cardQty.innerHTML = guests;
      }
    }
    guestsSum();
    $(function() {
      $(".plus, .minus").on("click", function() {
        var button = $(this);
        var oldValue = button.parent().find("input").val();
        if (button.hasClass('plus')) {
          var newVal = parseFloat(oldValue) + 1;
        } else {
          if (oldValue > 0) {
            var newVal = parseFloat(oldValue) - 1;
          } else {
            newVal = 0;
          }
        }
        button.parent().find("input").val(newVal);
        guestsSum();
      });

    });

    // =============================================
    // BOOKING FORM
    // =============================================
    $("#booking-form").on('submit', function(e) {
      e.preventDefault();

      //Get input field values from HTML form
      var booking_name = $("input[name=booking-name]").val();
      var booking_email = $("input[name=booking-email]").val();
      var booking_phone = $("input[name=booking-phone]").val();
      var booking_roomtype = $("select[name=booking-roomtype]").val();
      var booking_startdate = $("input[name=daterangepicker_start]").val();
      var booking_enddate = $("input[name=daterangepicker_end]").val();
      var booking_adults = $("input[name=booking-adults]").val();
      var booking_children = $("input[name=booking-children]").val();
      var booking_country = $("select[name=booking-country]").val();
      var booking_comments = $("textarea[name=booking-comments]").val();

      //Data to be sent to server
      var post_data;
      var output;
      post_data = {
        'booking_name': booking_name,
        'booking_email': booking_email,
        'booking_phone': booking_phone,
        'booking_roomtype': booking_roomtype,
        'booking_startdate': booking_startdate,
        'booking_enddate': booking_enddate,
        'booking_adults': booking_adults,
        'booking_children': booking_children,
        'booking_country': booking_country,
        'booking_comments': booking_comments
      };

      //Ajax post data to server
      $.post('email/booking.php', post_data, function(response) {

        var notification = $("#booking-notification");
        var bookingform = $("#booking-form");

        //Response server message
        output = '<p class="notification-text">' + response.text + '</div>';

        if (response.type === 'error') {
          notification.addClass('scale-out error');
          notification.removeClass('success');
          bookingform.addClass("booking-notification-open");
        } else {
          notification.addClass('scale-out success');
          notification.removeClass('error');
          //If success clear inputs
          $("input, textarea").val('');
          $('select').val('');
          $('select').val('').selectpicker('refresh');
        }
        notification.html(output);
        notification.delay(15000).queue(function(next) {
          $(this).removeClass("scale-out");
          bookingform.removeClass("booking-notification-open");
          next();
        });
        notification.on("click", function() {
          $(this).removeClass("scale-out");
          bookingform.removeClass("booking-notification-open");
        });
        $('#booking-form .form-control, #booking-form .bootstrap-select button, #booking-form .guestspicker').on("click", function() {
          notification.removeClass("scale-out");
          bookingform.removeClass("booking-notification-open");
        });

      }, 'json');

    });

    // =============================================
    // CONTACT FORM
    // =============================================
    $("#contact-form").on('submit', function(e) {
      e.preventDefault();

      //Get input field values from HTML form
      var user_name = $("input[name=name]").val();
      var user_phone = $("input[name=phone]").val();
      var user_email = $("input[name=email]").val();
      var user_subject = $("input[name=subject]").val();
      var user_message = $("textarea[name=message]").val();

      //Data to be sent to server
      var post_data;
      var output;
      post_data = {
        'user_name': user_name,
        'user_email': user_email,
        'user_message': user_message,
        'user_phone': user_phone,
        'user_subject': user_subject
      };

      //Ajax post data to server
      $.post('email/email.php', post_data, function(response) {

        var notification = $("#contact-notification");

        //Response server message
        output = '<p class="notification-text">' + response.text + '</div>';

        if (response.type === 'error') {
          notification.addClass('scale-out error');
          notification.removeClass('success');
        } else {
          notification.addClass('scale-out success');
          notification.removeClass('error');
          //If success clear inputs
          $("input, textarea").val('');
          $('select').val('');
          $('select').val('').selectpicker('refresh');
        }
        notification.html(output);
        notification.delay(15000).queue(function(next) {
          $(this).removeClass("scale-out");
          next();
        });
        notification.on("click", function() {
          $(this).removeClass("scale-out");
        });
        $('#contact-form .form-control').on("focus", function() {
          notification.removeClass("scale-out");
        });

      }, 'json');
    });

    // =============================================
    // SUBSCRIBE FORM (MAILCHIMP)
    // =============================================
    $("#subscribe-form").on('submit', function(e) {
      e.preventDefault();

      //Get input field values from HTML form
      var subscribe_email = $("input[name=subscribe-email]").val();

      //Data to be sent to server
      var post_data;
      var output;
      post_data = {
        'subscribe_email': subscribe_email,
      };

      //Ajax post data to server
      $.post('email/subscribe.php', post_data, function(response) {

        var notification = $("#subscribe-notification");

        //Response server message
        output = '<p class="notification-text">' + response.text + '</div>';

        if (response.type === 'error') {
          notification.addClass('scale-out error');
          notification.removeClass('success');
        } else {
          notification.addClass('scale-out success');
          notification.removeClass('error');
          //If success clear inputs
          $("input, textarea").val('');
          $('select').val('');
          $('select').val('').selectpicker('refresh');
        }
        notification.html(output);
        notification.delay(15000).queue(function(next) {
          $(this).removeClass("scale-out");
          next();
        });
        notification.on("click", function() {
          $(this).removeClass("scale-out");
        });
        $('#subscribe-form .form-control').on("focus", function() {
          notification.removeClass("scale-out");
        });

      }, 'json');
    });

    // =============================================
    // HOME PAGE 1 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-1").length) {
      var tpj = jQuery;
      var revapi1;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-1").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-1");
        } else {
          revapi1 = tpj("#rev-slider-1").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "auto",
            dottedOverlay: "none",
            delay: 9000,
            disableProgressBar: "on",
            navigation: {
              keyboardNavigation: "on",
              keyboard_direction: "horizontal",
              mouseScrollNavigation: "off",
              mouseScrollReverse: "default",
              onHoverStop: "on",
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 50,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              arrows: {
                style: "hermes",
                enable: true,
                hide_onmobile: true,
                hide_under: 600,
                hide_onleave: true,
                tmp: '<div class="tp-arr-allwrapper"><div class="tp-arr-imgholder"></div>',
                left: {
                  h_align: "left",
                  v_align: "center",
                  h_offset: 0,
                  v_offset: 0
                },
                right: {
                  h_align: "right",
                  v_align: "center",
                  h_offset: 0,
                  v_offset: 0
                }
              }

            },
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [800, 800, 700, 700],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "slidercenter",
              speed: 2000,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 55],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // HOME PAGE 2 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-2").length) {
      var tpj = jQuery;
      var revapi2;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-2").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-2");
        } else {
          revapi2 = tpj("#rev-slider-2").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "auto",
            dottedOverlay: "none",
            delay: 9000,
            disableProgressBar: "on",
            navigation: {
              keyboardNavigation: "on",
              keyboard_direction: "horizontal",
              mouseScrollNavigation: "off",
              mouseScrollReverse: "default",
              onHoverStop: "on",
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 50,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              arrows: {
                style: "hermes",
                enable: true,
                hide_onmobile: true,
                hide_under: 600,
                hide_onleave: true,
                tmp: '<div class="tp-arr-allwrapper"><div class="tp-arr-imgholder"></div>',
                left: {
                  h_align: "left",
                  v_align: "center",
                  h_offset: 0,
                  v_offset: 0
                },
                right: {
                  h_align: "right",
                  v_align: "center",
                  h_offset: 0,
                  v_offset: 0
                }
              }
            },
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [800, 800, 1100, 1100],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "slidercenter",
              speed: 2000,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 55],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // HOME PAGE 3 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-3").length) {
      var tpj = jQuery;
      var revapi3;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-3").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-3");
        } else {
          revapi3 = tpj("#rev-slider-3").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "fullscreen",
            dottedOverlay: "none",
            delay: 9000,
            navigation: {
              keyboardNavigation: 'on',
              keyboard_direction: 'horizontal',
              mouseScrollNavigation: 'off',
              mouseScrollReverse: 'default',
              onHoverStop: 'on',
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 1,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              bullets: {
                style: "",
                enable: true,
                container: "slider",
                hide_onmobile: true,
                hide_onleave: false,
                hide_delay: 200,
                hide_under: 0,
                hide_over: 9999,
                direction: "vertical",
                space: 5,
                h_align: "right",
                v_align: "center",
                h_offset: 50,
                v_offset: -15
              }
            },
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [800, 800, 800, 800],
            lazyType: "single",
            disableProgressBar: "on",
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: 1,
            stopAtSlide: 1,
            shuffle: "off",
            autoHeight: "on",
            autoWidth: "on",
            fullScreenAutoWidth: "on",
            fullScreenAlignForce: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // HOME PAGE 4 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-4").length) {
      var tpj = jQuery;
      var revapi4;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-4").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-4");
        } else {
          revapi4 = tpj("#rev-slider-4").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "fullscreen",
            dottedOverlay: "none",
            delay: 9000,
            navigation: {
              keyboardNavigation: "off",
              keyboard_direction: "horizontal",
              mouseScrollNavigation: "off",
              mouseScrollReverse: "default",
              onHoverStop: "off",
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 50,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
            },
            responsiveLevels: [1240, 1024, 778, 480],
            visibilityLevels: [1240, 1024, 778, 480],
            gridwidth: [1240, 1024, 778, 480],
            gridheight: [868, 768, 960, 720],
            lazyType: "none",
            parallax: {
              type: "3D",
              origo: "slidercenter",
              speed: 1000,
              levels: [2, 4, 6, 8, 10, 12, 14, 16, 45, 50, 47, 48, 49, 50, 0, 50],
              ddd_shadow: "off",
              ddd_bgfreeze: "on",
              ddd_overflow: "hidden",
              ddd_layer_overflow: "visible",
              ddd_z_correction: 100,
            },
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: 0,
            stopAtSlide: 1,
            shuffle: "off",
            autoHeight: "off",
            autoWidth: "off",
            fullScreenAutoWidth: "off",
            fullScreenAlignForce: "off",
            disableProgressBar: "on",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // HOME PAGE 5 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-5").length) {
      var tpj = jQuery;
      var revapi5;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-5").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-5");
        } else {
          revapi5 = tpj("#rev-slider-5").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "fullscreen",
            delay: 9000,
            navigation: {
              keyboardNavigation: 'on',
              keyboard_direction: 'horizontal',
              mouseScrollNavigation: 'on',
              mouseScrollReverse: 'default',
              onHoverStop: 'on',
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 1,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              bullets: {
                style: "",
                enable: true,
                container: "slider",
                hide_onmobile: true,
                hide_onleave: false,
                hide_delay: 200,
                hide_under: 0,
                hide_over: 9999,
                direction: "vertical",
                space: 5,
                h_align: "right",
                v_align: "center",
                h_offset: 50
              }
            },
            responsiveLevels: [1240, 1024, 778, 480],
            visibilityLevels: [1240, 1024, 778, 480],
            gridwidth: [1240, 1024, 778, 480],
            gridheight: [868, 768, 960, 720],
            lazyType: "none",
            scrolleffect: {
              blur: "on",
              maxblur: "2",
              on_slidebg: "on",
              direction: "top",
              multiplicator: "2",
              multiplicator_layers: "2",
              tilt: "10",
              disable_on_mobile: "off",
            },
            parallax: {
              type: "scroll",
              origo: "slidercenter",
              speed: 400,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 46, 47, 48, 49, 50, 51, 55],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            fullScreenAutoWidth: "on",
            fullScreenAlignForce: "on",
            disableProgressBar: "on",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // HOME PAGE 6 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-6").length) {
      var tpj = jQuery;
      var revapi6;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-6").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-6");
        } else {
          revapi6 = tpj("#rev-slider-6").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "auto",
            delay: 9000,
            navigation: {
              keyboardNavigation: "off",
              keyboard_direction: "vertical",
              mouseScrollNavigation: "off",
              mouseScrollReverse: "default",
              onHoverStop: "off",
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 1,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              bullets: {
                style: "",
                enable: true,
                container: "slider",
                hide_onmobile: false,
                hide_onleave: false,
                hide_delay: 200,
                hide_under: 0,
                hide_over: 9999,
                direction: "vertical",
                space: 5,
                h_align: "right",
                v_align: "center",
                h_offset: 50
              }
            },
            responsiveLevels: [1240, 1024, 778, 480],
            visibilityLevels: [1240, 1024, 778, 480],
            gridwidth: [1240, 1024, 778, 480],
            gridheight: [868, 768, 960, 720],
            lazyType: "none",
            scrolleffect: {
              blur: "on",
              maxblur: "2",
              on_slidebg: "on",
              direction: "top",
              multiplicator: "2",
              multiplicator_layers: "2",
              tilt: "10",
              disable_on_mobile: "off",
            },
            parallax: {
              type: "scroll",
              origo: "slidercenter",
              speed: 400,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 46, 47, 48, 49, 50, 51, 55],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            fullScreenAutoWidth: "on",
            fullScreenAlignForce: "off",
            disableProgressBar: "on",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // HOME PAGE 8 - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-7").length) {
      var tpj = jQuery;
      var revapi7;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-7").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-7");
        } else {
          revapi7 = tpj("#rev-slider-7").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "auto",
            dottedOverlay: "none",
            delay: 9000,
            disableProgressBar: "on",
            navigation: {
              keyboardNavigation: "on",
              keyboard_direction: "horizontal",
              mouseScrollNavigation: "off",
              mouseScrollReverse: "default",
              onHoverStop: "on",
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 50,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              arrows: {
                style: "zeus",
                enable: true,
                hide_onmobile: true,
                hide_under: 600,
                hide_onleave: true,
                tmp: '<div class="tp-title-wrap"><div class="tp-arr-imgholder"></div></div>',
                left: {
                  h_align: "left",
                  v_align: "center",
                  h_offset: 50,
                  v_offset: 0
                },
                right: {
                  h_align: "right",
                  v_align: "center",
                  h_offset: 50,
                  v_offset: 0
                }
              }
            },
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [830, 830, 700, 700],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "slidercenter",
              speed: 2000,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 55],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // COMING SOON - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-coming-soon").length) {
      var tpj = jQuery;
      var revapi8;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-coming-soon").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-coming-soon");
        } else {
          revapi8 = tpj("#rev-slider-coming-soon").show().revolution({
            sliderType: "hero",
            jsFileLocation: "revolution/js/",
            sliderLayout: "fullscreen",
            delay: 9000,
            navigation: {},
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "slidercenter",
              speed: 1000,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 46, 47, 48, 49, 50, 51, 55],
            },
            shadow: 0,
            spinner: "off",
            disableProgressBar: "on",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // EVENT DETAILS - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-event").length) {
      var tpj = jQuery;
      var revapi9;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-event").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-event");
        } else {
          revapi9 = tpj("#rev-slider-event").show().revolution({
            sliderType: "hero",
            jsFileLocation: "revolution/js/", 
            dottedOverlay: "twoxtwo",
            delay: 9000,
            navigation: {},
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [700, 700, 700, 700],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "enterpoint",
              speed: 400,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            },
            shadow: 0,
            spinner: "off",
            autoHeight: "off",
            disableProgressBar: "on",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // RESTAURANT - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-restaurant").length) {
      var tpj = jQuery;
      var revapi10;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-restaurant").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-restaurant");
        } else {
          revapi10 = tpj("#rev-slider-restaurant").show().revolution({
            sliderType: "hero",
            jsFileLocation: "revolution/js/",
            dottedOverlay: "twoxtwo",
            delay: 9000,
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [550, 550, 550, 550],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "enterpoint",
              speed: 400,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            },
            shadow: 0,
            spinner: "off",
            autoHeight: "off",
            forceFullWidth: "off",
            disableProgressBar: "on",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // SPA - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-spa").length) {
      var tpj = jQuery;
      var revapi11;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-spa").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-spa");
        } else {
          revapi11 = tpj("#rev-slider-spa").show().revolution({
            sliderType: "hero",
            jsFileLocation: "revolution/js/",
            dottedOverlay: "twoxtwo",
            delay: 9000,
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [550, 550, 550, 550],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "enterpoint",
              speed: 400,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            },
            shadow: 0,
            spinner: "off",
            autoHeight: "off",
            forceFullWidth: "off",
            disableProgressBar: "on",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // OFFER - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-offer").length) {
      var tpj = jQuery;
      var revapi12;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-offer").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-offer");
        } else {
          revapi12 = tpj("#rev-slider-offer").show().revolution({
            sliderType: "hero",
            jsFileLocation: "revolution/js/",
            dottedOverlay: "twoxtwo",
            delay: 9000,
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [550, 550, 700, 700],
            lazyType: "none",
            parallax: {
              type: "scroll",
              origo: "enterpoint",
              speed: 400,
              levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            },
            shadow: 0,
            spinner: "off",
            autoHeight: "off",
            forceFullWidth: "off",
            disableProgressBar: "on",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // GALLERY SLIDER - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-gallery").length) {
      var tpj = jQuery;
      var revapi13;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-gallery").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-gallery");
        } else {
          revapi13 = tpj("#rev-slider-gallery").show().revolution({
            sliderType: "carousel",
            jsFileLocation: "revolution/js/",
            sliderLayout: "auto",
            dottedOverlay: "none",
            delay: 9000,
            navigation: {
              keyboardNavigation: "on",
              keyboard_direction: "horizontal",
              mouseScrollNavigation: "on",
              mouseScrollReverse: "default",
              onHoverStop: "on",
            },
            carousel: {
              horizontal_align: "center",
              vertical_align: "center",
              fadeout: "on",
              vary_fade: "on",
              maxVisibleItems: 3,
              infinity: "on",
              space: 0,
              stretch: "off"
            },
            responsiveLevels: [1240, 1024, 778, 480],
            visibilityLevels: [1240, 1024, 778, 480],
            gridwidth: [600, 600, 400, 300],
            gridheight: [800, 800, 533, 400],
            lazyType: "none",
            shadow: 0,
            spinner: "off",
            stopLoop: "on",
            stopAfterLoops: 0,
            stopAtSlide: 1,
            shuffle: "off",
            autoHeight: "off",
            disableProgressBar: "on",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // ROOM SLIDER - REVOLUTION SLIDER
    // =============================================
    if ($("#rev-slider-room").length) {
      var tpj = jQuery;
      var revapi14;
      tpj(document).ready(function() {
        if (tpj("#rev-slider-room").revolution == undefined) {
          revslider_showDoubleJqueryError("#rev-slider-room");
        } else {
          revapi14 = tpj("#rev-slider-room").show().revolution({
            sliderType: "standard",
            jsFileLocation: "revolution/js/",
            sliderLayout: "auto",
            delay: 9000,
            navigation: {
              keyboardNavigation: 'on',
              keyboard_direction: 'horizontal',
              mouseScrollNavigation: 'off',
              mouseScrollReverse: 'default',
              onHoverStop: 'on',
              touch: {
                touchenabled: "on",
                swipe_threshold: 75,
                swipe_min_touches: 1,
                swipe_direction: "horizontal",
                drag_block_vertical: false
              },
              bullets: {
                style: "",
                enable: true,
                container: "slider",
                hide_onmobile: true,
                hide_onleave: false,
                hide_delay: 200,
                hide_under: 0,
                hide_over: 9999,
                direction: "vertical",
                space: 5,
                h_align: "right",
                v_align: "center",
                h_offset: 50,
                v_offset: -20
              }
            },
            viewPort: {
              enable: true,
              outof: "wait",
              visible_area: "80%"
            },
            responsiveLevels: [1200, 992, 768, 480],
            visibilityLevels: [1200, 992, 768, 480],
            gridwidth: [1200, 992, 768, 480],
            gridheight: [750, 750, 700, 600],
            lazyType: "single",
            disableProgressBar: "on",
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: 1,
            stopAtSlide: 1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
              simplifyAll: "off",
              nextSlideOnWindowFocus: "off",
              disableFocusListener: false,
            }
          });
        }
      });
    };

    // =============================================
    // MAGNIFIC POPUP
    // =============================================
    $(".magnific-popup, a[data-rel^='magnific-popup']").magnificPopup({
      type: 'image',
      mainClass: 'mfp-with-zoom',
      zoom: {
        enabled: true,
        duration: 300,
        easing: 'ease-in-out',
        opener: function(openerElement) {
          return openerElement.is('img') ? openerElement : openerElement.find('img');
        }
      },
      retina: {
        ratio: 1,
        replaceSrc: function(item, ratio) {
          return item.src.replace(/\.\w+$/, function(m) {
            return '@2x' + m;
          });
        }
      }
    });

    $('.image-gallery').each(function() {
      $(this).magnificPopup({
        //  delegate: '.owl-item:not(.cloned) a',
        delegate: 'a',
        type: 'image',
        mainClass: 'mfp-with-zoom',
        zoom: {
          enabled: true,
          duration: 300,
          easing: 'ease-in-out',
          fixedContentPos: true,
          opener: function(openerElement) {
            return openerElement.is('img') ? openerElement : openerElement.find('img');
          }
        },
        fixedContentPos: true,
        gallery: {
          enabled: true
        },
        removalDelay: 300,
        retina: {
          ratio: 1,
          replaceSrc: function(item, ratio) {
            return item.src.replace(/\.\w+$/, function(m) {
              return '@2x' + m;
            });
          }
        }

      });
    });


    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
    });

    // =============================================
    // WOW
    // =============================================
    new WOW().init();

    // =============================================
    // POP OVER & TOOLTIP
    // =============================================
    $('[data-toggle="popover"]').popover({
      html: true,
      offset: '0 10px'
    });

    $('[data-toggle="tooltip"]').tooltip({
      animated: 'fade',
      container: 'body',
      offset: '0 5px'
    });


    // =============================================
    // BOOTSTRAP SELECT
    // =============================================
    $('select').selectpicker({
      style: 'btn-info',
      size: 8
    });

    // =============================================
    // TESTIMONIALS - OWL CAROUSEL
    // =============================================
    var owl = $('.testimonials-owl');
    owl.owlCarousel({
      loop: true,
      items: 3,
      margin: 30,
      nav: false,
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 1
        },
        768: {
          items: 2
        },
        992: {
          items: 3
        }
      }
    });


    // =============================================
    // ROOMS - OWL CAROUSEL
    // =============================================
    var owl = $('.rooms-owl');
    owl.owlCarousel({
      loop: false,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 3
        },
        992: {
          items: 3
        }
      }
    });

    // =============================================
    // STAFF - OWL CAROUSEL
    // =============================================
    var owl = $('.staff-owl');
    owl.owlCarousel({
      loop: false,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 3
        },
        992: {
          items: 4
        }
      }
    });

    // =============================================
    // EVENTS - OWL CAROUSEL
    // =============================================
    var owl = $('.events-owl');
    owl.owlCarousel({
      loop: false,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 3
        },
        992: {
          items: 4
        }
      }
    });

    // =============================================
    // SHOP - OWL CAROUSEL
    // =============================================
    var owl = $('.shop-owl');
    owl.owlCarousel({
      loop: false,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 3
        },
        992: {
          items: 4
        }
      }
    });

    // =============================================
    // SHOP - OWL CAROUSEL
    // =============================================
    var owl = $('.shop-owl');
    owl.owlCarousel({
      loop: false,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 3
        },
        992: {
          items: 2
        }
      }
    });

    // =============================================
    // GALLERY - OWL CAROUSEL
    // =============================================
    var owl = $('.gallery-owl');
    owl.owlCarousel({
      loop: true,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 4
        },
        992: {
          items: 5
        }
      }
    });

    // =============================================
    // ROOMS - OWL CAROUSEL
    // =============================================
    var owl = $('.news-owl');
    owl.owlCarousel({
      loop: false,
      margin: 30,
      nav: true,
      dots: false,
      navText: [
        "<i class='fa fa-angle-left' aria-hidden='true'></i>",
        "<i class='fa fa-angle-right' aria-hidden='true'></i>"
      ],
      responsive: {
        0: {
          items: 1
        },
        480: {
          items: 2
        },
        768: {
          items: 3
        },
        992: {
          items: 3
        }
      }
    });

    // =============================================
    // SERVICES - OWL CAROUSEL
    // =============================================
    var owl = $('.services-owl');
    owl.owlCarousel({
      thumbs: true,
      thumbsPrerendered: true,
      items: 1,
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
      loop: true,
      autoplay: true,
      dots: false,
      nav: false,
      mouseDrag: false,
    });

    // =============================================
    // SERVICES VERSION 2 - OWL CAROUSEL
    // =============================================
    var owl = $('.services-v2-owl');
    owl.owlCarousel({
      items: 1,
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
      loop: true,
      autoplay: true,
      dots: false,
      nav: false,
      mouseDrag: false,
    });

    // =============================================
    // ROOM SLIDER - OWL CAROUSEL
    // =============================================
    if ($("#room-main-image").length) {
      var $sync1 = $("#room-main-image"),
        $sync2 = $("#room-thumbs"),
        duration = 300;

      $sync1.owlCarousel({
          items: 1,
          dots: false,
          animateIn: 'fadeIn',
          animateOut: 'fadeOut',
          autoplay: true,
          mouseDrag: false
        })
        .on('changed.owl.carousel', function(e) {
          var syncedPosition = syncPosition(e.item.index);

          if (syncedPosition != "stayStill") {
            $sync2.trigger('to.owl.carousel', [syncedPosition, duration, true]);
          }
        });

      $sync2
        .on('initialized.owl.carousel', function() {
          addClassCurrent(0);
        })
        .owlCarousel({
          dots: false,
          responsive: {
            0: {
              items: 4
            },
            600: {
              items: 4
            },
            960: {
              items: 5
            },
            1200: {
              items: 6
            }
          }
        })
        .on('click', '.owl-item', function() {
          $sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
        });

      function addClassCurrent(index) {
        $sync2
          .find(".owl-item")
          .removeClass("active-item")
          .eq(index).addClass("active-item");
      }

      function syncPosition(index) {
        addClassCurrent(index);
        var itemsNo = $sync2.find(".owl-item").length; //total items
        var visibleItemsNo = $sync2.find(".owl-item.active").length; //visible items

        if (itemsNo === visibleItemsNo) {
          return "stayStill";
        }
        var visibleCurrentIndex = $sync2.find(".owl-item.active").index($sync2.find(".owl-item.active-item"));

        if (visibleCurrentIndex == 0 && index != 0) {
          return index - 1;
        }
        if (visibleCurrentIndex == (visibleItemsNo - 1) && index != (itemsNo - 1)) {
          return index - visibleItemsNo + 2;
        }
        return "stayStill";
      }
    }

    // =============================================
    //  SHOP - OWL CAROUSEL
    // =============================================
    if ($(".big-images").length) {
      var $sync1 = $(".big-images"),
        $sync2 = $(".thumbs"),
        duration = 300;
      $sync1.owlCarousel({
          items: 1,
          dots: false,
        })
        .on('changed.owl.carousel', function(e) {
          var syncedPosition = syncPosition(e.item.index);

          if (syncedPosition != "stayStill") {
            $sync2.trigger('to.owl.carousel', [syncedPosition, duration, true]);
          }
        });
      $sync2
        .on('initialized.owl.carousel', function() {
          addClassCurrent(0);
        })
        .owlCarousel({
          dots: false,
          margin: 10,
          responsive: {
            0: {
              items: 3
            },
            600: {
              items: 3
            },
            960: {
              items: 4
            },
            1200: {
              items: 4
            }
          }
        })
        .on('click', '.owl-item', function() {
          $sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
        });

      function addClassCurrent(index) {
        $sync2
          .find(".owl-item")
          .removeClass("active-item")
          .eq(index).addClass("active-item");
      }

      function syncPosition(index) {
        addClassCurrent(index);
        var itemsNo = $sync2.find(".owl-item").length; //total items
        var visibleItemsNo = $sync2.find(".owl-item.active").length; //visible items

        if (itemsNo === visibleItemsNo) {
          return "stayStill";
        }
        var visibleCurrentIndex = $sync2.find(".owl-item.active").index($sync2.find(".owl-item.active-item"));

        if (visibleCurrentIndex == 0 && index != 0) {
          return index - 1;
        }
        if (visibleCurrentIndex == (visibleItemsNo - 1) && index != (itemsNo - 1)) {
          return index - visibleItemsNo + 2;
        }
        return "stayStill";
      }

    }

    // =============================================
    // TESTIMONIALS - RANDOM
    // =============================================
    var random = Math.floor(Math.random() * $('.testimonialv2-item').length);
    $('.testimonialv2-item').hide().eq(random).show();


    // =============================================
    // INSTAGRAM FEED - OWL CAROUSEL
    // =============================================
    if ($("#instafeed-gallery").length) {
      var galleryFeed = new Instafeed({
        get: "user",
        userId: 6954412019,
        accessToken: "6954412019.1677ed0.7a363e167d20449998757a3381ca9987",
        resolution: "standard_resolution",
        useHttp: "true",
        template: '<figure class="gradient-overlay-hover instagram-icon"><a href="{{link}}" target="_blank"><img src="{{image}}" class="img-responsive"></a></figure>',
        target: "instafeed-gallery",
        after: function() {
          var owl = $(".instagram-owl"),
            owlSlideSpeed = 300;
          $(document).ready(function() {
            owl.owlCarousel({
              loop: true,
              margin: 10,
              smartSpeed: 2000,
              dots: false,
              autoplay: true,
              autoplayTimeout: 4000,
              center: true,
              responsive: {
                0: {
                  items: 1
                },
                480: {
                  items: 3
                },
                760: {
                  items: 4
                },
                992: {
                  items: 6
                }
              }
            });
          });
        }
      });
      galleryFeed.run();
    }

    // =============================================
    // COUNT UP
    // =============================================
    var options = {
      useEasing: true,
      useGrouping: false,
      separator: ',',
      decimal: '.',
      prefix: '',
      suffix: ''
    };

    $('.countup-box').on('inview', function(event, visible) {
      if (visible) {

        $.each($('.number'), function() {
          var count = $(this).data('count'),
            numAnim = new CountUp(this, 0, count);
          numAnim.start();
        });

        $(this).unbind('inview');
      }
    });

    // =============================================
    // ISOTOPE
    // =============================================
    $(function() {
      var $grid = $('.grid').isotope({
        itemSelector: '.gallery-item'
      });
      // filters
      $('.gallery-filters').on('click', 'a', function(e) {
        e.preventDefault();
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({
          filter: filterValue
        });
      });
      // active class
      $('.gallery-filters').each(function(i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'a', function() {
          $buttonGroup.find('.active').removeClass('active');
          $(this).addClass('active');
        });
      });

      // fix for isotope overlapping images imagesloaded.pkgd.js required
      if ($(".grid").length) {
        // layout Isotope after each image loads
        $grid.imagesLoaded().progress(function() {
          $grid.isotope('layout');
        });
      }

    });

    // =============================================
    // MASONRY
    // =============================================
    var masonry_container = $('.masonry-grid');
    masonry_container.masonry({
      itemSelector: '.masonry-grid-item'
    });

    // =============================================
    // COMMING SOON PAGE
    // =============================================
    $('#countdown').each(function() {
      var $this = $(this),
        finalDate = $(this).data('countdown');
      $this.countdown(finalDate, function(event) {
        $this.html(event.strftime(
          '<div class="count-box"><div class="count-number">%D</div><div class="count-text">Days</div></div> ' + '<div class="count-box"><div class="count-number">%H</div><div class="count-text">Hours</div></div> ' + '<div class="count-box"><div class="count-number">%M</div><div class="count-text">Minutes</div></div> ' + '<div class="count-box"><div class="count-number">%S</div><div class="count-text">Seconds</div</div>'));
      });
    });

    // =============================================
    // BACK TO TOP
    // =============================================
    var amountScrolled = 500;
    var backtotop = $('.back-to-top');
    $(window).on('scroll', function() {
      if ($(window).scrollTop() > amountScrolled) {
        backtotop.addClass('active');
      } else {
        backtotop.removeClass('active');
      }
    });
    backtotop.on('click', function() {
      $('html, body').animate({
        scrollTop: 0
      }, 500);
      return false;
    });

    // =============================================
    // GOOGLE MAP
    // =============================================
    function initialize() {
      var map;
      var panorama;
      var var_latitude = 39.7715865; // Google Map Latitude
      var var_longitude = 19.997841; // Google Map Longitude
      var pin = 'images/icons/pin.svg';

      //Map pin-window details
      var title = "Hotel Himara - Click to see";
      var hotel_name = "Hotel Himara";
      var hotel_address = "Lorem ipsum dolor, 25, Himara";
      var hotel_desc = "5 star deluxe Hotel";
      var hotel_more_desc = "Lorem ipsum dolor sit amet, consectetur.";

      var hotel_location = new google.maps.LatLng(var_latitude, var_longitude);
      var mapOptions = {
        center: hotel_location,
        zoom: 14,
        scrollwheel: false,
        streetViewControl: false,
        styles: [{
          "featureType": "administrative",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#444444"
          }]
        }, {
          "featureType": "landscape",
          "elementType": "all",
          "stylers": [{
            "color": "#f5f5f5"
          }]
        }, {
          "featureType": "poi",
          "elementType": "all",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "road",
          "elementType": "all",
          "stylers": [{
            "saturation": -100
          }, {
            "lightness": 45
          }]
        }, {
          "featureType": "road.highway",
          "elementType": "all",
          "stylers": [{
            "visibility": "simplified"
          }]
        }, {
          "featureType": "road.arterial",
          "elementType": "labels.icon",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "transit",
          "elementType": "all",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "water",
          "elementType": "all",
          "stylers": [{
            "color": "#1dc1f8"
          }, {
            "visibility": "on"
          }]
        }]
      };

      map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

      var contentString =
        '<div id="infowindow_content">' +
        '<p><strong>' + hotel_name + '</strong><br>' +
        hotel_address + '<br>' +
        hotel_desc + '<br>' +
        hotel_more_desc + '</p>' +
        '</div>';

      var var_infowindow = new google.maps.InfoWindow({
        content: contentString
      });
      var marker = new google.maps.Marker({
        position: hotel_location,
        map: map,
        icon: pin,
        title: title,
        maxWidth: 500,
        optimized: false,
      });
      google.maps.event.addListener(marker, 'click', function() {
        var_infowindow.open(map, marker);
      });
      panorama = map.getStreetView();
      panorama.setPosition(hotel_location);
      panorama.setPov( /** @type {google.maps.StreetViewPov} */ ({
        heading: 265,
        pitch: 0
      }));
      var openStreet = document.getElementById('openStreetView');
      if (openStreet) {
        document.getElementById("openStreetView").onclick = function() {
          toggleStreetView()
        };
      }

      function toggleStreetView() {
        var toggle = panorama.getVisible();
        if (toggle == false) {
          panorama.setVisible(true);
        } else {
          panorama.setVisible(false);
        }
      }
    }
    //Check if google map exist
    if ($("#map-canvas").length) {
      google.maps.event.addDomListener(window, 'load', initialize);
    }

  });
})(jQuery);
