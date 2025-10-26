/** @type {import('tailwindcss').Config} */
export default {
  // CRUCIAL: Escanea archivos .vue y .js para generar el CSS
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}", 
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}