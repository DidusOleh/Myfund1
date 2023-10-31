/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./core/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'crimson': ['Crimson Text', 'serif'],
        'staatliches': ['Staatliches', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

