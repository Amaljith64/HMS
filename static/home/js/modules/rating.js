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

import StarRating from 'star-rating.js';

function setRatingStars() {
    const starsElems = document.querySelectorAll('.star-rating');
    if (starsElems.length !== 0) {
        const stars = new StarRating('.star-rating', {
            tooltip: false
        });
    }
}

export default setRatingStars;