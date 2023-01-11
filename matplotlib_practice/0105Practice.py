import numpy as np
import matplotlib.pyplot as plt


# 1번 ax.plot(y)
# 1-1
'''
np.random.seed(0)

y_data = np.random.normal(loc=0, scale=1, size=(300, ))
# loc 평균, scale 표준편차, size 크기 : 변수명을 지정하는 경우 순서 무관
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(y_data) # x_data는 0 부터 300까지 자동으로 산정

fig.tight_layout(pad=3)
ax.tick_params(labelsize=25)

plt.show()
'''
# 1-2 x_tick
'''
np.random.seed()

y_data = np.random.normal(loc=0, scale=1, size=(300, ))

fig, ax = plt.subplots(figsize=(10,5))

fig.tight_layout(pad=3)
ax.tick_params(labelsize=25)

x_ticks = np.arange(301, step=50)
ax.set_xticks(x_ticks)

plt.show()
'''

# 1-3
'''
np.random.seed(0)

n_data = 100
s_idx = 30
x_data = np.arange(s_idx, s_idx+n_data)
y_data = np.random.normal(0, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_data, y_data)

fig.tight_layout(pad=3)
x_ticks = np.arange(s_idx, s_idx + n_data + 1, 20)
ax.set_xticks(x_ticks)

ax.tick_params(labelsize=25)
ax.grid()

plt.show()
'''

# 1 -4

# np.random.seed(0)
#
# x_data = np.array([10, 25, 31, 40, 55, 80, 100])
# y_data = np.random.normal(0, 1, (7, ))
#
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(x_data, y_data)
#
# fig.subplots_adjust(left=0.2)
# -------------------------------------------
#
# ylim = ax.get_ylim() # y값의 최소 최대값
# print(ylim)
# yticks = np.linspace(ylim[0], ylim[1], 8)
# ax.set_yticks(yticks)
#
# ax.grid()
#
# plt.show()

'''1-5 x, y normal 값 그리기'''

# np.random.seed(0)
#
# x_data = np.random.normal(0, 1, (10, ))
# y_data = np.random.normal(0, 1, (10, ))
#
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(x_data, y_data) # 'o' , '^', '--' 등의 마커 변경 가능
#
# plt.show()

'''1-6 Nomal 평균 값 차이 '''
#
# n_data = 100
#
# random_noise1 = np.random.normal(0, 1, (n_data, ))
# random_noise2 = np.random.normal(1, 1, (n_data, ))
# random_noise3 = np.random.normal(2, 1, (n_data, ))
#
# fig, ax = plt.subplots(figsize=(10, 7))
#
# ax.plot(random_noise1)
# ax.plot(random_noise2)
# ax.plot(random_noise3)
#
# ax.tick_params(labelsize=20)
#
# plt.show()

'''1-7 data 개수의 차이 '''

# n_data1, n_data2, n_data3 = 200, 50 , 10
#
# x_data1 = np.linspace(0, 200, n_data1)
# x_data2 = np.linspace(0, 200, n_data2)
# x_data3 = np.linspace(0, 200, n_data3)
#
# random_noise1 = np.random.normal(0, 1, (n_data1, ))
# random_noise2 = np.random.normal(1, 1, (n_data2, ))
# random_noise3 = np.random.normal(2, 1, (n_data3, ))
#
# fig, ax = plt.subplots(figsize=(10, 7))
#
# ax.plot(x_data1, random_noise1)
# ax.plot(x_data2, random_noise2)
# ax.plot(x_data3, random_noise3)
#
# ax.tick_params(labelsize=20)
#
# plt.show()

'''1-8 '''
# # r'$laTex코드$' 사용할 수 있다
#
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 300)
# sin = np.sin(t)
# linear = 0.1*t
#
# fig, ax = plt.subplots(figsize=(14, 7))
# ax.plot(t, sin)
# ax.plot(t, linear)
#
# ax.set_ylim([-1.5 , 1.5])
#
# x_ticks = np.arange(-4*PI, 4*PI+0.1, PI)
# x_tickslabel = [str(i) + r'$\pi$' for i in range(-4, 5)]
#
# ax.set_xticks(x_ticks)
# ax.set_xticklabels(x_tickslabel)
#
# ax.tick_params(labelsize=20)
# ax.grid()
#
# plt.show()

'''2. Several Line Plot on Different Axes'''
# 하나의 페이지에서 여러가지 그래프 그리기
# 행렬로서 표현 다만, 인덱스이므로 0부터 시작
# plt.subplots(3, 1, figsize=(7, 10) : 3행 1열의 그래프 배




'''2-1 여러가지 그래프 그리기'''
# 발산하는 그래프를 그리게 되면 -> 값이 전부 이어지게 되는 error의 발생 : line plot은 다 연결하는 성질이 있기 떄문
# y[:-1][np.diff(y) < 0] = np.nan
# nan : Not a number -> 숫자 취급을 안함
# diff 나중값에서 처음 값을 뺀 경우

#
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 1000)
# sin = np.sin(t)
# cos = np.cos(t)
# tan = np.tan(t)
# tan[:-1][np.diff(tan) < 0] = np.nan
#
# fig, axes = plt.subplots(3, 1, figsize=(7, 10))
#
# axes[0].plot(t, sin)
# axes[1].plot(t, cos)
# axes[2].plot(t, tan)
#
# axes[2].set_ylim([-5, 5])
#
# fig.tight_layout()
# plt.show()

'''2-2'''

# np.linspace -> 하나의 벡터
# np.linspace(str, end, step).reshape(1,-1) : 행렬 list in list
# sharex : x축을 공유한다 즉 3개의 그래프에서 x 축을 하나만 그리겠다는 의미
# flatten() -> 1행 -1열로: 바로 인덱싱이 가능해진다.
'''
[[   ],
 [   ],
 [   ]]
'''
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 1000).reshape(1, -1)
# sin = np.sin(t)
# cos = np.cos(t)
# tan = np.tan(t)
# data = np.vstack((sin, cos, tan))
#
#
#
# title_list = [r'$sin(t)$', r'$cos(t)$', r'$tan(t)$']
# x_ticks = np.arange(-4*PI, 4*PI+PI, PI)
# x_ticklabels = [str(i) + r'$\pi$' for i in range(-4, 5)]  # x축의 tick Name
#
# fig, axes = plt.subplots(3, 1,
#                          figsize=(7, 10),
#                          sharex=True)
#
# # 지금 형태가 3,1 이기 때문에 윗줄부터 하나씩 -> column 2 이상인경우는 falt가 있어야 인덱싱으로 적용가능하다.
# for ax_idx, ax in enumerate(axes.flat):
#     ax.plot(t.flatten(), data[ax_idx])
#     ax.set_title(title_list[ax_idx],
#                  fontsize=30)
#     ax.tick_params(labelsize=20)
#     ax.grid()
#     if ax_idx == 2:
#         ax.set_ylim([-3,3])
#
#
#
# fig.subplots_adjust(left=0.1, right=0.95,
#                     bottom=0.05, top=0.95)
# axes[-1].set_xticks(x_ticks)
# axes[-1].set_xticklabels(x_ticklabels)
#
# plt.show()
''' flatten : 객체 반환, flat : no return'''
# https://cosmosproject.tistory.com/407
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [3,6,7]])
# flat_arr = arr.flatten()
# print(arr)
# print(flat_arr)
# print(arr.flat[4])

'''
행렬
[[1 2 3]
 [4 5 6]
 [3 6 7]]
 flatten
[1 2 3 4 5 6 3 6 7]
'''

# 3번 ax.axvline and ax.axhline
     # 점근선, 기준선, min,max를 표현할때 자주 사용된다.
'''3-1 vline'''
#
# fig, axes = plt.subplots(2, 1,
#                          figsize=(7, 7),
#                          sharex=True)
#
# axes[-1].set_xlim([-5, 5])
# axes[-1].set_ylim([-5, 5])
#
# axes[0].axvline(x=1,
#            color='black',
#            linewidth=3)
# axes[1].axvline(x=1,
#                 ymax=0.8, ymin=0.2,
#                 color='red',
#                 linewidth=3)
# plt.show()

'''3-2 hline'''
# fig, axes = plt.subplots(1, 2,
#                          figsize=(7, 10))
#
# for ax_idx in range(2):
#     axes[ax_idx].set_xlim([-5, 5])
#     axes[ax_idx].set_ylim([-5, 5])
#
# axes[0].axhline(y=1,
#                 color='green',
#                 linewidth=1)
# axes[1].axhline(y=3,
#                 xmax=0.8, xmin=0.2,
#                 color='red',
#                 linewidth=2)
#
# plt.show()

'''3-3 min,max 의 구분선'''
# ls : 라인의 모양
# lw : 라인 두께
# PI = np.pi
#
# x = np.linspace(-4*PI, 4*PI, 100)
# sin = np.sin(x)
# cos = np.cos(x)
#
# fig, ax = plt.subplots(figsize=(10,5))
#
# ax.plot(x, sin)
# ax.plot(x, cos)
# ax.axhline(y=1, ls=':', lw=1, color='gray')
# ax.axhline(y=-1, ls='-.', lw=5, color='blue')
#
# plt.show()

'''3-4 line 의 스타일'''
# 지정해 주지 않아도 알아서 색이 지정됨 tab10 순서에 따라

# x_data = np.array([0, 1])
# y_data = x_data
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(x_data, y_data)
#
# ax.plot(x_data, y_data+1,
#         linestyle='dotted')
#
# ax.plot(x_data, y_data+2,
#         linestyle='dashed')
#
# ax.plot(x_data, y_data+3,
#         linestyle='dashdot')
#
# plt.show()

'''3-5 라인 스타일 - 기호를 이용하여 그리기'''

# x_data = np.array([0, 1])
# y_data = x_data
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(x_data, y_data)
#
# ax.plot(x_data, y_data+1, ":")
#
# ax.plot(x_data, y_data+2, "-.")
#
# ax.plot(x_data, y_data+3, '--')
#
# plt.show()


'''3-6 라인 스타일 변경하여 min, max 그리기'''
#
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 500)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(t, sin)
# x_ticks = np.arange(-4*PI, 4*PI+0.1, PI)
# x_tickslabel = [str(i) + r'$\pi$' for i in range(-4, 5)]
#
# ax.set_xticks(x_ticks)
# ax.set_xticklabels(x_tickslabel)
# ax.axhline(y=1,
#            linestyle=':')
# ax.axhline(y=0,
#            color='black')
# ax.axhline(y=-1,
#            linestyle=":")
# ax.axvline(x=0,
#            color='black')
#
# plt.show()
'''4. marker style'''

'''4-1 customizing marekr'''
        # 그냥 'o' 만있으면 scatter 처럼 작동
        # marker = 'o' 라인과 같이

# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 70)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(t, sin,
#         color='black')
# ax.plot(t, sin+1,
#         marker='o',
#         color='black')
# ax.plot(t, sin+2,
#         marker='D',
#         color='black')
# ax.plot(t, sin+3,
#         marker='s',
#         color='black')
# ax.plot(t, sin+4,
#         'o') # scatter
# ax.text(10.5, 4.5,
#         s='like scatter',
#         fontsize=20)
# ax.text(5, 2.5,
#         s='line with marker',
#         fontsize=20,
#         color='red')
# plt.show()
'''4-2 marker size'''

# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 50)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(t, sin+1,
#         markerfacecolor='r',
#         markeredgecolor='b',
#         linewidth=3,
#         mew=3,
#         marker='o',
#         color='black',
#         markersize=15)
# plt.show()

'''4-3. marker color'''
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 50)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10,10)) # (가로길이, 세로길이)
#
# ax.plot(t, sin+1,
#         marker='o',
#         markerfacecolor='red',
#         markeredgecolor='green')
# plt.show()

'''4-4 edge width'''
# PI = np.pi
# t = np.linspace(-4*PI, 4*PI, 50)
# sin = np.sin(t)
#
# fig, ax = plt.subplots(figsize=(10,10)) # (가로길이, 세로길이)
#
# ax.plot(t, sin+1,
#         marker='o',
#         markerfacecolor='red',
#         markeredgecolor='green',
#         markeredgewidth=2)
# plt.tight_layout()
# plt.show()

'''5번 fmt'''

'''fmt 한번에 모아쓰기'''
        # marker, linestyle, color에 중복되는 기호가 없음
        # plot 할때 값을 하나만 넣게 되면 y_data를 넣게됨!!!!!!!!!!!!!!

# x_data = np.array([1, 2, 3, 4, 5])
# y_data = x_data
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.plot(x_data, y_data,
#         linestyle=':',
#         marker='o',
#         color='b')
# ax.plot(x_data, y_data+2, 'r^-.')
# plt.show()


''' 6번 Basic Usage of Legend'''
#         labeling
#
#         Error : No artists with labels found to put in legend. 라벨링이 되지 않음
# fig, ax = plt.subplots(figsize=(7, 6))
#
# ax.plot([1,5,3], [1, 4, 2])
# ax.legend()
# plt.show()
''' 6-1 legend font size'''
# np.random.seed(0)
#
# n_data = 100
# random_noise1 = np.random.normal(0, 1, (n_data, ))
# random_noise2 = np.random.normal(1, 1, (n_data, ))
# random_noise3 = np.random.normal(2, 1, (n_data, ))
#
# fig, ax = plt.subplots(figsize=(10, 7))
# ax.tick_params(labelsize=20)
#
# ax.plot(random_noise1,
#         label='random noise1')
# ax.plot(random_noise2,
#         label='random noise2')
# ax.plot(random_noise3,
#         label='random noise3')
#
# ax.legend()
# # ax.legend(fontsize=20) # lengend의 위치가 달라진다 -> 알아서 최적의 위치를 찾는다
# # loc => Inner : 9자리
# plt.show()

'''6-2 legend location(레전드 위치) - 그래프 내'''
# np.random.seed(0)
#
# n_data = 100
# random_noise1 = np.random.normal(0, 1, (n_data, ))
# random_noise2 = np.random.normal(1, 1, (n_data, ))
# random_noise3 = np.random.normal(2, 1, (n_data, ))
#
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.tick_params(labelsize=20)
#
# ax.plot(random_noise1,
#         label='random noise1')
# ax.plot(random_noise2,
#         label='random noise2')
# ax.plot(random_noise3,
#         label='random noise3')
#
#
# ax.legend(fontsize=20,
#           loc='lower right')
# # loc => Inner : 9자리
# plt.show()









