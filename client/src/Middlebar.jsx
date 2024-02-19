import React, { useRef, useEffect, useState } from 'react';
import * as maptilersdk from '@maptiler/sdk';
import '@maptiler/sdk/dist/maptiler-sdk.css';
import './App.css';
import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";

export default function Middlebar({mapContainer}) {
  return (
    <div className="map-wrap">
      <div ref={mapContainer} className="map" />
    </div>
  );
}
