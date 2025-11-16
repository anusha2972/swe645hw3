// Team members:
//  1. Anusha Gurram – G01514835
//  2. Bala Naga Tirumala Kiran Annadata – G01508483
// 3. Yashwanth Karthikeya Settem– G01512992
// Entry point that renders the main App component into the root DOM element using React 18's createRoot API.


import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
