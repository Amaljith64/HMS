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
'use strict';

import ProgressBar from 'progressbar.js/dist/progressbar';
import { inViewport } from './helpers';

function initProgressbar(container) {
    const progressBars = document.querySelectorAll('.progressLine');
    const rootEl = document.querySelector(container);
    progressBars.forEach(bar => {
        let id = bar.getAttribute('id');
        let value = bar.dataset.value;
        let limit = value / 5;

        let lineBar = new ProgressBar.Line(`#${id}`, {
            strokeWidth: 7.5,
            trailWidth: 7.5,
            trailColor: '#ddeaf6',
            from: {color: '#DDEAF6'},
            to: {color: '#235784'},
            text: {
                value: '0',
                className: 'progress-text',
            },
            step: (state, shape) => {
                shape.path.setAttribute("stroke", state.color);
                shape.setText(`${value}`);
            }
        });

        function animateProgress() {
            lineBar.animate(limit, {
                duration: 700
            });
        }

        window.addEventListener('scroll', checkVisibility);
        window.addEventListener('load', checkVisibility);

        function checkVisibility() {
            if(!inViewport(rootEl)) {
                animateProgress();
            }
        }

    })

}

export default initProgressbar;