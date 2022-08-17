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

import Headroom from "headroom.js";
import hcSticky from 'hc-sticky';
import offcanvas from "bootstrap/js/src/offcanvas";

export function drawNav() {
    const header = document.querySelector('.header');
    const menu = document.querySelector('.header_nav');
    const menuTrigger = document.querySelector('.header_trigger');
    const menuOffcanvas = document.querySelector('#menuOffcanvas');
    const bsOffcanvas = new offcanvas(menuOffcanvas)

    menuTrigger.addEventListener('click', () => {
        menuTrigger.classList.toggle('active');
        menu.classList.toggle('active');
        header.classList.add('sticky', 'opened');
    })

    function closeMenu() {
        menuTrigger.classList.remove('active');
        menu.classList.remove('active');
        header.classList.remove('opened');
        bsOffcanvas.hide();
    }

    menuOffcanvas.addEventListener('show.bs.offcanvas', () => {
        document.documentElement.classList.add('fixed');
        menuOffcanvas.style.transition = 'transform .5s ease'
    })

    menuOffcanvas.addEventListener('hidden.bs.offcanvas', () => {
        document.documentElement.classList.remove('fixed');
        menuOffcanvas.style.transition = 'unset'
    })


    initHeadroom(header);
    setActivePageClass(header);
    setDropdownMenu(menuOffcanvas);

    window.addEventListener('scroll', () => makeNavSticky(header, menuTrigger));
    window.addEventListener('resize', closeMenu);
    window.addEventListener('resize', () => setDropdownMenu(menuOffcanvas));
}

// hide header on scroll
function initHeadroom(headerEl) {
    const headroom = new Headroom(headerEl, {
        offset: 500,
        classes: {
            pinned: "header--pinned",
            unpinned: "header--unpinned",
        }
    });
    headroom.init();
}

// set activity class for the current page
function setActivePageClass(headerEl) {
    const menuListItems = document.querySelectorAll('.nav-item');
    const menuLinkItems = document.querySelectorAll('.nav-link');

    menuListItems.forEach(item => addClass(item));
    menuLinkItems.forEach(item => addClass(item));

    function addClass(el) {
        if (el.dataset.page === headerEl.dataset.page) {
            el.classList.add('current');
        }
    }
}

// change header on scroll

// dropdown menus (mobile/desktop)
function setDropdownMenu(offcanvas) {
    const dropdownElems = document.querySelectorAll('.header .dropdown');
    const triggers = document.querySelectorAll('.header .dropdown-toggle');
    const menuLists = document.querySelectorAll('.header .dropdown-menu');

    if (window.innerWidth < 992) {
        offcanvas.classList.add('offcanvas', 'offcanvas-end');
    } else {
        offcanvas.classList.remove('offcanvas', 'offcanvas-end');
        offcanvas.style.visibility = 'visible';
    }

    triggers.forEach((el, i) => {

        function closeMenu() {
            el.classList.remove('active');
            menuLists[i].classList.remove('active');
        }

        if (window.innerWidth < 992) {
            el.dataset.bsToggle = 'collapse';
            menuLists[i].classList.add('collapse');
            el.addEventListener('click', () => {
                el.classList.toggle('active');
                menuLists[i].classList.toggle('active');
            })
            window.addEventListener('resize', closeMenu)
        } else {
            el.dataset.bsToggle = '';
            menuLists[i].classList.remove('collapse');
            window.addEventListener('resize', closeMenu);
            window.addEventListener('scroll', closeMenu)
        }

    })


    dropdownElems.forEach(el => {

        el.addEventListener('mouseover', function (e) {
            let trigger = this.querySelector('a[data-bs-toggle]');
            let menu = trigger.nextElementSibling;
            trigger.classList.add('active');
            menu.classList.add('active');
        });

        el.addEventListener('mouseleave', function (e) {
            let trigger = this.querySelector('a[data-bs-toggle]');
            let menu = trigger.nextElementSibling;
            trigger.classList.remove('active');
            menu.classList.remove('active');
        })
    })

}

function makeNavSticky(headerEl, triggerEL) {
    const nextEl = headerEl.nextElementSibling;

    if (window.scrollY > 0 || triggerEL.classList.contains('active')) {
        headerEl.classList.add('sticky');

        if (headerEl.classList.contains('sticky')) {
            if (window.innerWidth < 992) {
                nextEl.style.marginTop = '60px';
            } else {
                nextEl.style.marginTop = '108px';
                if (headerEl.classList.contains('sticky')) {
                    nextEl.style.marginTop = '80px';
                }
            }
        }

    } else if (!triggerEL.classList.contains('active')) {
        headerEl.classList.remove('sticky');
        nextEl.style.marginTop = '0px';
    }
}


// sticky sidebar
export function makeElementSticky(selector = '[data-sticky="true"]', parent = '.sticky-parent') {
    const stickyElement = document.querySelector(selector);

    const commonOptions = {
        stickTo: parent,
        followScroll: false,
        responsive: {
            queries: {
                768: {
                    disable: true,
                    bottomEnd: 0
                }
            }
        }
    }

    if (stickyElement) {
        if (stickyElement.dataset.stop === "90") {
            let Sticky = new hcSticky(selector, {
                ...commonOptions,
                bottomEnd: 90
            });
        } else {
            let Sticky = new hcSticky(selector, {
                ...commonOptions,
                bottomEnd: 0,
            });
        }
    }
}
