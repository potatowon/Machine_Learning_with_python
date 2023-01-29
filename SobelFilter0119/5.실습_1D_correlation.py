''' for 문 없이 1D correlation 를 구현해 보세요
-> '''

import numpy as np

np.random.seed(0)

data = np.random.randint(-1, 2, (10, ))
filter_ = np.array([-1, 1, -1])
F = len(filter_)
L = len(data)
L_ = L - F + 1
print(data)
data_idx_row = np.arange(F).reshape(1, -1) # 0,1,2
data_idx_col = np.arange(L_).reshape(-1, 1) # 0,1,2,3,4,5,6,7
data_idx = data_idx_row + data_idx_col

data_arr = data[data_idx]
print(data_arr)
filter_ = np.transpose(filter_)

filtered_data = data_arr.dot(filter_)

print(filtered_data)
# 012 123 234 345 456 567 678 789