import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

athletes = [[2.50, 6.00, 'no'],
            [3.75, 8.00, 'no'],
            [2.25, 5.50, 'no'],
            [3.25, 8.25, 'no'],
            [2.75, 7.25, 'no'],
            [4.50, 5.00, 'no'],
            [3.50, 5.25, 'no'],
            [3.00, 3.25, 'no'],
            [4.00, 4.00, 'no'],
            [4.25, 3.75, 'no'],
            [2.00, 2.00, 'no'],
            [5.00, 2.50, 'no'],
            [8.25, 8.50, 'no'],
            [5.75, 8.75, 'yes'],
            [4.75, 6.25, 'yes'],
            [5.50, 6.75, 'yes'],
            [5.25, 9.50, 'yes'],
            [7.00, 4.25, 'yes'],
            [7.50, 8.00, 'yes'],
            [7.25, 5.75, 'yes']]

athletes_df = pd.DataFrame(athletes,
                           columns=['SPEED', 'AGILITY', 'DRAFT'])


X = athletes_df[['SPEED', 'AGILITY']].to_numpy()

y = athletes_df['DRAFT'].values

fig, ax = plt.subplots(figsize=(10, 10))

X_pos, X_neg = X[y == 'yes'], X[y == 'no']
print(X_pos)
print(X_neg)
ax.scatter(X_pos[:, 0], X_pos[:, 1], color='blue',
           marker='+', s=130, label='yes')
ax.scatter(X_neg[:, 0], X_neg[:, 1], color='red',
           marker='^', s=100, label='no')
ax.set_xlabel("Speed", fontsize=20)
ax.set_ylabel("AGILITY", fontsize=20)
ax.legend(fontsize=15)
ax.tick_params(labelsize=15)


K=3
# test data (Speed :6.75, Agility:3.00)
test_data = [6.75, 3.00]
distances = X - test_data
distances = np.array(np.sqrt(distances[:,0]**2)+np.sqrt(distances[:,1]**2))

dists_sort = np.argsort(distances) # 정렬하는 어레이의 인덱스의 반환
sorted_labels = np.array(y[dists_sort[:]])
k_nearest_label= sorted_labels[:K]

# 라벨 찾기
label_ = ['yes', 'no']
count_dic = {'yes': 0, 'no': 0}

for label in k_nearest_label:
    count_dic[label] += 1

count_label = np.array(list(count_dic.values()))
pred_label = label_[count_label.argmax()]

# 좌표 찾기
nearest_data = []

for idx in dists_sort[:K]:
    x_data = X[idx, 0]
    y_data = X[idx, 1]
    nearest_data.append([x_data,y_data])

# 그리기
if pred_label == 'yes':
    marker='+'
    color='blue'
    name='yes'
elif pred_label == 'no':
    marker='^'
    color='red'
    name='no'

ax.scatter(test_data[0], test_data[1],
           color=color,
           marker=marker,
           s=100)
for i in range(len(nearest_data)):
    ax.plot([test_data[0], nearest_data[i][0]],[test_data[1], nearest_data[i][1]],
            ':',
            color='deeppink')

ax.text(test_data[0]+0.1, test_data[1]+0.1,
        name,
        fontsize=25,
        color='deeppink')

# mesh grid그리기

x1_lim , x2_lim = ax.get_xlim(), ax.get_ylim()
x_lin = np.linspace(x1_lim[0], x1_lim[1], 100)
y_lin = np.linspace(x2_lim[0], x2_lim[1], 100)

x1, y1= np.meshgrid(x_lin, y_lin)
x_mesh = np.reshape(x1, (-1, ))
y_mesh = np.reshape(y1, (-1, ))



colors = []
# dist_dic = {idx : None for idx in range(len(x_mesh))}
for idx in range(len(x_mesh)):
    mesh_data = [x_mesh[idx], y_mesh[idx]]
    mesh_dists = X - mesh_data
    mesh_dists = np.array(np.sqrt(mesh_dists[:,0]**2)+np.sqrt(mesh_dists[:,1]**2))
    mesh_dists_sort = np.argsort(mesh_dists)
    sorted_mesh_labels = np.array(y[mesh_dists_sort[:]])
    k_nearest_mesh_label = sorted_mesh_labels[:K]
    label_ = ['yes', 'no']
    count_dic = {'yes': 0, 'no': 0}
    for label in k_nearest_mesh_label:
        count_dic[label] += 1
    count_label = np.array(list(count_dic.values()))
    pred_label = label_[count_label.argmax()]
    if pred_label == 'yes':
        color = 'blue'
    elif pred_label == 'no':
        color = 'red'
    colors.append(color)
ax.scatter(x_mesh, y_mesh,
           alpha=0.2,
           color=colors,
           s=10)

plt.show()