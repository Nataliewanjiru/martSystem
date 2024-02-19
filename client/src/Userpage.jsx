import React from 'react'
import Sidebar from './Sidebar'
import Middlebar from './Middlebar'
import Selectionbar from './Selectionbar'
import Appnavbar from './Navbar'
import './index.css'
import Geocode from 'react-geocoding';
import { useState,useRef,useEffect } from 'react'
import * as maptilersdk from '@maptiler/sdk';
import '@maptiler/sdk/dist/maptiler-sdk.css';
import './App.css';
import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";




function Userpage() {
  const mapContainer = useRef(null);
  const nairobi = { lng: 36.817223, lat: -1.286389 };
  const [zoom] = useState(14);
  const apiKey = 'JtiBf6AAQoLwnsi1NH8q';
  maptilersdk.config.apiKey = 'JtiBf6AAQoLwnsi1NH8q';
  const [map, setMap] = useState(null)

  useEffect(() => {
    const newMap = new maptilersdk.Map({
      container: mapContainer.current,
      style: maptilersdk.MapStyle.STREETS,
      center: [nairobi.lng, nairobi.lat],
      zoom: zoom,
    }
    );
    
    setMap(newMap); 

    const gc = new GeocodingControl({ apiKey, maplibregl: maptilersdk });
    map.addControl(gc);

    return () => {
      if (map) {
        map.removeControl(gc);
        map.remove();
      }
    };
  }, [nairobi.lng, nairobi.lat, zoom, apiKey]);

  return (
    <div className='userpage-parent'>
      <Appnavbar />
      <div className='userpage-separationline'></div>
      <div className='userpage-child'>
        <Sidebar />
        <Middlebar mapContainer={mapContainer} />
        <Selectionbar apiKey={apiKey} map={map}/>
      </div>
    </div>
  );
}

export default Userpage;
