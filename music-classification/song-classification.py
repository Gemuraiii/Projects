import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA


tracks = pd.read_csv("C:\Users\Glen F\Documents\Projects\music-classification\fma-rock-vs-hiphop.csv")
echonest_metrics = pd.read_json("C:\Users\Glen F\Documents\Projects\music-classification\echonest-metrics.json")

echo_tracks = echonest_metrics.merge(tracks[['track_id', 'genre_top']],  on= 'track_id')
echo_tracks.info()

corr_metrics = echo_tracks.corr()
corr_metrics.style.background_gradient()

features = echo_tracks.drop(['genre_top', 'track_id'], axis = 1)
labels = echo_tracks[['genre_top']]

scaler = StandardScaler()
scaled_train_features = scaler.fit_transform(features)

pca = PCA()
pca.fit(scaled_train_features)
exp_variance = pca.explained_variance_ratio_

fig, ax = plt.subplots()
ax.bar(range(pca.n_components_, exp_variance)
ax.set_xlabel('Principal Component #')

np.cumsum(exp_variance)
fig,ax = plt.subplots()
ax.plot()