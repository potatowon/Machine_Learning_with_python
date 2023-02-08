import numpy as np
import matplotlib.pyplot as plt

img = np.arange(0, 256, 50).reshape(-1, 1)
# img = np.arange(255, 0, -50).reshape(-1, 1)
img = img.repeat(100, axis=1).repeat(30, axis=0)

fig, ax = plt.subplots(figsize=(4, 8))

ax.imshow(img, cmap='gray_r')
# ax.imshow(img, cmap='gray')

ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)

plt.tight_layout()
plt.show()


