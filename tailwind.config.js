/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./config/**/*.py",
    "./wgapps/**/*.py",
  ],
  theme: {
    /* Кастомные брейкпоинты. Заменяют дефолтные sm/md/lg/xl.
       Мобильный — всё что ниже 768px (без префикса).
       tab:  ≥ 768px
       pc:   ≥ 1280px                                            */
    screens: {
      "tab": "768px",
      "pc":  "1280px",
    },
    extend: {
      colors: {
        "site-bg":  "#e5d9ce",
        "card-bg":  "#f0e9e1",
        "forest":   "#1a3a3a",
        "accent":   "#b06060",
      },
      fontFamily: {
        cormorant:  ['"Cormorant Garamond"', "serif"],
        montserrat: ["Montserrat", "sans-serif"],
      },
    },
  },
  plugins: [],
}
