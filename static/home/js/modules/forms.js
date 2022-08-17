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

const emailRegExp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

import initModal from "./modal";
import pickmeup from 'pickmeup';

async function sendForm(form) {
    let handler = form.getAttribute('action');
    if (handler !== '' && handler !== '#') {
        const response = await fetch(
            handler,
            {
                method: 'POST',
                body: new FormData(form)
            }
        );
        if(response.ok) {
            form.reset();
        }
    }
}

export function validateForm(target, fieldSelector = '.field') {
    const form = document.querySelector(target);
    const inputsArr = document.querySelectorAll(`${target} ${fieldSelector}`);

    let notificationText = '';

    const valid = elem => !elem.classList.contains('error');

    if (form) {
        form.addEventListener('submit', e => {
            for (let i = 0; i < inputsArr.length; i++) {
                const el = inputsArr[i];
                const value = el.value;
                if (el.classList.contains('required') && value === '') {
                    el.classList.add('error');
                } else if (el.dataset.type === 'email' && !emailRegExp.test(value)) {
                    el.classList.add('error');
                } else if (el.dataset.type === 'tel' && isNaN(+value)) {
                    el.classList.add('error');
                }

                el.addEventListener('input', () => {
                    el.classList.remove('error');
                });
            }

            if (Array.from(inputsArr).every(valid)) {
                inputsArr.forEach(el => {
                    el.classList.remove('error');
                })
                if (form.dataset.type === 'search') {
                    notificationText = 'Nothing found.';
                } else if (form.dataset.type === 'subscribe') {
                    notificationText = 'Subscription confirmation has been sent to your Email.';
                } else if (form.dataset.type === 'feedback') {
                    notificationText = 'Your message has been sent. We\'ll reply you as soon as possible.';
                } else if (form.dataset.type === 'reviewRoom' || form.dataset.type === 'comment') {
                    notificationText = 'Your comment is awaiting moderation.';
                }

                let notification = {
                    toast: true,
                    position: 'top-end',
                    timer: 3000,
                    html: `<p class="main">${notificationText}</p>`,
                    customClass: {
                        popup: 'alert_popup',
                        title: 'alert_popup-title',
                        htmlContainer: 'alert_popup-content',
                        closeButton: 'alert_popup-close',
                        container: 'alert_popup-container'
                    }
                };
                sendForm(form);
                initModal(notification);
            }
        })
    }
}

export function validate() {
    validateForm('[data-type="search"]');
    validateForm('[data-type="comment"]');
    validateForm('[data-type="reviewRoom"]');
    validateForm('[data-type="subscribe"]');
    validateForm('[data-type="feedback"]');
}

export function applyDatepicker() {
    let currentDate = new Date;
    const arrivalDate = document.querySelector('[data-start="true"]');
    const departureDate = document.querySelector('[data-end="true"]');

    const pickerDefaults = {
        hide_on_select: true,
        default_date: false,
        format: 'm.d.Y'
    }

    if (arrivalDate && departureDate) {
        const pickmeupArrivalInstance = pickmeup(arrivalDate, {
            min: new Date,
            ...pickerDefaults
        });

        const pickmeupDepartureInstance = pickmeup(departureDate, {
            render: function (date) {
                if (date < currentDate) {
                    return {disabled: true, class_name: 'date-in-past'};
                }
                return {};
            },
            ...pickerDefaults
        });

        departureDate.style.pointerEvents = 'none';

        arrivalDate.addEventListener('pickmeup-change', function (e) {
            currentDate = e.detail.date;
            pickmeupDepartureInstance.update();
            departureDate.style.pointerEvents = 'unset';
        });
    }

}

export function setBookingGuestsValue() {
    const displayFieldAll = document.querySelector('#guests');
    const adultsDisplay = document.querySelector('#adults');
    const childrenDisplay = document.querySelector('#children');
    const qtyFields = document.querySelectorAll('.booking_group-dropdown_wrapper .main');

    qtyFields.forEach((el, i) => {
        const triggers = el.querySelectorAll('.qty-changer');
        const triggerMinus = el.querySelector('.qty_minus');
        const triggerPlus = el.querySelector('.qty_plus');
        const targetDisplay = el.querySelector('input');
        let targetDisplayValue = parseInt(targetDisplay.getAttribute('value'));
        triggers.forEach((trigger, index) => {
            checkValue();
            trigger.addEventListener('click', () => {
                if (trigger.classList.contains('qty_plus')) {
                    targetDisplayValue++;
                    checkValue();
                } else if (trigger.classList.contains('qty_minus')) {
                    targetDisplayValue--;
                    checkValue();

                    if (targetDisplayValue < 1 && targetDisplay.id === 'children') {
                        targetDisplayValue = 0;
                    }
                }

            })
        })

        function checkValue() {
            if (targetDisplayValue > 1 || (targetDisplay.id === 'children' && targetDisplayValue === 1)) {
                triggerMinus.dataset.disabled = "";
            } else {
                triggerMinus.dataset.disabled = "true";
            }
            if (targetDisplayValue === 99) {
                triggerPlus.dataset.disabled = "true";
            } else {
                triggerPlus.dataset.disabled = "";
            }

            targetDisplay.setAttribute('value', targetDisplayValue);

            let result = `${adultsDisplay.value} adult${parseInt(adultsDisplay.value) > 1 ? 's' : ''}`;

            if (parseInt(childrenDisplay.value) >= 1) {
                result += ` ${childrenDisplay.value}`;
                if (parseInt(childrenDisplay.value) === 1) {
                    result += ' child';
                } else {
                    result += ' children';
                }
            }

            displayFieldAll.textContent = result;

        }

        checkValue();
    })
}