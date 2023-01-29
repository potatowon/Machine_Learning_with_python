import numpy as np
import matplotlib.pyplot as plt

white_patch = 1 * np.ones(shape=(10, 10))
black_patch = 0 * np.ones(shape=(10, 10))

img1 = np.hstack([white_patch, black_patch])
img2 = np.hstack([black_patch, white_patch])
img = np.vstack([img1, img2])

img = np.tile(img, reps=[2, 2])
# print(img.shape)
H, W = img.shape
x_filter = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
y_filter = np.array([[-1, -2, -1],
                     [0, 0, 0],
                     [1, 2, 1]])

F = x_filter.shape[0]
H_ = H - F + 1
W_ = W - F + 1

filtered_x_data = np.zeros(shape=(H_, W_))
filtered_y_data = np.zeros(shape=(H_, W_))
for h_idx in range(H_):
    for w_idx in range(W_):
        window = img[h_idx:h_idx+F,
                    w_idx:w_idx+F]

        z = np.sum(window*x_filter)
        u = np.sum(window*y_filter)
        filtered_x_data[h_idx, w_idx] = z
        filtered_y_data[h_idx, w_idx] = u
# np.set_printoptions(threshold=np.inf, linewidth=np.inf)
# print(filtered_data)
filtered_data = filtered_x_data + filtered_y_data

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

for ax in axes.flatten():
    ax.tick_params(left=False, labelleft=False,
                   bottom=False, labelbottom=False)



axes[0].imshow(img, cmap='gray')
axes[1].imshow(filtered_data, cmap='gray')

plt.tight_layout()
plt.show()
