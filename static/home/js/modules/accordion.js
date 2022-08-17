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

function drawAccordion() {
    const wrappers = document.querySelectorAll('.accordion_component-item .item-wrapper');
    const contentElems = document.querySelectorAll('.accordion_component-item .accordion-collapse');

    contentElems.forEach((el, i) => {
        el.addEventListener('shown.bs.collapse', () => {
            wrappers[i].style.height = '100%';
        })
        el.addEventListener('hide.bs.collapse', () => {
            wrappers[i].style.height = 'unset';
        })
    })
}

export default drawAccordion;