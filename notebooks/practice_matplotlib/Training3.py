# 실습 3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

### data setting
names = ['DFF R-FCN', 'R-FCN', 'FGFA R-FCN']
dff_data = np.array([(0.581, 13.5),(0.598, 12.8),(0.618, 11.7),
           (0.62, 11.3), (0.624, 10.2), (0.627, 9.8),
           (0.629, 9.2), (0.63, 9)])
r_data = np.array([(0.565, 11.2), (0.645, 9)])
fgfa_data = np.array([(0.63, 8.8), (0.653, 9.3), (0.664, 9.6), (0.676, 10.1)])
dff_text = ['1:20', '1:15', '1:10', '1:8','1:5', '1:3', '1:2', '1:1']
r_text = ['Half Model', 'Full Model']
fgfa_text = ['1:1', '3:1', '7:1', '19:1']


### 그래프 세팅
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlabel('mAP',
              fontsize=20)
ax.set_ylabel('AD',
              fontsize=20)
ax.set_ylim([8.5, 14])
ax.set_xlim([0.56, 0.70])
xticks = list([i for i in np.arange(0.58, 0.69, 0.02)])
ax.set_xticks(xticks)

# 데이터 정렬 -> 튜플에서 빼내야 하는 문제?
dff_data.reshape(-1, 1)
r_data.reshape(-1, 1)
fgfa_data.reshape(-1, 1)

# dff
ax.scatter(dff_data[:, 0], dff_data[:, 1],
           marker='o',
           s=50,
           label=names[0])
for idx in range(len(dff_text)):
    data = dff_data[idx]
    ax.text(data[0]+0.002, data[1]+0.1,
            s=dff_text[idx],
            fontsize=12)

# r-fcn
ax.scatter(r_data[:, 0],r_data[:, 1],
           marker='^',
           s=50,
           facecolor='red',
           label=names[1])
for idx in range(len(r_text)):
    data = r_data[idx]
    ax.text(data[0]+0.005, data[1]-0.1,
            s=r_text[idx],
            va='top', ha='center',
            fontsize=12)

# fgfa r-fcn
ax.scatter(fgfa_data[:, 0], fgfa_data[:, 1],
           marker='*',
           facecolor='b',
           s=50,
           label=names[2])

for idx in range(len(fgfa_text)):
    data = fgfa_data[idx]
    ax.text(data[0], data[1]-0.1,
            s=fgfa_text[idx],
            va='top', ha='center',
            fontsize=12)

ax.legend(fontsize=20)
ax.grid(':',
        alpha=0.3)
plt.show()


ax.legend(fontsize=20)
ax.grid(':',
        alpha=0.3)
plt.show()



