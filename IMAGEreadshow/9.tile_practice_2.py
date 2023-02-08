import numpy as np
import matplotlib.pyplot as plt

white_patch = 255*np.ones(shape=(10, 10))
gray_patch = 128*np.ones(shape=(10, 10))
black_pacth = 0*np.ones(shape=(10, 10))

img1 = np.hstack([white_patch, gray_patch])
img2 = np.hstack([gray_patch, black_pacth])
img = np.vstack([img1, img2])

img = np.tile(img, reps=[4, 4])

fig, ax = plt.subplots(figsize=(7, 7))

ax.imshow(img, cmap='gray')

ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)

plt.tight_layout()
plt.show()
