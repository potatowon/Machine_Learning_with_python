import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

means = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
std = [0.5, 0.4, 0.3, 0.2]
n_clustersmaple = 300
fig, ax = plt.subplots(figsize=(7, 7))
# X = np.random.uniform(-2, 2, (4, 1))
# Y = np.random.uniform(-2, 2, (4, 1))
# center = np.hstack([X, Y])
K = 4
data = []
for idx in range(len(means)):
    cluster_data = np.random.normal(loc=means[idx], scale=std[idx], size=(n_clustersmaple, 2))
    data.append(cluster_data)

data = np.vstack(data)

# 데이터 내에서 임의의 K 개의 점을 뽑아 centroid 만들기
n_data = data.shape[0]

random_idx = np.arange(n_data)
np.random.shuffle(random_idx)
centroid_idx = random_idx[:K]
centroids = data[centroid_idx]

ax.scatter(data[:, 0], data[:, 1],
           color='steelblue',
           alpha=0.5)
ax.scatter(centroids[:,0], centroids[:, 1],
           color='red',
           s=50)



ax.axvline(x=0,
           linestyle=':',
           color='gray',
           linewidth=1)
ax.axhline(y=0,
           linestyle=':',
           color='gray',
           linewidth=1)

plt.show()


