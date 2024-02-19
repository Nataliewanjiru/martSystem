import React, { useState } from 'react'
import Location from './Location'

function Selectionbar({apiKey,map}) {
  
  return (
   <Location apiKey={apiKey} map={map}/>
  )
}

export default Selectionbar