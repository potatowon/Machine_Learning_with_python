import matplotlib.pyplot as plt
import numpy as np


'''Legend'''

''' 1-1 for 문 이용해서 legned label '''

# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 300)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# for ax_idx in range(12):
#     label_template = 'added by {}'
#     ax.plot(t, sin+ax_idx,
#             label = label_template.format(ax_idx))
#
# ax.legend(fontsize=15)
# plt.show()

'''1-2 ncol Argument (legend의 열 개수 바꾸기)'''

# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 300)
# sin = np.sin(t)
#
# fig, axes = plt.subplots(1, 2, figsize=(10, 10))
#
# for ax_idx in range(12):
#     label_template = "added by {}"
#     axes[0].plot(t, sin+ax_idx,
#             label=label_template.format(ax_idx))
#     axes[1].plot(t, sin + ax_idx,
#                  label=label_template.format(ax_idx))
#
# axes[0].legend(fontsize=15,
#                bbox_to_anchor=(0,0),
#                loc='lower left',
#                ncol=3)
# axes[1].legend(fontsize=15,
#                ncol=1)
#
# plt.show()
'''1-3. bbox to anchor Argument(lengend lotaion)'''
    # (1,1) 정사각형 내에 좌표로서 legend의 위치를 지정할 수 있다.(legend 상자 기준점)

# n_data = 100
# random_noise1 = np.random.normal(0, 1, (n_data, ))
# random_noise2 = np.random.normal(1, 1, (n_data, ))
# random_noise3 = np.random.normal(2, 1, (n_data, ))
#
# fig, ax = plt.subplots(figsize=(10,7))
# ax.tick_params(labelsize=20)
#
# ax.plot(random_noise1,
#         label='random noise1')
# ax.plot(random_noise2,
#         label='random noise2')
# ax.plot(random_noise3,
#         label='random noise3')
#
# ax.legend(fontsize=20,
#           bbox_to_anchor=(0, 1),
#           loc='upper left')
# # 'best', 'upper right', 'upper left',
# # 'lower left', 'lower right', 'right',
# # 'center left', 'center right', 'lower center', 'upper center', 'center'
# plt.show()
'''1-4 bbox 그래프 밖으로 그리기'''
#
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 300)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# for ax_idx in range(12):
#     label_template = "added by {}"
#     ax.plot(t, sin+ax_idx,
#             label=label_template.format(ax_idx))
#
# ax.legend(fontsize=15,
#           ncol=4,
#           bbox_to_anchor=(0, -0.05),
#           loc='upper left')
#
# fig.tight_layout()
#
# plt.show()

'''1-5 line style을 적용하면 legend에도 반영이됨'''

# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 50)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(t, sin,
#         label='sin(t)')
#
# ax.plot(t, sin +1,
#         marker='o',
#         label='sin(t) +1',
#         linestyle=':')
#
# ax.plot(t, sin +2,
#         marker='D',
#         label='sin(t) +2',
#         linestyle='--')
#
# ax.plot(t, sin +3,
#         marker='s',
#         label='sin(t) +3',
#         linestyle='-.')
#
# ax.legend(bbox_to_anchor=(1, 0.5),
#            loc='center left',
#            fontsize=20)
#
# fig.tight_layout()
#
# plt.show()

'''1-6 클래스와 데이터'''
import matplotlib.cm as cm

# np.random.seed(0)
#
# n_class = 5
# n_data = 30
# center_pt = np.random.uniform(-20, 20, (n_class, 2)) # 균등분포 행렬 (5,2)로 생성
#
# cmap = cm.get_cmap('tab20')
# colors = [cmap(i) for i in range(n_class)]
#
# data_dict ={'class' + str(i) : None for i in range(n_class)} # dic comprehension : 데이터 초기화
# for class_idx in range(n_class):
#         center = center_pt[class_idx]
#         x_data = center[0] + 2 * np.random.normal(0, 1, (1, n_data)) # 1*30
#         y_data = center[1] + 2 * np.random.normal(0, 1, (1, n_data))
#         data = np.vstack((x_data,y_data))
#
#         data_dict['class' + str(class_idx)] = data
#
# fig, ax = plt.subplots(figsize=(12, 10))
# for class_idx in range(n_class):
#         data = data_dict['class' + str(class_idx)]
#         ax.scatter(data[0], data[1],
#                    s=1000,
#                    facecolor='None',
#                    edgecolor=colors[class_idx],
#                    linewidth=5,
#                    alpha=0.5,
#                    label='class'+str(class_idx))
# ax.legend(bbox_to_anchor=(1, 0.5),
#           loc='center left',
#           labelspacing=2,
#           fontsize=15,
#           ncol=2)
#
# fig.tight_layout()
# plt.show()
# print(center_pt)
# print(data_dict)

'''1-7. legend에 타이틀/배경색/테두리/열간격/ 행간격'''
# title=''
# title_fontsize=
# edgecolor=''
# facecolor
# labelspacing 행간격
# columnspacing : 열간격

np.random.seed(0)

n_data = 30
n_class = 5
center_pt = np.random.uniform(-20, 20, (n_class, 2))

cmap = cm.get_cmap('tab20')
colors = [cmap(i) for i in range(n_class)]

# 데이터 초기화
data_dic = {'class'+str(i) : None for i in range(n_class)}
# data dic 만들기
for class_idx in range(n_class):
    center = center_pt[class_idx]
    x_data = center[0] + 2*np.random.normal(0, 1, (1, n_data))
    y_data = center[1] + 2*np.random.normal(0, 1, (1, n_data))
    data = np.vstack((x_data, y_data))
    data_dic['class' + str(class_idx)] = data

# 그리기

fig, ax = plt.subplots(figsize=(12, 10))

for class_idx in range(n_class):
    data = data_dic['class'+str(class_idx)]
    ax.scatter(data[0], data[1],
               s=1000,
               facecolor='None',
               edgecolor=colors[class_idx],
               linewidth=5,
               alpha=0.5,
               label='class' + str(class_idx))

ax.legend(bbox_to_anchor=(1, 0.5),
          loc='center left',
          fontsize=15,
          ncol=2,
          title="Classes",
          title_fontsize=30,
          edgecolor='None',
          facecolor="None",
          labelspacing=3,
          columnspacing=1)

fig.tight_layout()
plt.show()

# scatter hatch='' -> 차원을 추가하는 의미로서 사용한다.
