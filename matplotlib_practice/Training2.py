# 실습 2
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

np.random.seed(8)
n_data = 20
data_dic = {'class'+str(idx) : None for idx in range(n_data)}
for i in range(n_data):
    x_data = np.random.normal(np.random.uniform(-60, 60), 2, (100, ))
    y_data = np.random.normal(np.random.uniform(-60, 60), 2, (100, ))
    data = np.vstack((x_data, y_data))
    data_dic['class'+str(i)] = data

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xlim([-65, 65])
ax.set_ylim([-65, 65])
for data_idx in range(n_data):
    data = data_dic['class'+str(data_idx)]
    ax.scatter(data[0], data[1],
               marker='.',
               s=15,
               alpha=0.5)
plt.show()