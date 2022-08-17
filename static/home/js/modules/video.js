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

import YouTubePlayer from 'youtube-player';

function setYTFrame() {

    const trigger = document.querySelector('.video-play');
    const popup = document.querySelector('.video');
    const playerElem = document.querySelector('#player');

    if (playerElem) {
        let player;
        player = YouTubePlayer('player');
        player.loadVideoById('ixIzimI35SE');
        player.stopVideo();

        if (popup) {
            document.body.addEventListener('click', (e) => {
                if (e.target !== null) {
                    if (popup.classList.contains('visible')) {
                        if (e.target !== playerElem) {
                            popup.classList.remove('visible', 'fadeIn');
                            popup.classList.add('fadeOut');
                            player.stopVideo();
                        }
                    } else if (e.target === trigger || (e.target.closest('a') !== null && e.target.closest('a').classList.contains('video-play'))) {
                        e.preventDefault();
                        popup.classList.remove('fadeOut');
                        popup.classList.add('visible', 'fadeIn');
                    }
                }
            })
        }
    }
}

export default setYTFrame;