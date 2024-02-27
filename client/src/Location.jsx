import React, { useState,useEffect } from 'react';
import 'react-geocoding';
import * as maptilersdk from '@maptiler/sdk';
import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";

const Location = ({apiKey,map }) => {
const[option1,setOption1]=useState(false)
const[option2,setOption2]=useState(false)


useEffect(() => {
  if(map){
  const gc = new GeocodingControl({ apiKey, maplibregl: maptilersdk });
  map.addControl(gc);
  
  // Cleanup function: remove the control when the component unmounts
  return () => {
    map.removeControl(gc);
  };
}
}, [option1]);
 
const handleFirstLocationInput=() => {
setOption1(true)
}

  return (
    <div>
      <button>current location</button>
      <button onClick={handleFirstLocationInput}>find location</button>
    </div>
  );
};

export default Location;
