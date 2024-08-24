import { useState } from 'react'
import Theme from './components/theme'
import Limit from './components/Limit'
import Colorize from './components/Colorize'
import Timer from './components/Timer'
import Expander from './components/Expander'

export default function App() {
  return (
    <main>
      <Theme />
      <Limit />
      <Colorize />
      <Timer />
      <Expander />
    </main>
  )
}