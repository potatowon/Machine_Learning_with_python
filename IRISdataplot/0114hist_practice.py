import numpy as np
import matplotlib.pyplot as plt

### data setting
ex_name = ['Ritti Dataset', 'Apollo-SouthBay Dataset' ]
labels = ['ICP-PO2PO' , 'ICP-PO2PI', 'G-TCP','AA-ICP', 'NDT-P2d','CPD','3DFeat-Net','Ours']

kitti_data = [8.17, 2.92, 6.92, 5.24, 8.73, 0, 15.02, 2.3] #  3241.29,
kitti_data_y = [0, 0, 0, 0, 0, 3241.29, 0, 0]
kitti_text = [8.17, 2.92, 6.92, 5.24, 8.73, 3241.29, 15.02, 2.3]
apollo_data = [6.33, 1.69, 3.94, 4.25, 7.44, 0, 11.92, 2.07] # 2566.02]
apollo_data_y = [0, 0, 0, 0, 0, 2566.02, 0, 0]
apollo_text = [6.33, 1.69, 3.94, 4.25, 7.44, 2566.02, 11.92, 2.07]

xticks = np.arange(0.2, 0.2 + 8 , 1)
# yticks = ['0', '10', '100', '1000', '10000', '']
n_feacture = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(10, 7))
ax2 = ax.twinx()
# data 1
bar_width = 0.3
ax.set_ylim([0, 46])
ax.set_xticks(xticks)
ax.tick_params(bottom=False,
               left=False)
ax.bar(n_feacture-0.1, kitti_data, bar_width)
ax.bar(n_feacture+bar_width, apollo_data, bar_width)
ax.set_xticklabels(labels,
                   rotation=30,
                   fontsize=12)
ax.set_yticklabels(['0', '10', '100', '1000', '10000'],
                   fontsize=14)
# ax.set_yticklabels(yticks)



# data 2

ax2.set_ylim([0,4000])
# ax2.set_xticks(xticks)
ax2.bar(n_feacture-0.1, kitti_data_y, bar_width)
ax2.bar(n_feacture+ bar_width , apollo_data_y, bar_width )
ax2.get_yaxis().set_visible(False)

# ax.set_xticks(xticks)
# ax.set_xticklabels(labels)
# ax.set_yticks([1,10,100,1000,10000])


## text 표현

for idx, text in enumerate(kitti_text):
    ax.text(n_feacture[idx]-0.15, text+0.5,
            s=text,
            fontsize=12,
            rotation=90)
for idx, text in enumerate(apollo_text):
    ax.text(n_feacture[idx]+0.1, text+0.5,
            s=text,
            fontsize=12,
            rotation=90)

ax2.text(n_feacture[5] - 0.15, kitti_data_y[5]+0.5,
         s=kitti_data_y[5],
         fontsize=12,
         rotation=90)
ax2.text(n_feacture[5] + 0.1, apollo_data_y[5]+0.5,
         s=apollo_data_y[5],
         fontsize=12,
         rotation=90)

ax2.spines['top'].set_visible(False)
ax.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax.spines['right'].set_visible(False)


ax.grid(axis='y')
plt.show()