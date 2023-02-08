''' np.repeat & np. tile'''

import numpy as np

data = np.arange(5) # np.array[0, 1, 2, 3, 4]
print(data)

# np.repeat => 원소별 반복
print("repeat: ", np.repeat(data, repeats=3))

# np.tile => 전체 패턴의 반복

print("tile: ", np.tile(data, reps=3))
