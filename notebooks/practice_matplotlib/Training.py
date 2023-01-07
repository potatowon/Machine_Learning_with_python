# 실습
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
# data set

countries = ['Australia', 'Austria', 'Belgium', 'Canada', 'Chile',
             'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
             'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland',
             'Israel', 'Italy', 'Japan', 'Korea', 'Luxembourg',
             'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland',
             'Portuagl', 'Slovak Republic', 'Slovenia', 'Spain', 'Sweden',
             'Switzerland', 'Turkey', 'United Kingdom', 'United States']

population_denstiy = [3, 101, 367, 4, 23,
                      133, 130, 29, 16, 117,
                      227, 86, 106, 3, 65,
                      365, 203, 337, 501, 207,
                      60, 406, 17, 13, 122,
                      116, 110, 103, 91, 21,
                      194, 97, 257, 32]
private_expenditure = [1.3, 8.9, 10.0, 10.9, 12.8,
                       13.0, 13.2, 13.4, 13.5, 14.8,
                       15.0, 15.8, 16.7, 17.1, 17.2,
                       17.4, 18.1, 18.1, 18.7, 18.9,
                       19.0, 19.0, 19.5, 19.9, 20.0,
                       21.5, 21.6, 23.0, 24.0, 25.0,
                       25.9, 26.7, 28.0, 34.3]
gdp = [38.7, 37.4, 33.6, 37.5, 16.4,
       24.5, 33.2, 19.3, 32.1, 32.0,
       36.2, 19.8, 17.8, 37.7, 37.7,
       29.4, 26.6, 32.0, 31.0, 67.9,
       13.4, 38.4, 27.0, 48.2, 18.9,
       20.9, 21.8, 24.2, 26.8, 36.2,
       42.5, 13.9, 35.6, 45.7]

gdp = np.array(gdp)

# 데이터 설정
n_class = len(countries)
cmap = cm.get_cmap('tab20')
colors = [cmap(i) for i in range(17)]*2

data_dic = {str(i): None for i in countries}        # {class(key) : data(value)}

for c_idx in range(n_class):
    x_data = population_denstiy[c_idx]
    y_data = private_expenditure[c_idx]
    z_data = gdp[c_idx]
    data_dic[countries[c_idx]] = [x_data, y_data, z_data]

# 그래프 설정
        # 하나의 그래프에 하나의 legend설정 가능 -> 다른 위치로 지정하기 위해서는 그래프 필요
        # twinx() 를 이용해 x 축을 공유하는 하나의 그래프를 생성 -> 단, 그리지는 않음
            # twinx된 그래프의 x , y축 지우기 -> ax2.get_xaise().set_visible(False)

fig, ax = plt.subplots(figsize=(14, 7))
ax2 = ax.twinx()


ax.set_ylim([-4, 40])
ax.set_xlim([-50, 550])
ax.set_xlabel('Population Density(lnh./km2)', fontsize=30)
ax.set_ylabel('Private Expenditure', fontsize=30)
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

# 그래프 그리기
for class_idx in range(n_class):
    data = data_dic[countries[class_idx]]
    if class_idx < 17:
        ax.scatter(data[0], data[1],
                   s=data[2]*50,
                   facecolor=colors[class_idx],
                   alpha=0.5,
                   hatch='//')
        ax.scatter([], [],
                   s=300,
                   facecolor=colors[class_idx],
                   alpha=0.5,
                   label=countries[class_idx],
                   hatch='//')

    else:
        ax.scatter(data[0], data[1],
                   s=data[2] * 50,
                   facecolor=colors[class_idx],
                   alpha=0.5,
                   hatch='.')
        ax.scatter([], [],
                   s=300,
                   facecolor=colors[class_idx],
                   alpha=0.5,
                   label=countries[class_idx],
                   hatch='.')
for i in [10, 25, 40, 55]:
    ax2.scatter([],[],
                s=30*i,
                label=str(i),
                color='b',
                alpha=0.5)

ax2.legend(bbox_to_anchor=(0.5,1.05),
           loc='lower center',
           ncol=4,
           fontsize=12,
           title='GDP Value',
           title_fontsize=30,
           labelspacing=2,
           columnspacing=3,
           edgecolor="None",
           facecolor='None')

ax.legend(bbox_to_anchor=(1, 0.5),
          loc='center left',
          labelspacing=1,
          ncol=2,
          fontsize=12)

fig.tight_layout()
ax.grid()
plt.show()