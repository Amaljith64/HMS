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
import Shuffle from 'shufflejs';

function initFilter(container, trigger, options) {
    const containerEl = document.querySelector(container);

    if (containerEl) {
        const shuffleInstance = new Shuffle(containerEl, {...options});
        const triggers = document.querySelectorAll(trigger);

        triggers.forEach(el => {
            el.addEventListener('click', function (e) {
                e.preventDefault();
                for (let i = 0; i < triggers.length; i++) {
                    triggers[i].classList.remove('active');
                }
                this.classList.add('active');
                const filter = this.dataset.target;
                shuffleInstance.filter(filter);
            })
        })
    }
}


export default initFilter;