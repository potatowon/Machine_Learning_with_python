import matplotlib.pyplot as plt
import numpy as np

# 1번 named colors
'''
color_list = ['b', 'g', 'r', 'c', 'm', 'y']

fig, ax = plt.subplots(figsize=(5,10))
ax.set_xlim([-1,1])
ax.set_ylim([-1, len(color_list)])

for c_idx, c in enumerate(color_list):
    ax.text(0, c_idx,
            "color="+c,
            fontsize = 20,
            ha='center',
            color=c)
    # "color="+c : 원하는 텍스트를 출력하는 것
    
plt.show()
'''

# Named Colors(tab10 Colors)
# Case-insensitive Tableau Colors from 'T10' categorical palette
'''
color_list = ['tab:blue', 'tab:orange',
              'tab:green', 'tab:red',
              'tab:purple', 'tab:brown',
              'tab:pink', 'tab:gray',
              'tab:olive', 'tab:cyan']
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_xlim([-1,1])
ax.set_ylim([-1, len(color_list)])

for c_idx, c in enumerate(color_list):
    ax.text(0, c_idx,
            "color="+c,
            ha='center',
            fontsize=20,
            color=c)

plt.show()
'''
# 3번 RGB Colors
'''
color_list = [(1., 0., 0.),
              (0., 1., 0.),
              (0., 0., 1.),
              (0.8, 0.4, 0.2)]

# tuple 로서 rgb 값을 선택할 수 있다 0 ~ 1 값으로 안에 선택 가능
fig, ax = plt.subplots(figsize=(5,10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, len(color_list)])

for c_idx, c in enumerate(color_list):
    ax.text(0, c_idx,
            f"color={c}",
            ha='center',
            fontsize=20,
            color=c)
plt.show()
'''
# Discrete Colormaps (lut Argument)
# Matplot에는 여러 개의 Color를 섞은 Colormap이 있습니다.
# 다음 코드로 cmap의 모든 이름들을 가져올 수 있습니다.
# 참고 https://wikidocs.net/141538
import matplotlib.cm as cm
'''
cmap = cm.get_cmap('tab20', lut=20) # tab20 에서 20개를 가져온다?
fig, ax = plt.subplots(figsize=(8,8))

for i in range(20):
    ax.scatter(i, i, color=cmap(i), s=100)
plt.show()
'''

# Continuous Colormaps(lut Argument)
'''
n_color = 10
cmap = cm.get_cmap('rainbow', lut=n_color)

for c_idx in range(n_color):
    print(cmap(c_idx))
'''

# Continuous Colormaps (lut Argument)
'''
n_color = 30
cmap = cm.get_cmap('rainbow', lut=n_color)

fig, ax = plt.subplots(figsize=(15,10))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, n_color])

for c_idx in range(n_color):
    color = cmap(c_idx)

    ax.text(0, c_idx,
            f"color={cmap(c_idx)}",
            fontsize=15,
            ha='center',
            color=color)

plt.show()
'''
# ax.plot and ax.scatter
'''
np.random.seed(0)

n_data = 100
x_data = np.random.normal(0, 1, (n_data, ))
y_data = np.random.normal(0, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(7,7))
ax.scatter(x_data, y_data, s=100, color='r')
# ax.plot(x_data, y_data, '--', markersize=10, color='red') # 그리기
plt.show()
'''


# ax.plot and ax.scatter

'''
np.random.seed(0)

x_min, x_max = -5, 5
n_data = 300

x_data = np.random.uniform(x_min, x_max, n_data)
y_data = x_data + 0.5*np.random.normal(0,1, n_data)

pred_x = np.linspace(x_min, x_max,5)
pred_y = pred_x

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x_data, y_data,
           color='green')
# Model 을 학습 시키고 난 예측값을 Line plot 으로 그려냄
ax.plot(pred_x, pred_y,
        color='r',
        linewidth=3)

plt.show()
print(pred_x)
'''

# Size Array and Color Array
'''
n_data = 10
x_data = np.linspace(0,10, n_data)
y_data = np.linspace(0,10, n_data)

s_arr = np.linspace(10, 500, n_data)

fig, ax = plt.subplots(figsize=(10,10))
# s : size -> s_arr 10,500을 같은 간격의 10가지의 값을 각 size로 지정한다
ax.scatter(x_data, y_data, s=s_arr)

plt.show()
'''

# Size array and Color array
'''
n_data= 10
x_data = np.linspace(0, 10, n_data)
y_data = np.linspace(0, 10, n_data)
# rgb 0 ~ 1 사이 -> 튜플로 적용하면 색상을 변경할 수 있다 matplotlib

c_arr = [(c/n_data,)*3 for c in range(n_data)]

fig, ax = plt.subplots(figsize=(10,10))
# 정육면체의 대각선 방향을 따르는 값의 색상들은 gray scale
ax.scatter(x_data, y_data,
           s=500,
           c=c_arr)

plt.show()
'''

# Size array and Color array
'''
n_data = 10
x_data = np.linspace(0,10, n_data)
y_data = np.linspace(0,10, n_data)

c_arr = [(c/n_data,)*3 for c in range(n_data)]
s_arr = np.linspace(10, 500, n_data)

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x_data, y_data,
           s=s_arr,
           c=c_arr)

plt.show()
'''

# Size array and color array
'''
np.random.seed(0)

n_data = 500
x_data = np.random.normal(0, 1, size=(n_data, ))
y_data = np.random.normal(0, 1, size=(n_data, ))
s_arr = np.random.uniform(100, 500, n_data)
c_arr = [np.random.uniform(0,1,3) for _ in range(n_data)]

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x_data, y_data,
           s=s_arr,
           c=c_arr)


ax.scatter(x_data, y_data,
           s=s_arr,
           c=c_arr,
           alpha=0.9)

plt.show()
'''

# Color Array at c argument
'''
import matplotlib.cm as cm

PI = np.pi
n_point = 100
t = np.linspace(-4*PI, 4*PI, n_point)
sin = np.sin(t)

cmap = cm.get_cmap('Reds', lut=n_point)
c_arr = [cmap(c_idx) for c_idx in range(n_point)]

fig, ax = plt.subplots(figsize=(15, 10))
ax.scatter(t, sin,
           s=300,
           c=c_arr)

plt.show()
'''

# Advaced Mackers
'''
fig, ax = plt.subplots(figsize=(5,5))

ax.scatter(0, 0, s=10000,
           marker='*',
           facecolor='y',
           edgecolor='gold',
           linewidth=5)
ax.text(x=0, y=0,
        ha='center', va='center',
        s='Miran')
plt.show()
# facecolor : marker 색상
# edgecolor : 테두리 색상
# linewidth : 테두리 두께
'''

# Advaced Markers
'''
n_data =100
x_data = np.random.normal(0, 1, (n_data,))
y_data = np.random.normal(0, 1, (n_data,))

fig, ax = plt.subplots(figsize=(5,5))

ax.scatter(x_data, y_data,
           s=200,
           marker='^',
           facecolor='None',
           edgecolor='green',
           linewidth=2)
plt.show()
'''

# Advanced Markers
'''
np.random.seed(0)

n_data = 200
x_data = np.random.normal(0, 1, (n_data, ))
y_data = np.random.normal(0, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(7,7))
ax.scatter(x_data, y_data,
           s=300,
           facecolor='None',
           edgecolor='tab:blue',
           linewidth=3,
           alpha=0.5)

plt.show()
'''