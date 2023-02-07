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

data_stack = np.vstack([data[i] for i in range(len(data))])
print(len(data_stack))
classes_k = 4
fig, axes = plt.subplots(2, 3,
                         figsize=(10, 7))
dataset = data_stack
np.random.shuffle(dataset)
X = dataset[:, 0]
Y = dataset[:, 1]

X = X[:classes_k]
Y = Y[:classes_k]

center = np.hstack([X.reshape(classes_k, -1),Y.reshape(classes_k, -1)])



for ax_idx, ax in enumerate(axes.flat):
    if ax_idx == 0:
        for idx in range(len(means)):

            ax.scatter(data[idx][:, 0], data[idx][:, 1],
                       color='steelblue',
                       alpha=0.5)
        ax.scatter(center[:, 0], center[:, 1],
                   s=50,
                   color='red')
    elif ax_idx == 1:
        pred = [[] for _ in range(classes_k)]
        for idx in range(len(data_stack)):
            distance = np.sum((data_stack[idx] - center) ** 2, axis=1)
            dist_argsort = np.argsort(distance)
            pred[dist_argsort[0]].append(data_stack[idx].tolist())



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
                    color='red',
                       s=50)
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
                    color='red',
                       s=50)



plt.show()