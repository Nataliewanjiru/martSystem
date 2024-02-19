import React, { useState } from 'react';
import 'react-geocoding';
import * as maptilersdk from '@maptiler/sdk';
import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";

const Location = ({apiKey,map }) => {
  const [searchTerm, setSearchTerm] = useState('');


  const handleChange = async (e) => {
    const newValue = e.target.value;
    setSearchTerm(newValue);
  };

  useEffect(() => {
    const gc = new GeocodingControl({ apiKey, maplibregl: maptilersdk });
    map.current.addControl(gc);

    // Cleanup function: remove the control when the component unmounts
    return () => {
      map.current.removeControl(gc);
    };
  }, [apiKey, map]);
  

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={handleChange}
        placeholder="Enter location..."
      />
    </div>
  );
};

export default Location;

