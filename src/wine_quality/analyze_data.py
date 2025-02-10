import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib
from pathlib import Path

# 高品質な出力設定
plt.rcParams['figure.dpi'] = 300
plt.style.use('default')
sns.set_palette("viridis")

def setup_output_directory():
    """結果保存用ディレクトリの設定"""
    results_dir = Path(__file__).parent.parent.parent / 'results' / 'figures'
    results_dir.mkdir(parents=True, exist_ok=True)
    return results_dir

def analyze_basic_stats(red_wine: pd.DataFrame, white_wine: pd.DataFrame, results_dir: Path):
    """基本統計量の分析と可視化"""
    # 基本統計量の計算
    red_stats = red_wine.describe()
    white_stats = white_wine.describe()
    
    # 各特徴量のボックスプロット
    for feature in red_wine.columns[:-1]:  # quality以外の特徴量
        plt.figure(figsize=(10, 6))
        data = [
            red_wine[feature],
            white_wine[feature]
        ]
        plt.boxplot(data)
        plt.xticks([1, 2], ['赤ワイン', '白ワイン'])
        plt.title(f'{feature}の分布比較')
        plt.ylabel(feature)
        plt.savefig(results_dir / f'boxplot_{feature}.png', bbox_inches='tight')
        plt.close()

def analyze_quality_distribution(red_wine: pd.DataFrame, white_wine: pd.DataFrame, results_dir: Path):
    """品質スコアの分布分析"""
    plt.figure(figsize=(12, 6))
    
    # 品質スコアの分布
    plt.subplot(1, 2, 1)
    sns.histplot(data=red_wine, x='quality', bins=10)
    plt.title('赤ワインの品質分布')
    plt.xlabel('品質スコア')
    plt.ylabel('頻度')
    
    plt.subplot(1, 2, 2)
    sns.histplot(data=white_wine, x='quality', bins=10)
    plt.title('白ワインの品質分布')
    plt.xlabel('品質スコア')
    plt.ylabel('頻度')
    
    plt.tight_layout()
    plt.savefig(results_dir / 'quality_distribution.png', bbox_inches='tight')
    plt.close()

def analyze_correlations(red_wine: pd.DataFrame, white_wine: pd.DataFrame, results_dir: Path):
    """特徴量間の相関分析"""
    # 赤ワインの相関マトリックス
    plt.figure(figsize=(12, 10))
    sns.heatmap(red_wine.corr(), annot=True, cmap='viridis', fmt='.2f')
    plt.title('赤ワインの相関マトリックス')
    plt.savefig(results_dir / 'red_wine_correlation.png', bbox_inches='tight')
    plt.close()
    
    # 白ワインの相関マトリックス
    plt.figure(figsize=(12, 10))
    sns.heatmap(white_wine.corr(), annot=True, cmap='viridis', fmt='.2f')
    plt.title('白ワインの相関マトリックス')
    plt.savefig(results_dir / 'white_wine_correlation.png', bbox_inches='tight')
    plt.close()

def analyze_feature_importance(red_wine: pd.DataFrame, white_wine: pd.DataFrame, results_dir: Path):
    """品質に影響を与える特徴量の分析"""
    # 品質との相関係数を計算
    red_correlations = red_wine.corr()['quality'].sort_values(ascending=False)
    white_correlations = white_wine.corr()['quality'].sort_values(ascending=False)
    
    # 相関係数の可視化
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    red_correlations[1:].plot(kind='bar')  # quality自身を除外
    plt.title('赤ワイン: 品質との相関係数')
    plt.xticks(rotation=45)
    plt.ylabel('相関係数')
    
    plt.subplot(1, 2, 2)
    white_correlations[1:].plot(kind='bar')  # quality自身を除外
    plt.title('白ワイン: 品質との相関係数')
    plt.xticks(rotation=45)
    plt.ylabel('相関係数')
    
    plt.tight_layout()
    plt.savefig(results_dir / 'quality_correlations.png', bbox_inches='tight')
    plt.close()

def analyze_wine_quality():
    """ワインの品質データ分析メイン関数"""
    # データ読み込み
    red_wine = pd.read_csv('data/winequality-red.csv', sep=';')
    white_wine = pd.read_csv('data/winequality-white.csv', sep=';')
    
    # 結果保存用ディレクトリの設定
    results_dir = setup_output_directory()
    
    # 各分析の実行
    analyze_basic_stats(red_wine, white_wine, results_dir)
    analyze_quality_distribution(red_wine, white_wine, results_dir)
    analyze_correlations(red_wine, white_wine, results_dir)
    analyze_feature_importance(red_wine, white_wine, results_dir)

if __name__ == '__main__':
    analyze_wine_quality()
