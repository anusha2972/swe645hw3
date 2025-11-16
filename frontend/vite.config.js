// Team members:
//  1. Anusha Gurram – G01514835
//  2. Bala Naga Tirumala Kiran Annadata – G01508483
// 3. Yashwanth Karthikeya Settem – G01512992

// Vite configuration for the React frontend application, including the React plugin.


import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})