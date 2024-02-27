import React, { useState } from 'react'
import Location from './Location'


function Selectionbar({apiKey,map}) {
  
  return (
    <div className='selection-wrap'>
   <Location apiKey={apiKey} map={map}/>
   </div>
  )
}

export default Selectionbar