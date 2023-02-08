''' ax.imread'''

import  matplotlib.pyplot as plt

# img = plt.imread('./Lenna.png')
# print(img.shape)
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# ax.imshow(img)
# ax.grid(color='white')
# plt.show()

'''Imge coordinates'''

img = plt.imread('./Lenna.png')
print(img.shape)

fig, axes = plt.subplots(1, 2, figsize=(14, 7))
fig.tight_layout()

axes[0].tick_params(labelsize=20)
axes[1].tick_params(labelsize=20)

axes[0].imshow(img)

img_cropped = img[:300, :300, :] # [H, W, RGB]
axes[1].imshow(img_cropped)

plt.show()


''' Image Coordinate(2)'''

# img = plt.imread('./Lenna.png')
# print(img.shape)
#
# fig, axes = plt.subplots(1, 2, figsize=(14, 7))
# fig.tight_layout()
#
# axes[0].tick_params(labelsize=20)
# axes[1].tick_params(labelsize=20)
#
# axes[0].imshow(img)
#
# img_cropped = img[200:400, 150:350, :]
#
# axes[1].imshow(img_cropped)
#
# plt.show()

''' ax.imshow -> color map '''
'''
행렬은 흑백이미지 이다. viridis 라는 default Color map 이 지정되어있기 때문이다.
'''
# img = plt.imread('./Lenna.png')
# print(img.shape)
#
# r_img = img[:, :, 0]
# g_img = img[:, :, 1]
# b_img = img[:, :, 2]
#
# print(r_img.shape)
# print(g_img.shape)
# print(b_img.shape)
#
# fig, axes = plt.subplots(2, 2, figsize=(15, 15))
#
# for ax in axes.flatten():
#     ax.tick_params(labelleft=False,
#                    labelbottom=False)
#
#     for spine_loc, spine in ax.spines.items(): # 축을 커스터마이징 하는 방법 (참고 : https://yeko90.tistory.com/entry/matplotlib-기초-spine-축-커스터마이징-방법)
#         spine.set_visible(False)
# fig.tight_layout()
#
# # ax.spines 는 그 값들을 dictionary의 형태로 가지고 있다. -> 따라서 이를 편리하게 for 문을 이용하여 조정 가능하다.
# ## key 값으로 left, right, top, bottom
# # 비슷한거 violin 그래프에서 각 요소들의 색상을 변경할때 사용했었다. 노션 matplotlib 연습 23번 참고
#
# axes[0, 0].imshow(img)
# axes[0, 1].imshow(r_img)
# axes[1, 0].imshow(g_img)
# axes[1, 1].imshow(b_img)
#
# plt.show()

''' ax.imshow rgb 0~ 255 컬러는 8비트  0 0 0 0 0 0 0 0(black) ~ 1 1 1 1 1 1 1 1(white) '''

#
# img = plt.imread('./Lenna.png')
# print(img.shape)
#
# r_img = img[:, :, 0]
# g_img = img[:, :, 1]
# b_img = img[:, :, 2]
#
# print(r_img.shape)
# print(g_img.shape)
# print(b_img.shape)
#
# fig, axes = plt.subplots(2, 2, figsize=(15, 15))
# for ax in axes.flatten():
#     ax.tick_params(labelleft=False,
#                    labelbottom=False)
#
#     for spine_loc, spine in ax.spines.items():
#         spine.set_visible(False)
#
# fig.tight_layout()
#
# axes[0, 0].imshow(img)
# axes[0, 1].imshow(r_img, cmap='gray')
# axes[1, 0].imshow(g_img, cmap='gray')
# axes[1, 1].imshow(b_img, cmap='gray')
#
#
# plt.show()
''' continous color map 을 가지고 오면 각 픽셀들이 가진 값에 비례하여 중간값을 알아서 배분해준다 '''
#
# img = plt.imread('./Lenna.png')
# print(img.shape)
#
# r_img = img[:, :, 0]
# g_img = img[:, :, 1]
# b_img = img[:, :, 2]
#
# print(r_img.shape)
# print(g_img.shape)
# print(b_img.shape)
#
# fig, axes = plt.subplots(2, 2, figsize=(15, 15))
# for ax in axes.flatten():
#     ax.tick_params(labelleft=False,
#                    labelbottom=False)
#
#     for spine_loc, spine in ax.spines.items():
#         spine.set_visible(False)
#
# fig.tight_layout()
#
# axes[0, 0].imshow(img)
# axes[0, 1].imshow(r_img, cmap='Reds_r')
# axes[1, 0].imshow(g_img, cmap='Greens_r')
# axes[1, 1].imshow(b_img, cmap='Blues_r')
#
# plt.show()
#
#

#
img = plt.imread('./rgb.png')
print(img.shape)

r_img = img[:, :, 0]
g_img = img[:, :, 1]
b_img = img[:, :, 2]

print(r_img.shape)
print(g_img.shape)
print(b_img.shape)

fig, axes = plt.subplots(2, 2, figsize=(15, 15))
for ax in axes.flatten():
    ax.tick_params(labelleft=False,
                   labelbottom=False)

    for spine_loc, spine in ax.spines.items():
        spine.set_visible(False)

fig.tight_layout()

axes[0, 0].imshow(img)
axes[0, 1].imshow(r_img, cmap='Reds') # Reds_r 컬러맵의 reverse
axes[1, 0].imshow(g_img, cmap='Greens')
axes[1, 1].imshow(b_img, cmap='Blues')

plt.show()
