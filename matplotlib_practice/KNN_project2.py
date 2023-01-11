import random

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(8)
n_data = 100
tr_data = int(n_data*0.8)
ts_data = int(n_data*0.2)
K=5

x_data = np.random.normal(0, 1, (1, 100))
y_data = x_data + 0.2*np.random.normal(1, 1, (1, 100))

train_xdata = x_data[:, :tr_data]
test_xdata = x_data[:, tr_data:]


train_ydata = train_xdata + 0.2*np.random.normal(0, 1, (1, tr_data))
test_ydata = test_xdata + 0.2*np.random.normal(0, 1, (1, ts_data))
y = train_ydata.reshape(-1, 1)


train_data_set = np.hstack([train_xdata.reshape(-1, 1), train_ydata.reshape(-1, 1)])
test_data_set = np.hstack([test_xdata.reshape(-1, 1), test_ydata.reshape(-1, 1)])

# print(test_data_set)
preds = []
clss_list = []
for test in test_data_set:
    e_dist = abs((train_data_set[:, 0] - test[0]))
    # print(e_dist)
    dist_argsort = np.argsort(e_dist)
    cloes_K_indices = dist_argsort[:K]
    cloes_classes = y[cloes_K_indices]
    # print(cloes_classes)
    class_ = sum(cloes_classes)/len(cloes_classes)
    # print(sum(cloes_classes))
    # print(len(cloes_classes))
    xx = test[0]
    yy = float(class_)
    preds.append([xx, yy])
preds_np = np.array(preds)

fig, ax = plt.subplots(figsize=(7, 7))

ax.scatter(test_xdata, test_ydata,
           alpha=0.5,
           color='orange',
           label='test dataset')
ax.scatter(train_xdata, train_ydata,
           alpha=0.5,
           label='train dataset')
ax.scatter(preds_np[:, 0], preds_np[:, 1],
           color='red')


plt.show()