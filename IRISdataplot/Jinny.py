import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

feature_names = iris.feature_names
# print(feature_names)
n_features = len(feature_names)
species = iris.target_names
# print(species)
n_species = len(species)
iris_X, iris_y = iris.data, iris.target

sepal_length = iris_X[:, 0]
sepal_width = iris_X[: , 1]
petal_length = iris_X[: , 2]
petal_width = iris_X[:, 3]

fig, axes = plt.subplots(4, 4,
                       figsize=(10, 10))
                       # 일단 이거 빼야해

#막대그래프 1
sepal_length = iris_X[:, 0]
Data = sepal_length

axes[0][0].tick_params(labelsize=20,
               length=5,
               width=1)
axes[0][0].hist(Data, rwidth=0.5)
#plt.show()

#막대그래프 2
sepal_width = iris_X[: , 1]
DAta = sepal_width

axes[1][1].tick_params(labelsize=20,
               length=5,
               width=1)
axes[1][1].hist(DAta, rwidth=0.5)
#plt.show()

#막대그래프 3
petal_length = iris_X[: , 2]
DATa = petal_length

axes[2][2].tick_params(labelsize=10,
               length=5,
               width=1)
axes[2][2].hist(DATa, rwidth=0.5)
#plt.show()

#막대그래프 4
petal_width = iris_X[:, 3]
DATA = petal_width

axes[3][3].tick_params(labelsize=10,
               length=5,
               width=1)
axes[3][3].hist(DATA, rwidth=0.5)
# plt.show()

#0-1 scatter
x_data = sepal_width
y_data = sepal_length

# fig, ax = plt.subplots(figsize=(7, 7))
axes[0][1].scatter(x_data, y_data,
           s=10,
           c=iris_y,
           alpha = 0.7)
axes[0][1].grid()
#plt.show()

#0-2 scatter
x_data = petal_length
y_data = sepal_length

# fig, ax = plt.subplots(figsize=(7, 7))
axes[0][2].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[0][2].grid()
#plt.show()

#0-3
x_data = petal_width
y_data = sepal_length

# fig, ax = plt.subplots(figsize=(7, 7))
axes[0][3].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[0][3].grid()
#plt.show()

#1-0
x_data = sepal_length
y_data = sepal_width

# fig, ax = plt.subplots(figsize=(7, 7))
axes[1][0].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[1][0].grid()
#plt.show()

#1-2
x_data = petal_length
y_data = sepal_width

# fig, ax = plt.subplots(figsize=(7, 7))
axes[1][2].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[1][2].grid()
#plt.show()

#1-3
x_data = petal_width
y_data = sepal_width

# fig, ax = plt.subplots(figsize=(7, 7))
axes[1][3].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[1][3].grid()
#plt.show()

#2-0
x_data = sepal_length
y_data = petal_length

# fig, ax = plt.subplots(figsize=(7, 7))
axes[2][0].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[2][0].grid()
#plt.show()

2-1
x_data = sepal_width
y_data = petal_length

# fig, ax = plt.subplots(figsize=(7, 7))
axes[2][1].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[2][1].grid()
# plt.show()

#2-3
x_data = petal_width
y_data = petal_length

# fig, ax = plt.subplots(figsize=(7, 7))
axes[2][3].scatter(x_data, y_data,
           s=10,
           c=iris_y,
           alpha = 0.7)
axes[2][3].grid()
# plt.show()

#3-0
x_data = sepal_length
y_data = petal_width

# fig, ax = plt.subplots(figsize=(7, 7))
axes[3][0].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[3][0].grid()
# plt.show()

#3-1
x_data = sepal_width
y_data = petal_width

# fig, ax = plt.subplots(figsize=(7, 7))
axes[3][1].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[3][1].grid()
# plt.show()

#3-2
x_data = petal_length
y_data = petal_width

# fig, ax = plt.subplots(figsize=(5, 5))
axes[3][2].scatter(x_data, y_data,
           s=20,
           c=iris_y,
           alpha = 0.7)
axes[3][2].grid()
plt.show()