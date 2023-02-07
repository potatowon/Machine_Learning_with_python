import numpy as np
import matplotlib.pyplot as plt

from Yang_utils import get_dataset
from Yang_utils import get_initial_centroids
from Yang_utils import clustering
from Yang_utils import update_centroids


K = 4
dataset = get_dataset()
centroids = get_initial_centroids(dataset, K)

fig, axes = plt.subplots(2, 3, figsize=(10, 6))
axes[0, 0].scatter(dataset[:, 0], dataset[:, 1], alpha=0.7)
axes[0, 0].scatter(centroids[:, 0], centroids[:, 1], color='r', s=50)

for ax in axes.flat[1:]:  #axes.flatten()[1:]
    clusters = clustering(dataset, centroids, K)
    centroids = update_centroids(clusters)

    for cluster_idx in range(K):
        cluster = clusters[cluster_idx]
        ax.scatter(cluster[:, 0], cluster[:, 1], alpha=0.3)
        ax.scatter(centroids[:, 0], centroids[:, 1], color='r')

plt.show()