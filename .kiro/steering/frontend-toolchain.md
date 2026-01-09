# フロントエンド (TypeScript/JavaScript)

## ツールチェーン

以下のツールを標準として使用すること。

| 種類 | ツール | 選定理由 |
|------|--------|----------|
| フレームワーク | Next.js 16 | React-based、App Router、静的サイト生成対応 |
| パッケージ/ライブラリ管理 | pnpm | 高速でディスク効率が良い。npm/yarn互換 |
| 型チェック | TypeScript (tsc) | 言語標準の型チェッカー |
| Linter / Formatter / Import sorter | Biome | 高速（Rustベース）。lint/format/importを1ツールで対応でき、依存を最小化できる |
| テストランナー | Vitest | Jest互換API、高速 |

npm / yarn コマンドは使用せず、pnpm を使用すること