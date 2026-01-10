/** @type {import('next').NextConfig} */
const nextConfig = {
  // App Router使用
  reactStrictMode: true,

  // 本番デプロイ時は静的エクスポート
  output: process.env.NODE_ENV === 'production' ? 'export' : undefined,

  // 画像最適化（静的エクスポート時は無効化）
  images: {
    unoptimized: process.env.NODE_ENV === 'production',
  },

  // 開発時のAPIプロキシ設定
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
