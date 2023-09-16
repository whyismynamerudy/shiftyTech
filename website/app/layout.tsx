import './globals.css'
import type { Metadata } from 'next'
import { Lato, Black_Han_Sans } from 'next/font/google'

const lato = Lato({ weight: '400', subsets: ['latin'], variable: '--font-lato' })
const han = Black_Han_Sans({ weight: '400', subsets: ['latin'], variable: '--font-black-han-sans' })

export const metadata: Metadata = {
  title: 'Shifty Tech',
  description: 'Code with Dance',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${lato.variable} ${han.variable}`}>{children}</body>
    </html>
  )
}
