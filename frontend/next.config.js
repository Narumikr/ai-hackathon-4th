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

  // 開発環境でのAPIプロキシ設定（CORS回避）
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/:path*', // /api プレフィックスを除去してプロキシ
      },
    ];
  },
};

module.exports = nextConfig;
