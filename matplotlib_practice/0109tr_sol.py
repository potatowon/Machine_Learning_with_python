import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

np.random.seed(8)

n_data = 20
n_point = 200
scale = 3

x_mean_list = np.random.randint(-60, 60, n_data)
y_mean_list = np.random.randint(-80, 80, n_data)

cmap = cm.get_cmap('rainbow', lut=n_data)

fig, ax = plt.subplots(figsize=(15, 15))

for data_idx in range(n_data):
    x_data = np.random.normal(loc=x_mean_list[data_idx], scale=scale, size=(1, n_point))
    y_data = np.random.normal(loc=y_mean_list[data_idx], scale=scale, size=(1, n_point))

    ax.scatter(x_data, y_data,
               color=cmap(data_idx),
               alpha=0.5)

ax.tick_params(axis='both',
               labelsize=20,
               length=8,
               width=3)

plt.show()