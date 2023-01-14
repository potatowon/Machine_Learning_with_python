import numpy as np
import matplotlib.pyplot as plt


"""1. ax.biolinplot"""
#
# np.random.seed(0)
#
# fig, ax = plt.subplots(figsize=(7, 7))
#
# data1 = np.random.normal(0, 1, 100)
# data2 = np.random.normal(5, 2, 200)
# data3 = np.random.normal(13, 3, 300)
#
# xticks = np.arange(3)
# # xticks = [1, 5, 6]
#
# ax.violinplot([data1, data2, data3], positions=xticks)
#
# ax.set_xticks(xticks)
# ax.set_xticklabels(['setosa', 'versicolor', 'cirginica'])
# ax.set_xlabel('Species', fontsize=15)
# ax.set_ylabel('Values', fontsize=15)
#
# plt.show()


''' 2. 각 데이터의 평균값 표시하기'''
#
# np.random.seed(0)
#
# fig, ax= plt.subplots(figsize=(7, 7))
#
# data1 = np.random.normal(0, 1, 100)
# data2 = np.random.normal(5, 2, 200)
# data3 = np.random.normal(13, 3, 300)
#
# xticks = np.arange(3)
#
# ax.violinplot([data1, data2, data3],
#               positions=xticks,
#               showmedians=True)
#               # showextrema=True)
#
#               # showmeans=True)
#
# ax.set_xticks(xticks)
# ax.set_xticklabels(['setosa', 'versicolor', 'virginica'])
# ax.set_xlabel('Species', fontsize=15)
# ax.set_ylabel('Values', fontsize=15)
#
# plt.show()

''' 3. 4분위 표시하기'''


# np.random.seed(0)
#
# fig, ax = plt.subplots(figsize=(7, 7))
#
# data1 = np.random.normal(0, 1, 100)
# data2 = np.random.normal(5, 2, 200)
# data3 = np.random.normal(13, 3, 300)
#
# xticks = np.arange(3)
# # xticks = [1, 5, 6]
#
# ax.violinplot([data1, data2, data3], positions=xticks,
#               quantiles=[[0.25, 0.75], [0.1, 0.9], [0.3, 0.7]])
#
# ax.set_xticks(xticks)
# ax.set_xticklabels(['setosa', 'versicolor', 'cirginica'])
# ax.set_xlabel('Species', fontsize=15)
# ax.set_ylabel('Values', fontsize=15)
#
# plt.show()

''' 4. 색상변경하기 등'''

np.random.seed(0)

fig, ax = plt.subplots(figsize=(7, 7))

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 2, 200)
data3 = np.random.normal(13, 3, 300)

xticks = np.arange(3)
# xticks = [1, 5, 6]

violin = ax.violinplot([data1, data2, data3],
                       positions=xticks,
                       quantiles=[[0.25, 0.75], [0.1, 0.9], [0.3, 0.7]])
                       # showmedians=True)
                       # showmeans=True)

ax.set_xticks(xticks)
ax.set_xticklabels(['setosa', 'versicolor', 'cirginica'])
ax.set_xlabel('Species', fontsize=15)
ax.set_ylabel('Values', fontsize=15)

violin['bodies'][0].set_facecolor('blue')

violin['cbars'].set_edgecolor('red') # 가운데 선
violin['cmaxes'].set_edgecolor('orange') # 위쪽라인 선
violin['cmins'].set_edgecolor('green') # 아래 라인 선
# violin['cmeans'].set_edgecolor('red') # 평균선
# violin['cmedians'].set_edgecolor('deeppink') # 중앙값선
violin['cquantiles'].set_edgecolor('red') # 사분위 선


plt.show()