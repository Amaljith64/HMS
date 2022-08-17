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

export function animateMouseMove() {
    document.addEventListener("mousemove", parallax);
    function parallax(e){
        this.querySelectorAll('.animatedElement').forEach(layer => {
            const speed = layer.getAttribute('data-speed');
            const direction = layer.getAttribute('data-direction');

            const x = (window.innerWidth - e.pageX*speed)/100
            const y = (window.innerHeight - e.pageY*speed)/100

            if (direction === 'both') {
                layer.style.transform = `translateX(${x}px) translateY(${y}px)`
            } else if (direction === 'moveX') {
                layer.style.transform = `translateX(${x}px)`
            } else if (direction === "moveY") {
                layer.style.transform = `translateY(${y}px)`
            }

        })
    }
}