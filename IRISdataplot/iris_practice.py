import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

feature_names = iris.feature_names
n_features = len(feature_names)
species = iris.target_names
n_species = len(species)

iris_X, iris_y = iris.data, iris.target
X_setosa, X_versicolor, X_virginica = iris_X[ iris_y ==0 ], iris_X[ iris_y == 1], iris_X[iris_y==2]

fig, axes = plt.subplots(n_features, n_features,
                         figsize=(10, 10))
                         # sharex='col',
                         # sharey='row')
# for row_idx in range(4):
#     row_axes = axes[row_idx][:]
#     for ax_idx, ax in enumerate(row_axes):
# axes[0][0].hist(iris_X[:,0])

for i in range(n_features):
    for j in range(n_features):
        if i == j :
            axes[i][j].hist(iris_X[:, i],
                            rwidth=0.7)
        else:
            axes[i][j].scatter(X_setosa[: , j], X_setosa[:, i],
                               color='purple',
                               alpha=0.5,
                               s=30)
            axes[i][j].scatter(X_versicolor[: , j], X_versicolor[:, i],
                               color='darkcyan',
                               alpha=0.5,
                               s=30)
            axes[i][j].scatter(X_virginica[: , j], X_virginica[:, i],
                               color='gold',
                               alpha=0.5,
                               s=30)
            axes[i][j].grid()
# aixs label

for i in range(n_features):
    axes[i][0].set_ylabel(feature_names[i], fontsize=15)
    axes[3][i].set_xlabel(feature_names[i], fontsize=15)



plt.show()

