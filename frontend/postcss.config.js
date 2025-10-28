// frontend/postcss.config.js
export default {
  plugins: {
    '@tailwindcss/postcss': {}, // <-- ¡Esta es la corrección!
    autoprefixer: {},
  },
};