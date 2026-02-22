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
        "site-bg":  "#B0E0E6",
        "card-bg":  "#E3D0BC",
        "forest":   "#1a3a3a",
        "accent":   "#A57C5C",
        "heading":  "#5E4B3C",
        "body":     "#6B5A4C",
      },
      fontFamily: {
        cormorant:  ['"Cormorant Garamond"', "serif"],
        montserrat: ["Montserrat", "sans-serif"],
      },
    },
  },
  plugins: [],
}
