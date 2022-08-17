/**
 * Hosteller
 * Hosteller Template created for hostels, students hotels, guest houses, small hotel, resort, room reservation, travel and more
 * Exclusively on https://1.envato.market/hosteller-html
 *
 * @encoding        UTF-8
 * @version         1.0.3
 * @copyright       (C) 2018 - 2022 Merkulove ( https://merkulov.design/ ). All rights reserved.
 * @license         Envato License https://1.envato.market/KYbje
 * @contributors    Lamber Lilit (winter.rituel@gmail.com)
 * @support         help@merkulov.design
 **/
"use strict";

import initProgressbar from "./modules/progress";
import {initSwiperSlider} from "./modules/slider";

document.addEventListener('DOMContentLoaded', () => {
    initProgressbar('.room_main .rating');
    initSwiperSlider('.room_main-slider_thumbs', {
        slidesPerView: 2,
        spaceBetween: 15,
        loop: true,
        watchSlidesProgress: true,
        autoplay: true,
        speed: 1500,
        breakpoints: {
            768: {
                spaceBetween: 30
            },
        }
    })
    swiperChangeableDirection();
    initSwiperSlider('.room_main-slider_view', {
        slidesPerView: 1,
        effect: 'fade',
        crossFade: true,
        loop: true,
        thumbs: document.querySelector('.room_main-slider_thumbs').swiper,
        autoplay: true,
        speed: 1500,
    })

    window.addEventListener('resize', swiperChangeableDirection);
})


function swiperChangeableDirection() {
    const thumbsInstance = document.querySelector('.room_main-slider_thumbs').swiper;

    if(window.innerWidth < 991.98) {
        thumbsInstance.changeDirection('horizontal');
    } else {
        thumbsInstance.changeDirection('vertical');
    }
}