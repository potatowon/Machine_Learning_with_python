import numpy as np
import matplotlib.pyplot as plt
# 색상은 - 0~ 255
white_patch = 255*np.ones(shape=(10, 10)) # (10, 10) 짜리의 흰색 패치 만들기  => 255로 채우기
black_patch = 0*np.ones(shape=(10, 10)) # (10, 10) 짜리의 검은색 패치 만들기 => 0으로 채우기

img1 = np.hstack([white_patch, black_patch]) # [흰, 검] (10, 20) 의 이미지 만들기
img2 = np.hstack([black_patch, white_patch]) # [검, 흰] (10, 20) 의 이미지 만들기
img = np.vstack([img1, img2])

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img, cmap='gray') #colormap = gray

ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)

plt.show()