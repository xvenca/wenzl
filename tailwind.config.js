/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './layouts/**/*.html',
    './content/**/*.md',
    './assets/**/*.js'
  ],
  theme: {
    extend: {
      typography: ({ theme }) => ({
        stone: {
          css: {
            '--tw-prose-headings': theme('colors.amber[800]'),
            '--tw-prose-links': theme('colors.amber[700]'),
            '--tw-prose-bold': theme('colors.stone[900]'),
            '--tw-prose-hr': theme('colors.amber[200]'),
            '--tw-prose-quote-borders': theme('colors.amber[400]'),
          }
        },
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: theme('colors.stone[700]'),
            h1: { color: theme('colors.amber[800]'), fontWeight: '700' },
            h2: { color: theme('colors.amber[800]'), borderBottom: `1px solid ${theme('colors.amber[100]')}`, paddingBottom: '0.4em' },
            h3: { color: theme('colors.amber[700]') },
            h4: { color: theme('colors.amber[700]') },
            a: {
              color: theme('colors.amber[700]'),
              textDecoration: 'none',
              '&:hover': { textDecoration: 'underline', color: theme('colors.amber[900]') }
            },
            strong: { color: theme('colors.stone[900]') },
            blockquote: {
              borderLeftColor: theme('colors.amber[400]'),
              color: theme('colors.stone[600]'),
            },
            hr: { borderColor: theme('colors.amber[200]') },
          }
        }
      })
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
