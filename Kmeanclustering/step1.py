import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x_mean = 1
y_mean = 3
n_data = 300
X = np.random.normal(loc=[x_mean, y_mean], scale=0.5, size=(n_data, 2))

fig, ax = plt.subplots(figsize=(7, 7))

ax.scatter(X[:, 0], X[:, 1])
ax.scatter(x_mean, y_mean,
           s=20,
           color='red')
ax.axvline(x=x_mean,
           linestyle=':',
           color='gray',
           linewidth=1)
ax.axhline(y=y_mean,
           linestyle=':',
           color='gray',
           linewidth=1)

plt.show()