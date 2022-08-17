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

const _KEY = 'PasteYourGoogleMapsApiKeyHere';

import {Loader} from "@googlemaps/js-api-loader";
import mapTheme from "./map-theme";

function initMap() {
    const loader = new Loader({
        apiKey: _KEY,
        version: "weekly",

    });
    const mapContainer = document.querySelector('#map');
    const defaultMarker = { lat: 40.74881584652125, lng: -73.98561648634562 };

    loader.load().then(() => {
        const map = new google.maps.Map(mapContainer, {
            center: defaultMarker,
            zoom: 16,
            styles: [...mapTheme],
            disableDefaultUI: true,
        });
        const marker = new google.maps.Marker({
            position: defaultMarker,
            map: map,
            icon: './svg/marker.svg'
        });
    });
}

export default initMap;