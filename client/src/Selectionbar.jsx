import React, { useState } from 'react'
import Location from './Location'
import Locationmethod2 from './Locationmethod2'

function Selectionbar({apiKey,map}) {
  
  return (
    <>
   <Location apiKey={apiKey} map={map}/>
   </>
  )
}

export default Selectionbar