# Python

## ツールチェーン

以下のツールを標準として使用すること。

| 種類 | ツール | 選定理由 |
|------|--------|----------|
| パッケージ/ライブラリ管理 | uv | pip互換で処理が速い |
| 型チェック | pyright | VSCodeのPython拡張機能と同一のため、エディタとCLI/CI/CDで結果が統一される。追加プラグイン不要 |
| Linter / Formatter / Import sorter | ruff | 処理が速い。lint/format/importを1ツールで対応でき、依存を最小化できる |
| テストランナー | pytest | 標準のunittestより機能が豊富 |

pip / pip3 コマンドは使用せず、uv を使用すること