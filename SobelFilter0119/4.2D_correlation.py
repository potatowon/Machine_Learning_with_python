import numpy as np

data1 = 10*np.arange(1, 8).reshape(1, -1)
data2 = 10*np.arange(5).reshape(-1, 1)

data = data1 + data2
print(data, '\n')

filter_ = np.array([[1, 2, 5],
                    [-10, 2, -2],
                    [5, 1, -4]])

H, W = data.shape

F = filter_.shape[0] # (3, 3) 인데 그중 앞에 인덱스만
H_ = H - F + 1
W_ = W - F + 1

filtered_data = np.zeros(shape=(H_, W_))

for h_idx in range(H_):
    for w_idx in range(W_):
        window = data[h_idx : h_idx+F,
                        w_idx : w_idx + F]

        z = np.sum(window*filter_)
        print(z)

        filtered_data[h_idx, w_idx] = z

print(filtered_data)