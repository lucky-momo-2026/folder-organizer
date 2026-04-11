# 📁 ファイル整理ツール（Python / CLI）

拡張子ごとにファイルを自動分類・整理するPythonツールです。  
dry-run（安全確認）機能とログ出力を備え、実務を想定して設計しています。

---

## 📋 機能一覧

- 拡張子を見てファイルを自動で仕分け（CSV・画像・PDF・その他）
- 同名ファイルがあっても上書きせず、連番で保存（例：`sample_1.csv`）
- 実行前に確認できる **dry-runモード**（ファイルを動かさず結果だけ表示）
- ファイル単体・フォルダ丸ごと、どちらにも対応
- 移動履歴を `log.txt` に記録

---

## 🗂️ ファイル構成

```
organize-files/
├── organize_files.py     # メインスクリプト
├── log.txt               # 出力：実行ログ（自動生成）
├── CSV/                  # 出力：.csv ファイルの移動先
├── 画像/                 # 出力：.png / .jpg / .jpeg の移動先
├── PDF/                  # 出力：.pdf ファイルの移動先
└── その他/               # 出力：上記以外の拡張子の移動先
```

---

## 📦 必要なライブラリ

標準ライブラリのみ使用のため、インストール不要です。

---

## 📂 移動先フォルダの対応表

| 拡張子 | 移動先フォルダ |
|--------|--------------|
| `.csv` | `CSV/` |
| `.png` `.jpg` `.jpeg` | `画像/` |
| `.pdf` | `PDF/` |
| それ以外 | `その他/` |

---

## 🚀 使い方

```bash
# 今いるフォルダを整理する
python organize_files.py

# 指定したフォルダを整理する
python organize_files.py C:\Users\YourName\Downloads

# dry-runモード（確認だけ・ファイルは動かない）
python organize_files.py --dry-run
python organize_files.py --dry-run C:\Users\YourName\Downloads

# ファイルを1つだけ整理する
python organize_files.py sample.csv
```

### 出力例（ターミナル）

```
画像 フォルダを作成しました
photo.jpg → 画像/photo.jpg に移動しました
report.pdf → PDF/report.pdf に移動しました
data.csv → CSV/data.csv に移動しました
notes.txt → その他/notes.txt に移動しました
```

dry-runのとき：

```
[DRY-RUN] photo.jpg → 画像/photo.jpg
[DRY-RUN] report.pdf → PDF/report.pdf
```

### ログの形式（log.txt）

```
[2025-04-11 10:30:00] photo.jpg → 画像/photo.jpg に移動しました
[2025-04-11 10:30:00] data.csv → CSV/data.csv に移動しました
[2025-04-11 10:30:00] [DRY-RUN] report.pdf → PDF/report.pdf
```

---

## ⚠️ 注意点

- `organize_files.py` 自身と `log.txt` は移動されません
- すでに存在するサブフォルダ（`CSV/` など）は移動対象外です
- ファイル名が重複する場合は自動で連番になります（`sample_1.csv`、`sample_2.csv` …）

---

## 🛠️ 開発環境

- Python 3.x

---

## 👤 作者

[lucky-momo-2026](https://github.com/lucky-momo-2026)