import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

means = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
std = [0.5, 0.4, 0.3, 0.2]
n_data = 100
data = []
for idx in range(len(means)):
    d = np.random.normal(loc=means[idx], scale=std[idx], size=(n_data, 2))
    data.append(d)

classes_k = 4
fig, axes = plt.subplots(2, 3,
                         figsize=(10, 7))
X = np.random.uniform(-2, 2, (classes_k, 1))
Y = np.random.uniform(-2, 2, (classes_k, 1))
center = np.hstack([X, Y])

for ax_idx, ax in enumerate(axes.flat):
    if ax_idx == 0:
        for idx in range(len(means)):

            ax.scatter(data[idx][:, 0], data[idx][:, 1],
                       color='steelblue',
                       alpha=0.5)
        ax.scatter(center[:, 0], center[:, 1],
                   color='red')
    elif ax_idx == 1:
        pred = [[] for _ in range(classes_k)]
        for idx in range(len(data)):
            for test in data[idx]:
                distance = np.sum((test - center)**2, axis=1)
                dist_argsort = np.argsort(distance)
                pred[dist_argsort[0]].append(test.tolist())


        for idx in range(len(pred)):
            pred_ = np.array(pred[idx])
            ax.scatter(pred_[:, 0], pred_[: , 1],
                       alpha=0.5)

        update_center = []
        for a in pred:
            avg = (np.sum(a, axis=0))/len(a)
            update_center.append(avg)


        for idx in range(len(update_center)):
            ax.scatter(update_center[idx][0], update_center[idx][1],
                    color='red')
    else:
        pred3 = [[] for _ in range(classes_k)]
        for idx in range(len(means)):
            for test in data[idx]:
                distance = np.sum((test - update_center)**2, axis=1)
                dist_argsort = np.argsort(distance)
                pred3[dist_argsort[0]].append(test.tolist())


        for idx in range(len(pred3)):
            pred3_ = np.array(pred3[idx])
            ax.scatter(pred3_[:, 0], pred3_[: , 1],
                       alpha=0.5)

        update_center = []
        for a in pred3:
            avg = (np.sum(a, axis=0))/len(a)
            update_center.append(avg)


        for idx in range(len(update_center)):
            ax.scatter(update_center[idx][0], update_center[idx][1],
                    color='red')



plt.show()