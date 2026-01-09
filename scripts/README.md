# GitHub ProjectへのIssue追加

このディレクトリには、リポジトリ内の全てのIssueをGitHub Projectに追加するためのツールが含まれています。

## 方法1: 手動スクリプトを使用する（推奨）

### 前提条件

- [GitHub CLI](https://cli.github.com/)がインストールされていること
- GitHubにログインしていること（`gh auth login`）

### 使用方法

```bash
./scripts/add-issues-to-project.sh <project_number> <owner_type>
```

#### 引数

- `project_number`: プロジェクト番号（例: 1）
- `owner_type`: プロジェクトのオーナータイプ
  - `user`: ユーザープロジェクトの場合
  - `org`: 組織プロジェクトの場合

#### 例

```bash
# ユーザープロジェクト（プロジェクト番号1）に追加
./scripts/add-issues-to-project.sh 1 user

# 組織プロジェクト（プロジェクト番号1）に追加
./scripts/add-issues-to-project.sh 1 org
```

### スクリプトの動作

1. 指定されたプロジェクトのIDを取得
2. リポジトリ内の全てのIssue（PRを除く）を取得
3. 各IssueをProjectに追加
4. 結果を表示

## 方法2: GitHub Actionsワークフローを使用する

### 新しいIssueを自動的に追加

新しいIssueが作成されると、自動的に指定されたプロジェクトに追加されます。

### 既存の全てのIssueを追加

1. GitHubリポジトリのページで「Actions」タブに移動
2. 「Add Issues to AI Hackathon 4th Project」ワークフローを選択
3. 「Run workflow」ボタンをクリック
4. プロジェクト番号とオーナータイプを入力
5. 「Run workflow」を実行

### ワークフローの設定

ワークフローファイル（`.github/workflows/add-issues-to-project.yml`）内のプロジェクトURLを適切に設定してください：

```yaml
# ユーザープロジェクトの場合
project-url: https://github.com/users/Narumikr/projects/1

# 組織プロジェクトの場合
project-url: https://github.com/orgs/Narumikr/projects/1
```

## プロジェクト番号の確認方法

1. GitHubでプロジェクトを開く
2. URLを確認する
   - ユーザープロジェクト: `https://github.com/users/USERNAME/projects/NUMBER`
   - 組織プロジェクト: `https://github.com/orgs/ORGNAME/projects/NUMBER`
3. URLの最後の数字がプロジェクト番号です

## トラブルシューティング

### エラー: プロジェクトが見つかりません

- プロジェクト番号が正しいか確認してください
- オーナータイプ（user/org）が正しいか確認してください
- プロジェクトが存在し、アクセス権限があることを確認してください

### エラー: 認証エラー

- GitHub CLIでログインしているか確認してください（`gh auth status`）
- 必要に応じて再ログインしてください（`gh auth login`）

### すでに追加されているIssue

スクリプトは既にプロジェクトに追加されているIssueをスキップします。エラーにはなりません。
