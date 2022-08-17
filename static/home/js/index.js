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

let isShown = false;

import {initSwiperSlider} from "./modules/slider";
import initModal from "./modules/modal";
import timer from "./modules/timer";

const commonOptions = {
    slidesPerView: 1,
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
    loop: true,
    autoplay: true,
    speed: 1500,
}

document.addEventListener('DOMContentLoaded', () => {
    initSwiperSlider('.reviews_slider--media', {
        ...commonOptions,
        watchSlidesProgress: true
    })
    initSwiperSlider('.reviews_slider--main', {
        ...commonOptions,
        thumbs: document.querySelector('.reviews_slider--media').swiper,
    })
    window.addEventListener('scroll', openPromoModal);
})

function openPromoModal() {
    if (window.pageYOffset > 1000 && !isShown) {
        initModal({
            html: `
                    <div class="modal_popup-wrapper d-lg-flex">
                        <div class="main col-lg-6">
                            <h4 class="main_subtitle">Special Offer</h4>
                            <h2 class="main_title">20% off your trip if it’s longer than 3 nights</h2>
                            <p class="main_text">Condimentum id venenatis eget arcu dictum varius duis at con sectetur</p>
                            <div class="main_timer timer d-flex justify-content-start">
                                <div class="timer_block theme-element d-flex flex-column justify-content-center">
                                    <span class="timer_block-number h4" id="days">30</span>
                                    days
                                </div>
                                <div class="timer_block theme-element d-flex flex-column justify-content-center">
                                    <span class="timer_block-number h4" id="hours">14</span>
                                    hours
                                </div>
                                <div class="timer_block theme-element d-flex flex-column justify-content-center">
                                    <span class="timer_block-number h4" id="minutes">18</span>
                                    <span class="short">mins</span>
                                    <span class="full">minutes</span>
                                </div>
                                <div class="timer_block theme-element d-flex flex-column justify-content-center">
                                    <span class="timer_block-number h4" id="seconds">10</span>
                                    <span class="short">secs</span>
                                    <span class="full">seconds</span>
                                </div>
                            </div>
                            <a class="main_btn btn theme-element theme-element--accent" href="rooms.html">Choose room</a>
                        </div>
                        <div class="media col-lg-6">
                            <picture>
                                <source data-srcset="img/placeholder.jpg"
                                        srcset="img/placeholder.jpg">
                                <img class="lazy"
                                     data-src="img/placeholder.jpg"
                                     src="img/placeholder.jpg"
                                     alt="media">
                            </picture>
                        </div>
                    </div>   
                `,
        }, 'modal_popup--promo')
        isShown = true;
        timer('.timer', '2022-02-29')
    }
}