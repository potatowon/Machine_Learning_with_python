import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

means = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
std = [0.5, 0.4, 0.3, 0.2]
n_data = 300
fig, ax = plt.subplots(figsize=(7, 7))
X = np.random.normal(0, 1, (4, 1))
Y = np.random.normal(0, 1, (4, 1))

center = np.hstack([X.reshape(4, -1), Y.reshape(4, -1)])
print(center)
print(center[:, 0])
print(center[:, 1])

for idx in range(len(means)):
    data = np.random.normal(loc=means[idx], scale=std[idx], size=(n_data, 2))
    ax.scatter(data[:, 0], data[:, 1],
               color='steelblue',
               alpha=0.5)
ax.scatter(center[:, 0], center[:, 1],
           color='red')

ax.axvline(x=0,
           linestyle=':',
           color='gray',
           linewidth=1)
ax.axhline(y=0,
           linestyle=':',
           color='gray',
           linewidth=1)

plt.show()