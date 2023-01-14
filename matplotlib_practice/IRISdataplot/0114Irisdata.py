import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

feature_names = iris.feature_names
n_features = len(feature_names)
species = iris.target_names
n_species = len(species)

iris_X, iris_y = iris.data, iris.target

fig, axes = plt.subplots(2, 2,
                       figsize=(7, 7))
                       # sharex=True)

xticks = np.arange(3)
xtick_labels = species

# axes.set_xticks(xticks)
# axes.set_xticklabels(xtick_labels)
ax_title = feature_names
X_setosa, X_versicolor, X_virginica = iris_X[ iris_y ==0 ], iris_X[ iris_y == 1], iris_X[iris_y==2]
# print(X_setosa[:,0])

for ax_idx, ax in enumerate(axes.flat):
    ax.violinplot([X_setosa[:, ax_idx],
                   X_versicolor[:, ax_idx],
                   X_virginica[:, ax_idx]],
                  positions=xticks)
    ax.set_xticks(xticks)
    # ax.xaxis.set_ticklabels(which='both',
    #                         labelbottom=True)
    ax.get_xaxis().set_visible(True)
    ax.set_xticklabels(xtick_labels, fontsize=14)
    ax.set_title(ax_title[ax_idx])


plt.tight_layout()
plt.show()

