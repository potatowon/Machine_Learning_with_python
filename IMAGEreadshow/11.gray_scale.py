import numpy as np
import matplotlib.pyplot as plt

img = np.arange(0, 151, 50).reshape(1, -1)
''' 범위가 150임에도 흰색도 나왔다. cmap='gary' 는 흰색~검은색까지의 continous 하다.
그래서 범위가 주어지면 각 끝점을 cmap의 양끝이라고 생각하고 색상을 입력해준다. 이를 보정하는 방법이 
vmax, vmin을 이용하는 것이다.
vmax=255, vmin=0 을 이용한다
'''
print(img)
img = img.repeat(100, axis=0).repeat(30, axis=1)




fig, ax = plt.subplots(figsize=(8, 4))

ax.imshow(img, cmap='gray')

ax.tick_params(left=False, labelleft=False,
               bottom=False, labelbottom=False)

plt.show()