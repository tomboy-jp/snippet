"""
sklearn関連
"""
# 教師あり回帰/線形モデル
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

# 教師あり分類/線形モデル
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

# 教師あり分類/決定木モデル
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import xgboost as xgb

# 教師あり分類/ニューラルネットワーク
from sklearn.neural_network import MLPClassifier

# 教師なし分類
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# データ作成
from sklearn.datasets import make_regression
from sklearn.datasets import make_classification
from sklearn.datasets import make_gaussian_quantiles
from sklearn.datasets import make_blobs

# テストデータ
from sklearn.datasets import load_iris
from sklearn.datasets import load_boston
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits
from sklearn.datasets import load_linnerud

# データ分割
from sklearn.model_selection import train_test_split

# 特徴量エンジニアリング
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler

# 自然言語処理
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# グリッドサーチとパイプ
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

# 結果を確認する
from sklearn.metrics import classification_report
