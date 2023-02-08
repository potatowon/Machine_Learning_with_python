'''tile'''

import numpy as np

data = np.arange(6).reshape(2, 3)

print(data)
## reps=[n, m]
      # n : 행 방향 반복 횟수
      # m : 열방향 반복 횟수
print("tile(axis=0: \n",
      np.tile(data, reps=[3, 1]))

print("tile(axis=1: \n",
      np.tile(data, reps=[1, 3]))

print("tile(axis=0 & axis=1): \n",
      np.tile(data, reps=[3, 3]))