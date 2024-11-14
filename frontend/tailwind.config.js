/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,css,scss,html}",
    "../exemple/**/templates/**/*.{js,css,scss,html}",
    "../components/**/*.{js,css,scss,html}",
    "../.venv/**/crispy_tailwind/**/*.{js,css,scss,html}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
    require('flowbite/plugin'),
  ],
}

