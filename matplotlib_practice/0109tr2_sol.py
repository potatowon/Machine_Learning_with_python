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


### customizing materials setting

colors = ['b', 'r', 'green']
markers = ['o', '^', '*']
markersizes = [400, 380, 500]

data_list = [dff_data, r_data, fgfa_data]
text_list = [dff_text, r_text, fgfa_text]
fig, ax = plt.subplots(figsize=(18, 15))

for data_idx, (data, text_arr) in enumerate(zip(data_list, text_list)):
    ### scatter plotting
    ax.scatter(data[:, 0], data[:, 1],
               s=markersizes[data_idx],
               c=colors[data_idx],
               label=names[data_idx],
               marker=markers[data_idx])

    for text_idx, text in enumerate(text_arr):
        ax.text(data[text_idx, 0] + 0.002, data[text_idx, 1],
                text,
                fontsize=25)

plt.show()