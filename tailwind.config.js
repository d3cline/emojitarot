  /** @type {import('tailwindcss').Config} */

module.exports = {
    mode: 'jit',
    content: [
        './www/**/*.html',   // Matches all HTML files in the www directory and subdirectories
        './big3/www/**/*.html' // Matches all HTML files in the big3/www directory and subdirectories
    ],

    daisyui: {
        styled: true,
        themes: ["light", "dark"],
        base: true,
        utils: true,
        logs: true,
        rtl: false,
        prefix: "",
        darkTheme: "dark",
      },
    plugins: [
      require('@tailwindcss/typography'),
      require('daisyui'),
   ],
  }
  