import numpy as np
import matplotlib.pyplot as plt

img = np.arange(0, 151, 50).reshape(1, -1)
print(img)
img = img.repeat(100, axis=0).repeat(30, axis=1)
# axis=0 행방향 증가 이므로 -> 그림의 높이가 증가
# axis=1 열방향 증가 이므로 -> 각 그라데이션의 폭의 증가



fig, ax = plt.subplots(figsize=(8, 4))

ax.imshow(img, cmap='gray', vmax=255, vmin=0)

ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)


plt.tight_layout()
plt.show()