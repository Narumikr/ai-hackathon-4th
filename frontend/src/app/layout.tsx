import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Historical Travel Agent',
  description: '歴史学習特化型旅行AIエージェント',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}
