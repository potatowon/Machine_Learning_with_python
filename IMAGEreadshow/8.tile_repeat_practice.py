import numpy as np
import matplotlib.pyplot as plt

white_patch = 255*np.ones(shape=(5, 5))
black_patch = 0*np.ones(shape=(5, 5))

img1 = np.hstack([white_patch, black_patch])
img2 = np.hstack([black_patch, white_patch])
img = np.vstack([img1, img2])

img_pattern = np.tile(img, reps=[4, 4])

fig, ax = plt.subplots(figsize=(7, 7))

ax.imshow(img_pattern, cmap='gray') #colormap = gray

ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)

plt.tight_layout()
plt.show()