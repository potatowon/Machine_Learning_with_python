import numpy as np

data = 10*np.arange(1, 11)
L = len(data)
W = 3
print(data, '\n')

L_ = L - W + 1 # 총 나오는 데이터의 갯수 공식

for idx in range(L_):
    print(data[idx: idx+W]) # [0 : 0+ 3] 부터 [7 : 7 + 3] 까지 슬라이싱