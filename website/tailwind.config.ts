import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        'han': "var(--font-black-han-sans)",
        'lato': "var(--font-lato)",
      },
      colors: {
        'pink': "#F2C8D7",
        'teal': "#0A535E",
        'teal-hover': "#023F49",
        'crimson': "#AE003A",
        'crimson-hover': "#83022D",
      }
    },
  },
  plugins: [],
}
export default config
