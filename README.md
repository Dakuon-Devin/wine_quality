# ワインの品質データ分析

UCIのワイン品質データセットを使用した分析プロジェクト。

## データ

データセットは[UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/186/wine+quality)から取得しています。

以下のデータファイルを使用しますが、Gitでは追跡しません：
- `data/winequality-red.csv` (82.2 KB)
- `data/winequality-white.csv` (258.2 KB)
- `data/winequality.names` (3.2 KB)

## 分析結果

分析結果は以下のディレクトリに保存されますが、Gitでは追跡しません：
- `results/figures/`: 分析で生成された可視化ファイル

## セットアップ

1. データのダウンロード:
```bash
python3 src/wine_quality/download_data.py
```

2. 分析の実行:
```bash
python3 src/wine_quality/run_analysis.py
```
