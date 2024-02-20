import React from 'react'
import Sidebar from './Sidebar'
import Middlebar from './Middlebar'
import Selectionbar from './Selectionbar'
import Appnavbar from './Navbar'
import './index.css'
import maplibregl from 'maplibre-gl';
import { useState,useRef,useEffect } from 'react'
import * as maptilersdk from '@maptiler/sdk';
import '@maptiler/sdk/dist/maptiler-sdk.css';
import './App.css';
//import MapboxGeolocateControl from '@mapbox/mapbox-gl-geolocate-control';
import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";




function Userpage() {
  const mapContainer = useRef(null);
  const nairobi = { lng: 36.817223, lat: -1.286389 };
  const [zoom] = useState(14);
  const apiKey = 'JtiBf6AAQoLwnsi1NH8q';
  maptilersdk.config.apiKey = 'JtiBf6AAQoLwnsi1NH8q';
  const [map, setMap] = useState(null)
 

useEffect(() => {
    const initializeMap = async () => {
      const newMap = new maptilersdk.Map({
        container: mapContainer.current,
        style: maptilersdk.MapStyle.STREETS,
        center: [nairobi.lng, nairobi.lat],
        zoom: zoom,
      });


      const geolocateControl = new maptilersdk.GeolocateControl({
        positionOptions: {
          enableHighAccuracy: true,
        },
        trackUserLocation: true,
        showUserLocation: true,
      });
    
      // Add the geolocate control to the map
      newMap.addControl(geolocateControl);
      newMap.on('load', () => {
        setMap(newMap) 
      });



    };

    initializeMap();
  }, [nairobi.lng, nairobi.lat, zoom, apiKey]);

  const handleFindLocationClick= () => {
    if (map) {
      map.flyTo({ center: map.getCenter(), zoom: 14 });
    }
  };

  return (
    <div className='userpage-parent'>
      <Appnavbar />
      <div className='userpage-separationline'></div>
      <div className='userpage-child'>
        <Sidebar />
        <Middlebar mapContainer={mapContainer} />
        <Selectionbar apiKey={apiKey} map={map}/>
      </div>
      <button onClick={handleFindLocationClick}>Find My Location</button>
    </div>
  );
}

export default Userpage;
