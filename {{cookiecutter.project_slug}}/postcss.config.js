const tailwindcss = require('tailwindcss')

module.exports = {
  plugins: [
    tailwindcss('./{{ cookiecutter.project_slug }}/src/css/tailwind.config.js'),
    require('autoprefixer')
  ]
}
