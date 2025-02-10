# ワインの品質データ分析

UCIのワイン品質データセットを使用した分析プロジェクト。

## 引用
このデータセットを使用する場合は、以下の論文を引用してください：

### 論文の引用
P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
Modeling wine preferences by data mining from physicochemical properties.
In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

### データセットの引用
Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). 
Wine Quality [Dataset]. UCI Machine Learning Repository. 
https://doi.org/10.24432/C56S3T

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
