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

export function preventDefault() {
    const emptyLinks = document.querySelectorAll('a[href="#"]');
    const forms = document.querySelectorAll('form');

    emptyLinks.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
        })
    })

    forms.forEach(form => {
        form.addEventListener('submit', e => {
            e.preventDefault();
        })
    })
}

export function setAccordionWrapperHeight() {
    const accordionItems = document.querySelectorAll('.accordion_component-item');
    const accordionWrappers = document.querySelectorAll('.accordion_component-item .item-wrapper');

    accordionItems.forEach((el, i) => {
        el.addEventListener('hidden.bs.collapse', () => {
            accordionWrappers[i].style.height = 'unset';
        })
    })
}

export function inViewport(el) {
    let rect = el.getBoundingClientRect();
    return rect.bottom < 0 || rect.right < 0 || rect.left > window.innerWidth || rect.top > window.innerHeight;
}

export function changeRating() {
    const ratingStars = [...document.querySelectorAll('[data-type="changeable"] .star')];

    function executeRating(stars) {
        const starClassActive = "icon-star icon active";
        const starClassInactive = "icon-star icon";
        const starsLength = stars.length;
        let i;
        stars.map((star) => {

            function setActiveStarState() {
                i = stars.indexOf(star);

                if (star.className === starClassInactive) {
                    for (i; i >= 0; --i) stars[i].className = starClassActive;
                } else {
                    for (i; i < starsLength; ++i) stars[i].className = starClassInactive;
                }
            }

            star.addEventListener('click', setActiveStarState);
        });
    }

    executeRating(ratingStars);
}

