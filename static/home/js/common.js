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

import {Collapse, Offcanvas, Tab, Dropdown} from "bootstrap";
import AOS from 'aos';
import svg4everybody from "svg4everybody";
import LazyLoad from "vanilla-lazyload";

import {preventDefault} from "./modules/helpers";
import {drawNav, makeElementSticky} from "./modules/nav";
import initMap from "./modules/map";
import {validate, setBookingGuestsValue} from "./modules/forms";
import animateNumber from "./modules/counter";
import setRatingStars from "./modules/rating";
import {applyDatepicker} from "./modules/forms";
import shaveTitle from "./modules/shave";
import drawAccordion from "./modules/accordion";
import setYTFrame from "./modules/video";

document.addEventListener('DOMContentLoaded', () => {
    drawNav();
    svg4everybody();

    AOS.init({
        offset: 30, // offset (in px) from the original trigger point
        delay: 0, // values from 0 to 3000, with step 50ms
        duration: 650, // values from 0 to 3000, with step 50ms
        easing: 'ease', // default easing for AOS animations
        once: true, // animation repeat
    });

    const lazyload = new LazyLoad();

    preventDefault();

    makeElementSticky();

    animateNumber();

    setRatingStars();

    drawAccordion();

    applyDatepicker();

    shaveTitle();

    if (document.querySelector('#map')) {
        initMap();
    }

    window.addEventListener('resize', shaveTitle);

    validate();
    setBookingGuestsValue();
    setYTFrame();
})

