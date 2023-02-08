import numpy as np

data = np.arange(6).reshape(2, 3)
print(data)

#axis = 0 : 행 방향 반복
print("repeat(axis=0)\n", np.repeat(data, repeats=3, axis=0))

# axis = 1 : 열 방향 반복
print("repeat(axis=1)\n", np.repeat(data, repeats=3, axis=1))

# 행 방향으로 2번 반복 후 열방향으로 3번 반복
print("repeat(axis=0 and axis=1 \n", np.repeat(np.repeat(data, repeats=2, axis=0), repeats=3, axis=1))